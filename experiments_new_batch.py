import argparse
import mysql.connector
from mysql.connector import Error
import json
import random
from dotenv import load_dotenv
from openai import OpenAI
from openai import APITimeoutError
import os
import time
import requests.exceptions
import ollama
import requests

from llamafactory.chat import ChatModel
from llamafactory.extras.misc import torch_gc

import logging

# Suppress info and warning messages, only show errors
logging.getLogger().setLevel(logging.ERROR)


TIMES = 300 
connection = None 
chat_model = None

def is_json(my_string):
    try:
        json_object = json.loads(my_string)
    except ValueError as e:
        return False
    return True


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all the rows from the result
        connection.commit()
        # change all the letter in query to lower case
        query = query.lower()

        if "insert" in query or "delete" in query or "update" in query:
            return ["Succeed"]
        else:
            return [r[0] for r in result]
    except Error as e:
        #print(query)
        #print(f"Error: '{e}'")
        
        connection.rollback()

        return ["Fail"]
    finally:
        cursor.close()



def connect_to_server():
    global connection
    try:
        connection = mysql.connector.connect(
            #host='localhost',
            #password='1q2w3e4r5t',
            user='root',
            password='',
            unix_socket='/var/run/mysqld/mysqld.sock'  # Replace with the actual path to your MySQL socket
        )      

        if connection.is_connected():
            #print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def concatenate_prompt(prompts):
    prompt = ""
    for p in prompts:
        prompt += p + "\n"
    return prompt

def read_data(name,encoding):
    data = {}
    if os.path.exists(f"{name}_{encoding}.json"):
        with open(f"{name}_{encoding}.json", "r") as file:
            data = json.load(file)
    return data



def generate_system_prompt(common_prompts,encoding,prompting):
    prompting_translations = {"zero_shot":"ZERO-SHOT","zero_shot_cot":"ZERO-COT","few_shot":"FEW-SHOT","few_shot_cot":"FEW-SHOT-COT"}
    system_prompt = concatenate_prompt(common_prompts[encoding]["system_prompt"])
    
    system_prompt += concatenate_prompt(common_prompts[encoding][prompting_translations[prompting]])

    #system_prompt += concatenate_prompt(common_prompts[encoding]["drop_database"])
    #system_prompt += concatenate_prompt(common_prompts[encoding]["create_database"])
    #system_prompt += concatenate_prompt(common_prompts[encoding]["use_database"])



    return system_prompt

def random_combination(n, k):
    combination = random.sample(range(n), min(k,n))

    for i in range(k-n):
        random_index = random.randint(0, n-1)
        combination.append(random_index)
    #print(sorted(combination))

    return sorted(combination)


