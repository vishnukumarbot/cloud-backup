import mysql.connector
import json

def test_mysql_connection():
    # Load database configuration from the JSON file
    with open("db_config.json", "r") as file:
        db_config = json.load(file)
        print("host",db_config["database"])
         
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mypass",
            database="aws"
        )
        if conn.is_connected():
            print("Connection to MySQL database was successful!")

            # Created a cursor to execute queries
            cursor = conn.cursor()

            # Test query: Fetch data from a table
            query = "SELECT * FROM student;"
            cursor.execute(query)
            results = cursor.fetchall()

            # Print the results
            print("\nData from 'test':")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        print("\nMySQL connection is closed.")

if __name__ == "__main__":
    test_mysql_connection()
