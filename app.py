from flask import Flask, jsonify, request
import db_eventos
import sqlite3

app = Flask(__name__)

eventos = db_eventos.get_eventos()

@app.route("/eventos/<int:id>", methods = ["DELETE"])
def del_evento(id):
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute("DELETE FROM eventos WHERE id = ?", (id,))
        if c.rowcount == 0:
            return jsonify({"message": "Evento no encontrado"}), 404
        conn.commit()
        return jsonify({"message": "Evento eliminado exitosamente"}), 200
    except sqlite3.Error:
        return jsonify({"message": "Error al eliminar el evento"}), 500
    finally:
        conn.close()

@app.route("/eventos/<int:id>", methods = ["PUT"])
def update_evento(id):
    body = request.get_json()
    nombre = body.get("nombre")
    hora = body.get("hora")
    duracion = body.get("duracion")
    ubicacion = body.get("ubicacion")
    descripcion = body.get("descripcion")
    tipo_evento = body.get("tipo_evento")
    idioma = body.get("idioma")
    if not (nombre and hora and duracion and ubicacion and tipo_evento and idioma):
        return jsonify({"message": "Todos los atributos deben ser proporcionados"}), 400
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute("UPDATE eventos SET nombre = ?, hora = ?, duracion = ?, ubicacion = ?, descripcion = ?, tipo_evento = ?, idioma = ? WHERE id = ?", (nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma, id))
        if c.rowcount == 0:
            return jsonify({"message": "Evento no encontrado"}), 404
        conn.commit()
        return jsonify({"message": f"Evento '{nombre}' actualizado exitosamente"}), 200
    except sqlite3.Error:
        return jsonify({"message": f"Error al actualizar el evento {nombre}"}), 500
    finally:
        conn.close()

@app.route("/eventos", methods = ["POST"])
def add_evento():
    body = request.get_json()
    nombre = body.get("nombre")
    hora = body.get("hora")
    duracion = body.get("duracion")
    ubicacion = body.get("ubicacion")
    descripcion = body.get("descripcion")
    tipo_evento = body.get("tipo_evento")
    idioma = body.get("idioma")
    if not (nombre and hora and duracion and ubicacion and tipo_evento and idioma):
        return jsonify({"message": "Todos los atributos son necesarios son necesarios"}), 400
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute('INSERT INTO eventos (nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma) VALUES (?, ?, ?, ?, ?, ?, ?)', (nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma))
        conn.commit()
        return jsonify ({"message": "Evento creado exitosamente"}), 200
    except:
        return jsonify({"message": "Error al añadir el evento"}), 500
    finally:
        conn.close()

@app.route("/eventos/hora/<hora>", methods=["GET"])
def get_eventos_por_hora(hora):
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute("SELECT * FROM eventos WHERE hora = ?", (hora,))
        resultado = c.fetchall()
        if resultado:
            for i in resultado:
                eventos_dicts = {
                        "id": i[0],
                        "nombre": i[1],
                        "hora": i[2],
                        "duracion": i[3],
                        "ubicacion": i[4],
                        "descripcion": i[5],
                        "tipo_evento": i[6],
                        "idioma": i[7]
                    }
            return jsonify(eventos_dicts), 200
        else:
            return jsonify({"message": "Evento no encontrado"}), 404
    except sqlite3.Error:
        return jsonify({"message": "Error al obtener eventos por hora"}), 500
    finally:
        conn.close()

@app.route("/eventos/<int:id>", methods = ['GET'])
def get_evento(id):
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute("SELECT * FROM eventos WHERE id = ?", (id,))
        resultado = c.fetchone()
        if resultado:
            evento_dict =  {
                    "id": resultado[0],
                    "nombre": resultado[1],
                    "hora": resultado[2],
                    "duracion": resultado[3],
                    "ubicacion": resultado[4],
                    "descripcion": resultado[5],
                    "tipo_evento": resultado[6],
                    "idioma": resultado[7]
                }
            return jsonify(evento_dict), 200
        else:
            return jsonify({"message": "Evento no encontrado"}), 404
    except sqlite3.Error:
        return jsonify({"message": "Error al obtener el evento"}), 500
    finally:
        conn.close()

@app.route('/eventos', methods = ['GET'])
def get_eventos():
    eventos_clean = []
    for e in eventos:
        eventos_clean.append ({"id": e[0], "nombre": e[1], "hora": e[2], "duracion": e[3], "ubicacion": e[4], "descripcion": e[5], "tipo_evento": e[6], "idioma": e[7]})
    return jsonify(eventos_clean), 200

@app.route("/")
def home():
    return "Te conectaste a la API de Eventos V 1.0"

if __name__ == "__main__":
    app.run(debug=True)