def generate_query_result_pair(common_prompts,all_prompts,encoding,scale, balance, overlap, operation=None):
    db_index = random.randint(1, 20)
    #print(f"db_index: {db_index}")
    
    sql_data = all_prompts["sql"][db_index]
    data = all_prompts[encoding][db_index]

    


    sql_populating_query = ""
    populating_query = ""

    sql_query = ""
    query = ""

    tmp_sql_insert_populating_queries = []
    tmp_sql_delete_update_populating_queries = {}

    tmp_insert_populating_queries = []
    tmp_delete_update_populating_queries = {}

    
    insert_scale = int(scale * balance)
    delete_update_scale = int(scale * (1 - balance))
    select_scale = int(scale * 0.1)


    radius = int(overlap * insert_scale)


    # generate the populating query
    for i in range(insert_scale+1):
        tmp_sql_delete_update_populating_queries[i] = []
        tmp_delete_update_populating_queries[i] = []

    
    # choose insert_scale number of index from the insert queries
    random_index_list = random_combination(len(sql_data["insert"]), insert_scale)

    for i in range(insert_scale):
        # get a random number between 0 and len(data["insert"])
        random_index = random_index_list[i]

        tmp_sql_insert_populating_queries.append(sql_data["insert"][random_index])
        tmp_insert_populating_queries.append(data["insert"][random_index])

    for i in range(select_scale):
        db_query_categories = list(data["select"].keys())

        category_index = random.randint(0, len(db_query_categories)-1)
        category = db_query_categories[category_index]

        db_queries = sql_data["select"][category]
        queries = data["select"][category]

        random_index = random.randint(0, len(db_queries)-1)

        sql_query = db_queries[random_index]
        query = queries[random_index]

        random_index_in_populating_queries = random.randint(insert_scale-radius*2,insert_scale)
        

        tmp_sql_delete_update_populating_queries[random_index_in_populating_queries].append(sql_query)
        tmp_delete_update_populating_queries[random_index_in_populating_queries].append(query)

    for i in range(delete_update_scale):
        # get a random number between 0 and 1
        random_number = random.random()

        

        if random_number <= 0.5: # insert a delete query
            # get a random number between 0 and 1
            random_index_in_populating_queries = random.randint(insert_scale-radius*2,insert_scale)
            random_index = random.randint(0, len(sql_data["delete"])-1)
            tmp_sql_delete_update_populating_queries[random_index_in_populating_queries].append(sql_data["delete"][random_index])
            tmp_delete_update_populating_queries[random_index_in_populating_queries].append(data["delete"][random_index])
        else: # insert an update query
            random_index_in_populating_queries= random.randint(insert_scale-radius*2,insert_scale)
            random_index = random.randint(0, len(sql_data["update"])-1)
            tmp_sql_delete_update_populating_queries[random_index_in_populating_queries].append(sql_data["update"][random_index])
            tmp_delete_update_populating_queries[random_index_in_populating_queries].append(data["update"][random_index])

    for i in range(insert_scale+1):
        for j in range(len(tmp_sql_delete_update_populating_queries[i])):
            sql_populating_query += tmp_sql_delete_update_populating_queries[i][j] + "\n"
            populating_query += tmp_delete_update_populating_queries[i][j] + "\n"
        if i < insert_scale:
            sql_populating_query += tmp_sql_insert_populating_queries[i] + "\n"
            populating_query += tmp_insert_populating_queries[i] + "\n"
    

    
    sql_populating_query_create_database = concatenate_prompt(sql_data["drop_database"]) 
    sql_populating_query_create_database += concatenate_prompt(sql_data["create_database"]) 
    sql_populating_query_create_database += concatenate_prompt(sql_data["use_database"])

    sql_populating_query_for_create_tables = ""
    sql_populating_query_for_create_tables += concatenate_prompt(sql_data["create_tables"]) 
    sql_populating_query =  sql_populating_query_create_database + sql_populating_query_for_create_tables + sql_populating_query

    

    populating_query_create_database = concatenate_prompt(data["drop_database"])
    populating_query_create_database += concatenate_prompt(data["create_database"])
    populating_query_create_database += concatenate_prompt(data["use_database"])

    #populating_query_create_database += concatenate_prompt(data["drop_tables"])
    populating_query_for_create_tables = ""
    populating_query_for_create_tables += concatenate_prompt(data["create_tables"])

    populating_query = populating_query_create_database + populating_query_for_create_tables + populating_query

    #populating_query = concatenate_prompt(common_prompts[encoding]["user_prompt_1"]) + populating_query


    if operation == None:
        operation = random.choice(["insert","delete","update","select"])
        
    # generate the query
    if operation == "insert" or operation == "delete" or operation == "update":
        random_index = random.randint(0, len(data[operation])-1)
        sql_query = sql_data[operation][random_index]
        query = data[operation][random_index]

    elif operation == "select":

        db_query_categories = list(data["select"].keys())

        category_index = random.randint(0, len(db_query_categories)-1)
        category = db_query_categories[category_index]

        db_queries = sql_data["select"][category]
        queries = data["select"][category]

        random_index = random.randint(0, len(db_queries)-1)

        sql_query = db_queries[random_index]
        query = queries[random_index]
    else:
        category = operation

        db_queries = sql_data["select"][category]
        queries = data["select"][category]

        random_index = random.randint(0, len(db_queries)-1)
        sql_query = db_queries[random_index]
        query = queries[random_index]

    populating_query += query + "\n"
    sql_populating_query += sql_query + "\n"

    populating_queries = populating_query.split("\n")[:-1]
    sql_populating_queries = sql_populating_query.split("\n")[:-1]
    #print(populating_query)
    #print(sql_populating_queries)
    #print(query)

    # execute the db_populating_query and db_query
    # now populating query include original population query and the new query
    true_results = []
    #connection = connect_to_server()
    if connection is not None:    
        #print("populating db")
        for query in sql_populating_queries:
            true_result = execute_query(connection, query)
            if "DROP DATABASE" in query or "CREATE DATABASE" in query or "USE test" in query or "CREATE TABLE" in query: 
                if len(true_result) == 0:
                    true_result = ["Succeed"]
                else:
                    true_result = ["Fail"]



            true_results.append(true_result)
        #print("executing query")
        #true_result = execute_query(connection, sql_query)

        #connection.close()
        #print("Connection closed")
    
    # true_result is an array
    return populating_queries, true_results



