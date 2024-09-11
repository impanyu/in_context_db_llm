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



def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all the rows from the result
        connection.commit()
        # change all the letter in query to lower case
        query = query.lower()

        if "insert" in query or "delete" in query or "update" in query:
            return "Succeed"
        else:
            return json.dumps([r[0] for r in result])
    except Error as e:
        print(f"Error: '{e}'")
        print(query)
        connection.rollback()

        return "Fail"
    finally:
        cursor.close()



def connect_to_server():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1q2w3e4r5t'
        )
        if connection.is_connected():
            print("Connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def concatenate_prompt(prompts):
    prompt = ""
    for p in prompts:
        prompt += p + "\n"
    return prompt

def read_data(dataset,encoding):
    data = {}
    if os.path.exists(f"{dataset}_{encoding}.json"):
        with open(f"{dataset}_{encoding}.json", "r") as file:
            data = json.load(file)
    return data

def generate_system_prompt(datasets,encoding,prompting):
    data = datasets[encoding]
    db_data = datasets["sql"]

    drop_db_query = data["drop_database"][0]
    create_db_query = data["create_database"][0]
    use_db_query = data["use_database"][0]
    create_table_query = data["create_table"]

    db_drop_db_query = db_data["drop_database"][0]
    db_create_db_query = db_data["create_database"][0]
    db_use_db_query = db_data["use_database"][0]
    db_create_table_query = db_data["create_table"]

    system_prompt_1 = data["system_prompt_1"]
    system_prompt_2 = data["system_prompt_2"]





    cot = data["COT"]

    prompt = concatenate_prompt(system_prompt_1)+concatenate_prompt(system_prompt_2)
    prompt += concatenate_prompt(drop_db_query)+concatenate_prompt(create_db_query)+concatenate_prompt(use_db_query)+concatenate_prompt(create_table_query)

 

    if "COT" in prompting:
        prompt += concatenate_prompt(cot)



    connection = connect_to_server()
    if connection is not None:
        print("drop db")
        execute_query(connection, db_drop_db_query)
        print("create db")
        execute_query(connection, db_create_db_query)
        print("use db")
        execute_query(connection, db_use_db_query)
        print("create tables")
        for query in db_create_table_query:
            execute_query(connection, query)


        
        connection.close()
        print("Connection closed")


    return prompt



def generate_query_result_pair(datasets,encoding,scale, balance, overlap, operation):
    db_data = datasets["sql"]
    data = datasets[encoding]

    db_populating_query = ""
    populating_query = ""

    db_query = ""
    query = ""

    tmp_db_insert_populating_queries = []
    tmp_db_delete_update_populating_queries = {}

    tmp_insert_populating_queries = []
    tmp_delete_update_populating_queries = {}

    
    insert_scale = int(scale * balance)
    delete_update_scale = int(scale * (1 - balance))


    radius = int(overlap * insert_scale)


    
    # generate the populating query
    for i in range(insert_scale+1):
        tmp_db_delete_update_populating_queries[i] = []
        tmp_delete_update_populating_queries[i] = []


    for i in range(insert_scale):
        # get a random number between 0 and len(data["insert"])
        random_index = random.randint(0, len(db_data["insert_data"])-1)
        tmp_db_insert_populating_queries.append(db_data["insert_data"][random_index])
        tmp_insert_populating_queries.append(data["insert_data"][random_index])

    for i in range(delete_update_scale):
        # get a random number between 0 and 1
        random_number = random.random()
        if random_number <= 0.5: # insert a delete query
            # get a random number between 0 and 1
            random_index_in_populating_queries = random.randint(insert_scale-radius*2,insert_scale)
            random_index = random.randint(0, len(db_data["delete_data"])-1)
            tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(db_data["delete_data"][random_index])
            tmp_delete_update_populating_queries[random_index_in_populating_queries].append(data["delete_data"][random_index])
        else: # insert an update query
            random_index_in_populating_queries= random.randint(insert_scale-radius*2,insert_scale)
            random_index = random.randint(0, len(db_data["delete_data"])-1)
            tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(db_data["update_data"][random_index])
            tmp_delete_update_populating_queries[random_index_in_populating_queries].append(data["update_data"][random_index])

    for i in range(insert_scale+1):
        for j in range(len(tmp_db_delete_update_populating_queries[i])):
            db_populating_query += tmp_db_delete_update_populating_queries[i][j] + "\n"
            populating_query += tmp_delete_update_populating_queries[i][j] + "\n"
        if i < insert_scale:
            db_populating_query += tmp_db_insert_populating_queries[i] + "\n"
            populating_query += tmp_insert_populating_queries[i] + "\n"


    # generate the query
    if operation == "insert_data" or operation == "delete_data" or operation == "update_data":
        random_index = random.randint(0, len(data[operation])-1)
        db_query = db_data[operation][random_index]
        query = data[operation][random_index]

    elif operation == "select_data":

        db_query_categories = list(data["select_data"].keys())

        category_index = random.randint(0, len(db_query_categories)-1)
        category = db_query_categories[category_index]

        db_queries = db_data["select_data"][category]
        queries = data["select_data"][category]

        random_index = random.randint(0, len(db_queries)-1)

        db_query = db_queries[random_index]
        query = queries[random_index]
    else:
        category = operation

        db_queries = db_data["select_data"][category]
        queries = data["select_data"][category]

        random_index = random.randint(0, len(db_queries)-1)
        db_query = db_queries[random_index]
        query = queries[random_index]

    
    db_populating_queries = db_populating_query.split("\n")[:-1]

    # execute the db_populating_query and db_query
    connection = connect_to_server()
    if connection is not None:
        db_use_db_query = db_data["use_database"][0]
        execute_query(connection, db_use_db_query)

        print("clear tables")
        for query in db_data["clear_tables"]:
            execute_query(connection, query)
        print("populating db")
        for query in db_populating_queries:
            execute_query(connection, query)
        print("executing query")
        true_result = execute_query(connection, db_query)

        
        connection.close()
        print("Connection closed")

    user_prompt_1 = datasets[encoding]["user_prompt_1"]
    user_prompt_2 = datasets[encoding]["user_prompt_2"]

    user_prompt = concatenate_prompt(user_prompt_1)
    user_prompt += populating_query

    user_prompt += concatenate_prompt(user_prompt_2)
    user_prompt += query

        
    return user_prompt, true_result



def main():
    # Read cmd line arguments with argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--model', type=str, default='gpt4', help='Model to evaluate')
    parser.add_argument('--prompting', type=str, default='zero_shot', help='Prompting strategy')
    parser.add_argument('--dataset', type=str, default='world', help='Dataset to evaluate')
    parser.add_argument('--encoding', type=str, default='sql', help='Encoding method for data and query')

    parser.add_argument('--operation', type=str, default='select_data', help='Dataset query operation')

    parser.add_argument('--scale', type=int, default='100', help='Number of operations in the dataset')
    parser.add_argument('--balance', type=float, default=0.5, help='Ratio of insert in the operations in the dataset, a number between 0 and 1')
    parser.add_argument('--overlap', type=float, default=0.5, help='Ratio of overlap between the operations in the dataset, a number between 0 and 0.5')
    args = parser.parse_args()
    #args_dict = vars(args)


    scale = args.scale
    balance = args.balance
    overlap = min(args.overlap,0.5)
    dataset = args.dataset
    model = args.model
    prompting = args.prompting
    encoding = args.encoding
    operation = args.operation

    TIMES = 80

    accuracy = 0

    datasets = {}

    datasets["sql"] = read_data(dataset,"sql")
    datasets[encoding] = read_data(dataset,encoding)
    few_shot_number = 3
    example_scale = 20

    # repeat the experiment TIMES times
    for t in range(TIMES):
        


    
        prompt = generate_system_prompt(datasets,encoding,prompting)
        

        query_result_pairs = []

        if "few_shot" in prompting:
            for p in range(few_shot_number):
                user_prompt, true_result = generate_query_result_pair(datasets,encoding, example_scale, balance, overlap, operation)
                query_result_pairs.append((user_prompt, true_result))
        
        user_prompt, true_result = generate_query_result_pair(datasets,encoding, scale, balance, overlap, operation)
                


        if model == "gpt4":
            # Load environment variables from the .env file
            load_dotenv()

            # Fetch the API key from the environment variable
            api_key = os.getenv("OPENAI_API_KEY")

            # Initialize the OpenAI client with the API key
            client = OpenAI(api_key=api_key)

            messages = [{"role": "system", "content": prompt}]
            for pair in query_result_pairs:
                messages.append({"role": "user", "content": pair[0]})
                messages.append({"role": "assistant", "content": pair[1]})
            
            messages.append({"role": "user", "content": user_prompt})

            print("start api call")
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages= messages,
                    temperature=0.5,  # Set the temperature here (adjust as needed)
                    timeout=5  # Set a timeout of 10 seconds
                )
            except APITimeoutError:
                t = t-1
                time.sleep(1)
                continue
            print("end api call")

            # get the response
            result = response.choices[0].message.content

        if "Fail" in true_result:
            if "Fail" in result:
                accuracy += 1
        elif "Succeed" in true_result:
            if "Succeed" in result:
                accuracy += 1
        else:
            true_result = json.loads(true_result)
            # replace ' with " in the result"
            result = result.replace("'", "\"")
           
            try:

                result = json.loads(result)
                if not type(result) == list:
                    print(true_result)
                    print(result)

                    print(f"Accuracy: {accuracy}")
                    continue
                
                if len(result) > 0:
                    if type(result[0]) == list or type(result[0]) == tuple:
                        result = [r[0] for r in result]
                    elif not type(result[0]) == int and not type(result[0]) == float:
                        print(true_result)
                        print(result)

                        print(f"Accuracy: {accuracy}")
                        continue

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
                    accuracy += 1 * order_accuracy  
                else:
                    accuracy += len(result_overlap) / len(result_union) * order_accuracy
                



                #print(f"result_overlap: {result_overlap}")
                #print(f"result_union: {result_union}")
            except json.JSONDecodeError as e:
                pass
            except Exception as e:
                pass
                

        print(true_result)
        print(result)

        print(f"Accuracy: {accuracy}")
        

    accuracy = accuracy / TIMES
    print(f"Total Accuracy: {accuracy}")
      
        


  

    




    
if __name__ == "__main__":
    main()