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
        with open('items.json', 'r') as f:
            data = json.load(f)
            itemList = data.get('items', [])
    except Exception as e:
        itemList = []
        print(f"Error reading items.json: {e}")
    return render_template('items.html', items=itemList)

def read_from_json(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return []

def read_from_csv(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products=[]
    error = None

    if source == "json":
        products = read_from_json("products.json")
    elif source == "csv":
        products = read_from_csv("products.csv")
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)
    
    if product_id:
        if product_id.isdigit():
            product_id = int(product_id)
            products = [p for p in products if product_id == int(p['id']) ]
            if not products:
                error= "Product not found"
        else:
            error= "Invalid ID"
            products = []
    return render_template('product_displat.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