def calculate_accuracy(true_result, result,user_prompt):
    # result is a string
    # true_result is an array
    #print("in calculate_accuracy")
    #print(type(true_result))
    if "Fail" in true_result:
        if "Fail" in result:
            return 1
        else:
            #print("Fail in true_result")
            return 0
    elif "Succeed" in true_result:
        if "Succeed" in result:
            return 1
        else:
            #print("Succeed in true_result")
            return 0
    else:
        #true_result = json.loads(true_result)
        # replace ' with " in the result"
        result = result.replace("'", "\"")
        
        try:
            if not is_json(result):
                return 0

            result = json.loads(result)
            if not type(result) == list:
                #print(true_result)
                #print(result)
                #print("result not a list")

                return 0
            
            if len(result) > 0:
                if type(result[0]) == list or type(result[0]) == tuple:
                    result = [r[0] for r in result]
                #elif not type(result[0]) == int and not type(result[0]) == float:
                    #print(true_result)
                    #print(result)

                    #print(f"Accuracy: {accuracy}")
                    #print("result not a list of number")
                    #return 0

            order_accuracy = 1
            if "order by" in user_prompt.split("\n")[-1].lower():
                
                for k in range(1,min(len(true_result),len(result))+1):
                    result_overlap = set(true_result[:k]).intersection(set(result[:k]))
                    result_union = set(true_result[:k]).union(set(result[:k]))
                    
                    order_accuracy += len(result_overlap) / len(result_union)
                

                order_accuracy = order_accuracy / (min(len(true_result),len(result))+1)
                
            
            
            result_overlap = set(true_result).intersection(set(result))
            result_union = set(true_result).union(set(result))
            if len(result_union) == 0:
                #print("union is 0")
                return 1 * order_accuracy  
            else:
                #print("union is not 0")
                #print(result_union)
                #print(len(true_result))
                #print(len(result))
           
                return len(result_overlap) / len(result_union) * order_accuracy
            



            #print(f"result_overlap: {result_overlap}")
            #print(f"result_union: {result_union}")
        except json.JSONDecodeError as e:
            print("json decode error")
            return 0
        except Exception as e:
            print(e)
            return 0

