from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def load_json(json_path):
    try:
        with open(json_path) as f:
            data = json.load(f)
            return data, None
    except Exception as e:
        return [], f"Error loading JSON: {e}"

def load_csv(csv_path):
    try:
        with open(csv_path, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader), None
    except Exception as e:
        return [], f"Error loading CSV: {e}"

def load_sql(sql_path):
    try:
        conn = sqlite3.connect(sql_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        products = [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]
        return products, None
    except Exception as e:
        return [], f"Error loading from database: {e}"

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products, error = load_json('products.json')
    elif source == 'csv':
        products, error = load_csv('products.csv')
    elif source == 'sql':
        products, error = load_sql('products.db')
    else:
        error = "Wrong source"

    if not error and id_filter:
        try:
            id_filter = int(id_filter)
            products = [p for p in products if int(p.get('id', -1)) == id_filter]
            if not products:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
