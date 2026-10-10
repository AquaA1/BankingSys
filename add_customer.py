import psycopg
import os
from dotenv import load_dotenv
from datetime import date
from decimal import Decimal

load_dotenv()

dbPass = os.getenv("DB_Pass")

def add_customer():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    dob = date.fromisoformat(input("Enter your date of birth in (YYYY-MM-DD) format: "))
    amount = Decimal(input("Enter your amount: "))

    if not name:
        raise ValueError("Not a valid name")

    if age<0:
        raise ValueError("Age cannot be negative")

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    connection = psycopg.connect(
        host="localhost",
        dbname="banking_system",
        user = "postgres",
        password = dbPass
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        insert into customers (name , age , dob , amount)
        values (%s , %s , %s ,%s)
        returning id
        """,
        (name , age , dob , amount)
    )

    customer_id = cursor.fetchone()[0]

    print("Sucessfully created the customer")
    print("Customer id = ",customer_id)
    print("Customer name = ",name)

    connection.commit()

if __name__ == "__main__":
    add_customer()