def get_samples(common_prompts,all_prompts,encoding,scale, balance, overlap, model, prompting, operation,samples):
    for t in range(20):

        system_prompt = generate_system_prompt(common_prompts,encoding,prompting)
        #print(system_prompt)
           
    
        
        queries, true_results = generate_query_result_pair(common_prompts,all_prompts,encoding, scale, balance, overlap, operation)
        
        messages = [{"role": "system", "content": system_prompt}]
        
            
        user_message = ""
        for i in range(len(queries)):
            query = queries[i]
            # true_result is an array
            true_result = true_results[i]
            
            if "few_shot" in prompting:
                messages.append({"role": "user", "content": query})
                if "Succeed" in true_result or "Fail" in true_result:
                    messages.append({"role": "assistant", "content": true_result[0]})
                else:
                    messages.append({"role": "assistant", "content": json.dumps(true_result)})
            else:
                user_message += query + "\n"
                
                if i == len(queries)-1:
                    messages.append({"role": "user", "content": user_message})
                    if "Succeed" in true_result or "Fail" in true_result:
                        messages.append({"role": "assistant", "content": true_result[0]})
                    else:
                        messages.append({"role": "assistant", "content": json.dumps(true_result)})

                
        
            
        sample = {"messages":messages}
        samples.append(sample)


