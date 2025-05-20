from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

def inicializar_bd():
    if not os.path.exists("mercadolibre.db"):
        os.system("python Request_data.py")
    else:
        conn = sqlite3.connect("mercadolibre.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT 1 FROM productos LIMIT 1")
        except sqlite3.OperationalError:
            conn.close()
            os.system("python Request_data.py")
        else:
            conn.close()

def obtener_productos():
    conn = sqlite3.connect("mercadolibre.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, precio, link FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

@app.route("/")
def index():
    inicializar_bd()
    productos = obtener_productos()
    return render_template("index.html", productos=productos)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
