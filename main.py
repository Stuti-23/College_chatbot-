import mysql.connector
import pymysql
import pandas as pd
config = {
    'user': 'root',
    'password': 'Stuti18#',
    'host': 'localhost',
    'database': 'chatbot'
}

try:
    # Establish the connection

    conn = mysql.connector.connect(**config)
    if conn:
        print('Successfully connected to the database')

    # Create a cursor object

    query = "SELECT * FROM chatbotqa"
    df = pd.read_sql(query, conn)

    # Close the connection
    conn.close()

    # Display the DataFrame
    print(df)

except pymysql.MySQLError as err:
    print(f"Error: {err}")