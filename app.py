from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def obtener_productos():
    conn = sqlite3.connect("mercadolibre.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, link FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

@app.route("/")
def index():
    productos = obtener_productos()
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    app.run(debug=True)
