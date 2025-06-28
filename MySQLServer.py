#!/usr/bin/env python3
"""
Python script to create the alx_book_store database in MySQL server.
This script handles database creation with proper error handling and connection management.
"""

import mysql.connector


def create_database():
    """
    Creates the alx_book_store database in MySQL server.
    Handles connection, creation, and cleanup with appropriate error messages.
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password=''   # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database with IF NOT EXISTS to avoid errors if it already exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()