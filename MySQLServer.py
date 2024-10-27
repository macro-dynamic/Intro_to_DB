import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server (update with your MySQL username and password)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
        
        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Run the function to create the database
create_database()
