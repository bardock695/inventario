import sqlite3

# Conectar a la base de datos (la creará si no existe)
conn = sqlite3.connect('productos.db')

# Crear el cursor
cursor = conn.cursor()

# Crear la tabla 'productos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL
)
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla creadas con éxito.")
