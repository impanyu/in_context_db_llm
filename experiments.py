import argparse
import mysql.connector
from mysql.connector import Error
import json
import random


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchall()  # Fetch all the rows from the result
        return result
    except Error as e:
        print(f"Error: '{e}'")
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



def main():
    # Read cmd line arguments with argparse
    parser = argparse.ArgumentParser(description='Run experiments')
    parser.add_argument('--model', type=str, default='gpt4', help='Model to evaluate')
    parser.add_argument('--prompting', type=str, default='zero_shot', help='Prompting strategy')
    parser.add_argument('--dataset', type=str, default='world', help='Dataset to evaluate')
    parser.add_argument('--encoding', type=str, default='sql', help='Encoding method for data and query')

    parser.add_argument('--operation', type=str, default='select', help='Dataset query operation')

    parser.add_argument('--scale', type=int, default='300', help='Number of operations in the dataset')
    parser.add_argument('--balance', type=float, default=0.5, help='Ratio of insert in the operations in the dataset, a number between 0 and 1')
    parser.add_argument('--overlap', type=float, default=0.5, help='Ratio of overlap between the operations in the dataset, a number between 0 and 0.5')
    args = parser.parse_args()
    args_dict = vars(args)


    scale = args.scale
    balance = args.balance
    overlap = min(args.overlap,0.5)

    

    # generate db populating query and db query
    with open(f"world_sql.json", "r") as file:
        data = json.load(file)
        drop_db_query = data["drop_database"]
        create_db_query = data["create_database"]
        use_db_query = data["use_database"]
        create_table_query = data["create_table"]

        db_populating_query = ""
      

        db_query_categories = list(data["select_data"].keys())

        category_index = random.randint(0, len(db_query_categories)-1)
        category = db_query_categories[category_index]
        db_queries = data["select_data"][category]

        random_index = random.randint(0, len(db_queries)-1)
        db_query = db_queries[random_index]


        must_insert = data["must_insert_data"]

        for q in must_insert:
            db_populating_query += q + "\n" 

        scale -= len(must_insert)
        insert_scale = int(scale * balance)
        delete_update_scale = int(scale * (1 - balance))

  
        radius = int(overlap * insert_scale)
   

        tmp_db_insert_populating_queries = []
        tmp_db_delete_update_populating_queries = {}
        # populate the tmp_db_delete_update_populating_queries with 0 to insert_scale keys with the value of []
        for i in range(insert_scale+1):
            tmp_db_delete_update_populating_queries[i] = []



        for i in range(insert_scale):
            # get a ramdom number between 0 and len(data["insert"])
            random_index = random.randint(0, len(data["insert"])-1)
            tmp_db_insert_populating_queries.append(data["insert"][random_index])

        for i in range(delete_update_scale):
            # get a ramdom number between 0 and 1
            random_number = random.random()
            if random_number <= 0.5: # insert a delete query
                # get a ramdom number between 0 and 1
                random_index_in_populating_queries = random.randint(insert_scale-radius*2,insert_scale)
                random_index = random.randint(0, len(data["delete_update"])-1)
                tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(data["delete_update"][random_index])
            else: # insert an update query
                ramdom_index_in_populating_queries= random.randint(insert_scale-radius*2,insert_scale)
                random_index = random.randint(0, len(data["delete_update"])-1)
                tmp_db_delete_update_populating_queries[random_index_in_populating_queries].append(data["update_update"][random_index])

        for i in range(insert_scale+1):
            for j in range(len(tmp_db_delete_update_populating_queries[i])):
                db_populating_query += tmp_db_delete_update_populating_queries[i][j] + "\n"
            if i < insert_scale:
                db_populating_query += tmp_db_insert_populating_queries[i] + "\n"




    # execute the db_populating_query and db_query
    connection = connect_to_server()
    if connection is not None:
        execute_query(connection, drop_db_query)
        execute_query(connection, create_db_query)
        execute_query(connection, use_db_query)
        execute_query(connection, create_table_query)
        execute_query(connection, db_populating_query)
        result = execute_query(connection, db_query)

        
        connection.close()
        print("Connection closed")

    # generate populating query and query for selected model

    




    
if __name__ == "__main__":
    main()