def run_experiment(common_prompts,all_prompts,encoding,scale, balance, overlap, model, prompting, operation):

    accuracy = 0

    accuracy_1 = 0
    accuracy_2 = 0

    accuracy_1_count = 0

    global chat_model

    # repeat the experiment TIMES times
    for t in range(TIMES):

        system_prompt = generate_system_prompt(common_prompts,encoding,prompting)
        #print(system_prompt)
           
    
        
        queries, true_results = generate_query_result_pair(common_prompts,all_prompts,encoding, scale, balance, overlap, operation)

        if not len(true_results) == len(queries):
            time.sleep(1)
            t = t - 1
            continue
            
        messages = [{"role": "system", "content": system_prompt}]
        user_message = ""
        
        for i in range(len(queries)-1):
            query = queries[i]
            # true_result is an array
            true_result = true_results[i]
            
            if "few_shot" in prompting:
                messages.append({"role": "user", "content": query})
                if "Succeed" in true_result or "Fail" in true_result:
                    messages.append({"role": "assistant", "content": true_result[0]})
                else:
                    messages.append({"role": "assistant", "content": json.dumps(true_result)})
            else:
                user_message += query + "\n"
                
  
        if "few_shot" in prompting:
            messages.append({"role": "user", "content": queries[-1]})
        else:
            user_message += queries[-1] + "\n"
            messages.append({"role": "user", "content": user_message})
        true_result = true_results[-1]

        result = ""
        
        
                

        if model == "gpt4":
            # Load environment variables from the .env file
            load_dotenv()

            # Fetch the API key from the environment variable
            api_key = os.getenv("OPENAI_API_KEY")

            # Initialize the OpenAI client with the API key
            client = OpenAI(api_key=api_key)

            #print("start api call")
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages= messages,
                    temperature=0.5,  # Set the temperature here (adjust as needed)
                    timeout=25  # Set a timeout of 10 seconds
                )
                
                
            except APITimeoutError:
                t = t-1
                time.sleep(1)
                continue
            #print("end api call")

            # get the response
            result = response.choices[0].message.content

        elif model == "llama3.1-8B":
            try:
                response = ollama.chat(model='llama3.1', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

      
        elif model == "mistral":
            try:
                response = ollama.chat(model='mistral', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue
        
        elif model == "gemma2":
            try:
                response = ollama.chat(model='gemma2', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

        elif model == "codellama":
            try:
                response = ollama.chat(model='codellama', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

        elif model == "phi3":
            try:
                response = ollama.chat(model='phi3', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

        elif model == "fine_tuned_llama3.1-8B":
            try:
                if "few_shot" in prompting:
               
                    args = dict(
                        model_name_or_path="unsloth/llama-3-8b-Instruct-bnb-4bit", # use bnb-4bit-quantized Llama-3-8B-Instruct model
                        adapter_name_or_path="llama3_lora",            # load the saved LoRA adapters
                        template="llama3",                     # same to the one in training
                        finetuning_type="lora",                  # same to the one in training
                        quantization_bit=4,                    # load 4-bit quantized model
                        )
                else:
                    args = dict(
                        model_name_or_path="unsloth/llama-3-8b-Instruct-bnb-4bit", # use bnb-4bit-quantized Llama-3-8B-Instruct model
                        adapter_name_or_path="llama3_lora_zero_shot",            # load the saved LoRA adapters
                        template="llama3",                     # same to the one in training
                        finetuning_type="lora",                  # same to the one in training
                        quantization_bit=4,                    # load 4-bit quantized model
                        )
                if chat_model is None:               
                    chat_model = ChatModel(args)
                response = chat_model.chat(messages=messages, temperature=0.5)
                result = response[0].response_text
            
                #time.sleep(1)
            
          

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

        elif model == "llama3.2":
            try:
                response = ollama.chat(model='llama3.2', messages=messages)
                result = response['message']['content']
            except requests.exceptions.Timeout:
                print("The request timed out.")
                t = t - 1
                time.sleep(1)
                continue

            except Exception as e:
                print(f"An error occurred: {e}")
                
                time.sleep(1)
                continue

        result_array = result.split("\n")
        k = len(result_array)-1
        while k >= 0:
            if result_array[k] == "" or result_array[k] == "```":
                k = k - 1
            else:
                break
        result = result_array[k]

        
        accuracy_delta = calculate_accuracy(true_result, result,queries[-1])
        print(f"Accuracy delta: {accuracy_delta}")
        accuracy += accuracy_delta

        if not operation in ["update","delete","insert"]:# "select" in user_prompt.split("\n")[-1].lower():
            if not len(true_result) == 0:
                accuracy_1 += accuracy_delta
                accuracy_1_count += 1
            else:
                accuracy_2 += accuracy_delta

        else:
            if "Succeed" in true_result:
                accuracy_1 += accuracy_delta
                accuracy_1_count += 1
            else:
                accuracy_2 += accuracy_delta

        print(f"round {t}: accuracy_1: {accuracy_1}, accuracy_2: {accuracy_2}") 

        
        print(true_result)
        print(result)
        #print(response)


    
        

    #accuracy = accuracy / TIMES
    if not accuracy_1_count == 0:
        accuracy_1 = accuracy_1 / accuracy_1_count
    if not TIMES - accuracy_1_count == 0:
        accuracy_2 = accuracy_2 / (TIMES - accuracy_1_count)

    if not operation in ["update","delete","insert"]:#"select" in user_prompt.split("\n")[-1].lower():
        accuracy = accuracy_1 * 0.9 + accuracy_2 * 0.1
    else:
        accuracy = (accuracy_1 + accuracy_2) / 2
    


    print(f"Total Accuracy: {accuracy}")
    return accuracy

def main():
    
    # Read cmd line arguments with argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--model', type=str, default="llama3.1-8B", help='Model to evaluate')

    parser.add_argument('--prompting', type=str, default='zero_shot', help='Prompting strategy')
    parser.add_argument('--encoding', type=str, default='sql', help='Encoding method for data and query')
    parser.add_argument('--operation', type=str, default='select', help='Dataset query operation')

    parser.add_argument('--scale', type=int, default=50, help='Number of operations in the dataset')
    parser.add_argument('--balance', type=float, default=0.5, help='Ratio of insert in the operations in the dataset, a number between 0 and 1')
    parser.add_argument('--overlap', type=float, default=1, help='Ratio of overlap between the operations in the dataset, a number between 0 and 1')

    parser.add_argument('--generate_sample', type=bool, default=False, help='If generate the sample data or not') 
    args = parser.parse_args()
    #args_dict = vars(args)

    output = {}


    sql = read_data("common","sql")
    nl = read_data("common","nl")

    common_prompts={}
    common_prompts["sql"] = sql
    common_prompts["nl"] = nl

    all_prompts = {"sql":{}, "nl":{}}
    for i in range(1,21):
        #print(i)
      
        data = read_data(i,"sql")
        #data["drop_database"][0] = data["drop_database"][0].replace("test","test1")
        #data["create_database"][0] = data["create_database"][0].replace("test","test1")
        #data["use_database"][0] = data["use_database"][0].replace("test","test1")

        all_prompts["sql"][i] = data

        

        
        data = read_data(i,"nl")
        #data["drop_database"][0] = data["drop_database"][0].replace("test","test1")
        #data["create_database"][0] = data["create_database"][0].replace("test","test1")
        #data["use_database"][0] = data["use_database"][0].replace("test","test1")
        all_prompts["nl"][i] = data




        #data = read_data(i,"nl")
        #all_prompts["nl"][i] = data
    


    scale = args.scale
    balance = args.balance
    overlap = min(args.overlap,1)

    model = args.model
    prompting = args.prompting
    encoding = args.encoding
    operation = args.operation

    generate_sample = args.generate_sample
    samples = []


    #current_model = model
    if model in ["gpt4","llama3.1-8B","mistral","gemma2","llama3.2","codellama","fine_tuned_llama3.1-8B"]:
        all_model = [model]
    else:
        #all_model = ["llama3.1-8B","mistral","gemma2","codellama","phi3"]
        all_model = ["fine_tuned_llama3.1-8B","llama3.1-8B","llama3.2","mistral","gemma2"]
    for current_model in all_model:

        if prompting in ["zero_shot","few_shot","zero_shot_cot"]:
            all_prompting = [prompting]
        else:
            all_prompting = ["few_shot","zero_shot_cot"]
        for current_prompting in all_prompting:
            if encoding in ["sql","nl"]:
                all_encoding = [encoding]
            else:
                all_encoding = ["sql","nl"]
            for current_encoding in all_encoding:
                if operation in ["select","update","delete","insert","no_filtering","single_filtering","double_filtering","triple_filtering","range_filtering","ranking","count","single_table","double_table","three_table"]:  
                    all_operation = [operation]
                else:
                    all_operation = ["update","delete","insert","no_filtering","single_filtering","double_filtering","triple_filtering","range_filtering","ranking","count","single_table","double_table","three_table"]
                for current_operation in all_operation:
                    if scale <0:
                        all_scale = [10,50,100,150,200,250,300,350,400]
                    else:
                        all_scale = [scale]
                    for current_scale in all_scale:
                        if balance <0:
                            all_balance = [0,0.2,0.4,0.6,0.8,1]
                        else:
                            all_balance = [balance]
                        for current_balance in all_balance:
                            if overlap <0:
                                all_overlap = [0,0.2,0.4,0.6,0.8,1]
                            else:
                                all_overlap = [overlap]
                            for current_overlap in all_overlap:
                                current_overlap = current_overlap/2

                                if not generate_sample:
                                    accuracy = run_experiment(common_prompts,all_prompts,current_encoding,current_scale, current_balance, current_overlap, current_model, current_prompting, current_operation)
                                    output[f"{current_model}_{current_prompting}_{current_encoding}_{current_operation}_{current_scale}_{current_balance}_{current_overlap*2}"] = accuracy

                                    if scale <0:
                                        with open(f"batch_output_scale_{current_model}.json", "w") as file:
                                            json.dump(output, file)
                                            file.flush()
                                    elif balance <0:
                                        with open(f"batch_output_balance_{current_model}.json", "w") as file:
                                            json.dump(output, file)
                                            file.flush()
                                    elif overlap <0:
                                        with open(f"batch_output_overlap_{current_model}.json", "w") as file:
                                            json.dump(output, file)
                                            file.flush()
                                        
                                    else:
                                        with open(f"output_{current_model}.json", "w") as file:
                                            json.dump(output, file)
                                            file.flush()
                                else:
                                    get_samples(common_prompts,all_prompts,current_encoding,current_scale, current_balance, current_overlap, current_model, current_prompting, current_operation,samples)
                                    print(f"{current_model}_{current_prompting}_{current_encoding}_{current_operation}_{current_scale}_{current_balance}_{current_overlap*2}")
                                    with open(f"samples.json", "w") as file:
                                        json.dump(samples, file)
                                        file.flush()


        




  
    
if __name__ == "__main__":
    
    connection = connect_to_server()
    main()
    connection.close()
   