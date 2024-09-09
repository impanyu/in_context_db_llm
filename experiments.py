import argparse
import mysql.connector
from mysql.connector import Error
import json
import random
from dotenv import load_dotenv
from openai import OpenAI
import os


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
            return result
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

def read_data(dataset,encoding,scale, balance, overlap, operation):
    # generate db populating query and db query
    with open(f"{dataset}_{encoding}.json", "r") as file:
        data = json.load(file)
        drop_db_query = data["drop_database"]
        create_db_query = data["create_database"]
        use_db_query = data["use_database"]
        create_table_query = data["create_table"]

        db_populating_query = ""

        if operation == "insert_data" or operation == "delete_data" or operation == "update_data":
            random_index = random.randint(0, len(data[operation])-1)
            db_query = data[operation][random_index]

        elif operation == "select_data":


            db_query_categories = list(data["select_data"].keys())

            category_index = random.randint(0, len(db_query_categories)-1)
            category = db_query_categories[category_index]
            db_queries = data["select_data"][category]

            random_index = random.randint(0, len(db_queries)-1)
            db_query = db_queries[random_index]
        else:
            category = operation

            db_queries = data["select_data"][category]

            random_index = random.randint(0, len(db_queries)-1)
            db_query = db_queries[random_index]



        must_insert = data["must_insert_data"]
        
        tmp_db_insert_populating_queries = []
        tmp_db_delete_update_populating_queries = {}

        for q in must_insert:
            #db_populating_query += q + "\n"
            tmp_db_insert_populating_queries.append(q)
        print(len(tmp_db_insert_populating_queries))

        
        insert_scale = int(scale * balance)
        remaining_insert_scale = max(0,insert_scale - len(must_insert))
        delete_update_scale = int(scale * (1 - balance))

  
        radius = int(overlap * insert_scale)
   

        
        # populate the tmp_db_delete_update_populating_queries with 0 to insert_scale keys with the value of []
        for i in range(insert_scale+1):
            tmp_db_delete_update_populating_queries[i] = []



        for i in range(remaining_insert_scale):
            # get a random number between 0 and len(data["insert"])
            random_index = random.randint(0, len(data["insert_data"])-1)
            tmp_db_insert_populating_queries.append(data["insert_data"][random_index])

        for i in range(delete_update_scale):
            # get a random number between 0 and 1
            random_number = random.random()
            if random_number <= 0.5: # insert a delete query
                # get a random number between 0 and 1
                random_index_in_populating_queries = random.randint(insert_scale-radius*2,insert_scale)
                random_index = random.randint(0, len(data["delete_data"])-1)
                tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(data["delete_data"][random_index])
            else: # insert an update query
                random_index_in_populating_queries= random.randint(insert_scale-radius*2,insert_scale)
                random_index = random.randint(0, len(data["delete_data"])-1)
                tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(data["update_data"][random_index])

        for i in range(insert_scale+1):
            for j in range(len(tmp_db_delete_update_populating_queries[i])):
                db_populating_query += tmp_db_delete_update_populating_queries[i][j] + "\n"
            if i < insert_scale:
                db_populating_query += tmp_db_insert_populating_queries[i] + "\n"
    return db_populating_query, db_query, data

def concatenate_prompt(prompts):
    prompt = ""
    for p in prompts:
        prompt += p + "\n"
    return prompt

def main():
    # Read cmd line arguments with argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--model', type=str, default='gpt4', help='Model to evaluate')
    parser.add_argument('--prompting', type=str, default='zero_shot', help='Prompting strategy')
    parser.add_argument('--dataset', type=str, default='world', help='Dataset to evaluate')
    parser.add_argument('--encoding', type=str, default='sql', help='Encoding method for data and query')

    parser.add_argument('--operation', type=str, default='select_data', help='Dataset query operation')

    parser.add_argument('--scale', type=int, default='50', help='Number of operations in the dataset')
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

    TIMES = 3

    accuracy = 0

    # repeat the experiment TIMES times
    for t in range(TIMES):

        # generate populating query and query 
        db_populating_query,user_query,data = read_data(dataset,"sql",scale, balance, overlap, operation)

        #user_query = "INSERT INTO `city` VALUES (69,'Buenos Aires','AAA','Distrito Federal',2982146);"


        drop_db_query = data["drop_database"][0]
        create_db_query = data["create_database"][0]
        use_db_query = data["use_database"][0]
        create_table_query = data["create_table"]

        print(user_query)

        db_populating_queries = db_populating_query.split("\n")[:-1]
        print(len(db_populating_queries))


        # execute the db_populating_query and db_query
        connection = connect_to_server()
        if connection is not None:
            print("drop db")
            execute_query(connection, drop_db_query)
            print("create db")
            execute_query(connection, create_db_query)
            print("use db")
            execute_query(connection, use_db_query)
            print("create tables")
            for query in create_table_query:
                execute_query(connection, query)
            print("populating db")
            for query in db_populating_queries:
                execute_query(connection, query)
            print("executing query")
            true_result = execute_query(connection, user_query)

            
            connection.close()
            print("Connection closed")

        

        drop_db_query = data["drop_database"]
        create_db_query = data["create_database"]
        use_db_query = data["use_database"]
        create_table_query = data["create_table"]

        system_prompt_1 = data["system_prompt_1"]
        system_prompt_2 = data["system_prompt_2"]
        system_prompt_3 = data["system_prompt_3"]

        user_prompt_1= data["user_prompt_1"]
        zero_shot = data["zero_shot"]
        zero_shot_COT = data["zero_shot_COT"]
        few_shot_example = data["few_shot_example"]
        few_shot = data["few_shot"]
        few_shot_COT = data["few_shot_COT"]

        prompt = concatenate_prompt(system_prompt_1)+concatenate_prompt(system_prompt_2)
        if prompting == "zero_shot":
            prompt += concatenate_prompt(zero_shot)
        elif prompting == "zero_shot_COT":
            prompt += concatenate_prompt(zero_shot_COT)
        elif prompting == "few_shot":
            prompt += concatenate_prompt(few_shot_example)+concatenate_prompt(few_shot)
        elif prompting == "few_shot_COT":
            prompt += concatenate_prompt(few_shot_example)+concatenate_prompt(few_shot_COT)

        prompt += concatenate_prompt(system_prompt_3)
        prompt += db_populating_query

        user_prompt = concatenate_prompt(user_prompt_1)
        user_prompt += user_query

        print(user_prompt)

        if model == "gpt4":
            # Load environment variables from the .env file
            load_dotenv()

            # Fetch the API key from the environment variable
            api_key = os.getenv("OPENAI_API_KEY")

            # Initialize the OpenAI client with the API key
            client = OpenAI(api_key=api_key)

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_prompt},

                ]
            )

            # get the response
            result = response.choices[0].message.content

        if "Fail" in true_result:
            if "Fail" in result:
                accuracy += 1
        elif "Succeed" in true_result:
            if "Succeed" in result:
                accuracy += 1
        else:
            overlap = set(true_result).intersection(set(result))
            union = set(true_result).union(set(result))
            accuracy += len(overlap) / len(union)
            

        print(true_result)
        print(result)

        print(f"Accuracy: {accuracy}")

    accuracy = accuracy / TIMES
    print(f"Total Accuracy: {accuracy}")
      
        


  

    




    
if __name__ == "__main__":
    main()