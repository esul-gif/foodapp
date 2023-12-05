
'''
TO DO:

- Make empty strings null?
- Better GUI
- 
'''
from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)


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
        portion VARCHAR(255),
        protein INT,
        carbs INT,
        fat INT,
        price_100grams INT,
        date DATE
    )
''')


# Function to insert food data into the table
def insert_food(food_name,portion,protein,carbs,fat,price_100grams,current_date):
    sql = 'INSERT INTO foods (food_name,portion,protein,carbs,fat,price_100grams,date) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    values = (food_name,portion,protein,carbs,fat,price_100grams,current_date)
    cursor.execute(sql,values)
    conn.commit()




@app.route("/", methods=['GET', 'POST'])

def add_food():
    sum_protein = 0  # Default value
    if request.method == 'POST':
        food_name = request.form['food_name']
        portion = request.form['portion']
        protein = request.form['protein']
        carbs = request.form['carbs']
        fat = request.form['fat']
        price_100grams = request.form['price_100grams']
        current_date = datetime.now().date()
        insert_food(food_name, portion, protein, carbs, fat, price_100grams, current_date)


        # Fetch the sum of protein columns from the database for the current day
        cursor.execute('SELECT SUM(protein) FROM foods WHERE date = %s', (current_date,))
        
        sum_protein = 0  # Default value if no rows are found
        row = cursor.fetchone()
        if row is not None:
            sum_protein = row[0]  # Get the sum value
    return render_template('add_food.html', sum_protein=sum_protein)



if __name__ == '__main__':
    app.run(debug=True)