import sqlite3

def crear_tabla():
    conn = sqlite3.connect('eventos.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS eventos')
    c.execute('''
              CREATE TABLE eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    hora TEXT NOT NULL,
    duracion TEXT NOT NULL,
    ubicacion TEXT NOT NULL,
    descripcion TEXT,
    tipo_evento TEXT NOT NULL,
    idioma TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

def get_eventos():
    conn = sqlite3.connect('eventos.db')
    c = conn.cursor()
    c.execute('SELECT * FROM eventos')
    eventos = c.fetchall()
    conn.close()
    return eventos

def add_evento (id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma):
    try:
        conn = sqlite3.connect('eventos.db')
        c = conn.cursor()
        c.execute('INSERT INTO eventos (id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Error: El evento {nombre} ya existe")
    except:
        print("Error al añadir el evento")
    conn.close()

if __name__ == "__main__":
    crear_tabla()
    add_evento('001','Reunion de equipo', '10:00', '2 horas', 'Argentina', 'Reunion para definir objetivos', 'Virtual', 'Espaniol')
    add_evento('002', 'Conferencia de Innovacion', '14:00', '3 horas', 'Espania', 'Presentacion sobre las ultimas tendencias en tecnologia e innovacion', 'Presencial', 'Espaniol')
    add_evento('003', 'Seminario de Marketing Digital', '09:00', '4 horas', 'Mexico', 'Taller intensivo sobre estrategias de marketing en redes sociales', 'Virtual', 'Espaniol')
    add_evento('004', 'Webinar de Finanzas Personales', '17:00', '1.5 horas', 'Colombia', 'Sesion en linea para aprender sobre gestion de finanzas personales', 'Virtual', 'Espaniol')
    add_evento('005', 'Taller de Desarrollo Web', '08:00', '5 horas', 'Chile', 'Curso practico sobre la creacion de sitios web utilizando HTML, CSS y JavaScript', 'Presencial', 'Espaniol')
    add_evento('006', 'Taller de Inteligencia Artificial', '12:00', '4 horas', 'Estados Unidos', 'Taller de desarrollo de soluciones basadas en inteligencia artificial', 'Presencial', 'Ingles')