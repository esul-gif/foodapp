'''
To do: Add columns for portion eaten, maybe calories, then work on the user input.

Work on api - django - start with simple ui

Maybe make it so that everytime a new user joins, it creates a new table and only that user has privileges to edit that table. Also must create some sort of permissions to make sure the number of users isnt abused because if i use heroku ill have limited bandwidth i think.

Also, if we turn it into a webapp then we need to make sure that we give access to the IP relevant to the user. Since i will be moving around, this might mean that we have to create a user relevant to whatrever ip im using when im in a different place? this could create too many users though. Maybe we can allow the ip address to change, as long as we can identify the user. 
'''

import mysql.connector
from datetime import datetime

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='foodapp',
    password='Foodie_121_',
    database='my_food_db'
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Create a table to store food data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS foods (
        id INT AUTO_INCREMENT PRIMARY KEY,
        food_name VARCHAR(255),
        protein VARCHAR(255),
        price_100grams VARCHAR(255),
        date DATE
    )
''')


# Function to insert food data into the table
def insert_food(food_name, protein, price_100grams, current_date):
    sql = 'INSERT INTO foods (food_name, protein, price_100grams, date) VALUES (%s, %s, %s, %s)'
    values = (food_name, protein, price_100grams, current_date)
    cursor.execute(sql, values)
    conn.commit()

# Example: Inserting food data
insert_food('Banana','1','20','2023-12-01')
insert_food('Salad','1','10','2023-12-02')

# Function to retrieve food data from the table
def get_foods():
    cursor.execute('SELECT * FROM foods')
    return cursor.fetchall()

# Example: Retrieving food data
foods = get_foods()
for food in foods:
    print(food)

# Close the cursor and connection when done
cursor.close()
conn.close()
