from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', "r") as it:
            data = json.load(it)
        items = data["items"] if data["items"] else []
    except:
        items = []
    
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    # First get the argument from the url link
    source = request.args.get('source')
    table_heads = []
    table_items = []
    error_message = None
    
    #check if it is json 

    if source ==  "json":
        try:
            with open('./products.json', "r") as prod_json:
                data = json.load(prod_json)
            table_heads = data[0].keys()
            table_items = data
        except FileNotFoundError:
            print("JSON file Not Found")
    #check if it is csv  
    elif source ==  'csv':
        try:
            data = []
            with open('./products.csv', 'r') as p_csv:
                data_csv = csv.DictReader(p_csv)
                for i in data_csv:
                    data.append(i)
            table_heads = data[0].keys()
            table_items = data
        except FileNotFoundError:
            print("CSV file Not Found")
            
    # Check if it is a SQL Database
    elif source ==  "sql":
        try:
            conn = sqlite3.connect('products.db')
            curr = conn.cursor()
            curr.execute('''SELECT * FROM Products''')
            rows = curr.fetchall()
            table_heads = [description[0] for description in curr.description]
            table_items = [dict(zip(table_heads, row)) for row in rows]
            
            #for i in rows:
            #    item = {}
            #    for key_id in range(len(table_heads)):
            #        item[table_heads[key_id]] = i[key_id]
            #    table_items.append(item)   
        
        except Exception :
            print("Connection is not established")
    # Handle invalid format
    else:
        return "Wrong source"

    
    
    try:
        id = request.args.get('id')
        sel_item = None
        for i in table_items:
            if int(i.get('id')) == int(id):
                sel_item = i
                break
        if not (sel_item is None):
            table_items = [sel_item]
        else:
            error_message = 'Product not found'
    except Exception:
        pass
        
    
    return render_template(
        'product_display.html',
        table_heads=list(table_heads)[1:] or [],
        table_items=table_items or [{}],
        error_message=error_message or None
    )

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()




if __name__ == '__main__':
    #create_database()
    app.run(debug=True, port=5000)
