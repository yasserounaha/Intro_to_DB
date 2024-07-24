import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def main():
    try:
        # Establish connection to MySQL server
        cnx = mysql.connector.connect(user='yasser', password='yasser', host='127.0.0.1')
        cursor = cnx.cursor()
        
        # Create database
        create_database(cursor)
        print("Database 'alx_book_store' created successfully!")
        
        # Close cursor and connection
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    main()

