import requests

class Evento:
    def __init__(self, id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma):
        self.id = id
        self.nombre = nombre
        self.hora = hora
        self.duracion = duracion
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.tipo_evento = tipo_evento
        self.idioma = idioma

    def describe(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "hora": self.hora,
            "duracion": self.duracion,
            "ubicacion": self.ubicacion,
            "descripcion": self.descripcion,
            "tipo de evento": self.tipo_evento,
            "idioma": self.idioma
        }

class CapacidadLimitada(Evento):
    def __init__(self, id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma, capacidad):
        self.capacidad = capacidad
        super().__init__(id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma, capacidad)

def obtener_eventos(base_url):
    url = f"{base_url}/eventos"
    response = requests.get(url)
    if response.status_code == 200:
        eventos = response.json()
        eventos_transformados = []
        for e in eventos:
            eventos_transformados.append(crear_evento(e))
        return eventos_transformados
    return None

def agregar_evento(base_url, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento):
    url = f"{base_url}/eventos"
    payload = {"nombre": nombre_evento, "hora": hora_evento, "duracion": duracion_evento, "ubicacion": ubicacion_evento, "descripcion": descripcion_evento, "tipo_evento": tipo_evento, "idioma": idioma_evento}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Evento agregado")

def crear_evento(evento):
    if evento[]
