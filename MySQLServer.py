import mysql.connector

def connect_and_create_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Kapule@1"
        )
        
        cursor = mydb.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error:
        print("Error while connecting to MySQL")
    
    finally:
        if 'mydb' in locals() and mydb.is_connected():
            cursor.close()
            mydb.close()

if __name__ == "__main__":
    connect_and_create_db()
    