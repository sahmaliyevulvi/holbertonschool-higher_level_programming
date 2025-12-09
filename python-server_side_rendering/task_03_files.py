from flask import Flask, render_template, request
import json
import csv

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
            items = data.get("items", [])
    except:
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    table_heads = []
    table_items = []
    error_message = None

    if source == "json":
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
                table_heads = data[0].keys()
                table_items = data
        except:
            return "Error loading JSON file"

    elif source == "csv":
        try:
            data = []
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)
                table_heads = data[0].keys() if data else []
                table_items = data
        except:
            return "Error loading CSV file"

    else:
        return "Wrong source"

    try:
        prod_id = request.args.get('id')
        if prod_id:
            selected = None
            for item in table_items:
                if int(item.get('id')) == int(prod_id):
                    selected = item
                    break
            if selected:
                table_items = [selected]
            else:
                error_message = "Product not found"
    except:
        pass

    return render_template(
        'product_display.html',
        table_heads=list(table_heads)[1:] if table_heads else [],
        table_items=table_items,
        error_message=error_message
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
