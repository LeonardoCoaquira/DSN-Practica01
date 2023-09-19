from flask import Flask, jsonify, request, render_template, redirect, url_for
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_config = {
    'host': 'db1',
    'user': 'root',
    'password': 'root',
    'database': 'practica01'
}

def get_data_from_database():
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre FROM usuarios")
        data = cursor.fetchall()
        return data

@app.route('/', methods=['GET'])
def index():
    data = get_data_from_database()
    return render_template('index.html', data=data)

@app.route('/data/<int:id>/update', methods=['GET'])
def update_form(id):
    item = get_data_from_database()  # Cambia esto para obtener los datos de la base de datos
    item_to_update = None

    for data_item in item:
        if data_item['id'] == id:
            item_to_update = data_item
            break

    if item_to_update:
        return render_template('update.html', item=item_to_update)
    else:
        return "Dato no encontrado", 404

@app.route('/data/<int:id>/update', methods=['POST'])
def update(id):
    data = request.form
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (data['nombre'], id))
        connection.commit()
    return redirect(url_for('index'))


@app.route('/data/<int:id>/delete', methods=['POST'])
def delete(id):
    item = get_data_from_database()  # Cambia esto para obtener los datos de la base de datos
    item_to_delete = None

    for data_item in item:
        if data_item['id'] == id:
            item_to_delete = data_item
            break

    if item_to_delete:
        with mysql.connector.connect(**db_config) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            connection.commit()
        return redirect(url_for('index'))
    else:
        return "Dato no encontrado", 404


@app.route('/data/create', methods=['GET'])
def create_form():
    return render_template('create.html')

@app.route('/data/create', methods=['POST'])
def create_data():
    new_name = request.form['nombre']
    with mysql.connector.connect(**db_config) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (new_name,))
        connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
