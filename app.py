from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('productos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página para agregar producto
@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':  # Si es una solicitud POST (cuando se envían los datos)
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']

        # Conectar a la base de datos y agregar el producto
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conn.commit()
        conn.close()

        # Redirigir al menú de inicio después de agregar el producto
        return redirect(url_for('index'))

    return render_template('agregar_producto.html')

# Ver inventario
@app.route('/ver_inventario')
def ver_inventario():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template('ver_inventario.html', productos=productos)

# Eliminar producto
@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('ver_inventario'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
