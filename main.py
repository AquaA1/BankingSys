
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DB_Pass")

# Connect to our PostgreSQL database
connection = psycopg.connect(
    host="localhost",
    dbname="banking_system",
    user="postgres",
    password=db_password
)

print("Connected to PostgreSQL!")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Fetch all customers from the database
cursor.execute("SELECT * FROM customers")

# Retrieve all rows returned by the query
customers = cursor.fetchall()

# Display the customers
for customer in customers:
    print(customer)

# Close the cursor and connection
cursor.close()
connection.close()
