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
            "tipo_evento": self.tipo_evento,
            "idioma": self.idioma
        }

class CapacidadLimitada(Evento):
    def __init__(self, id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma, capacidad):
        super().__init__(id, nombre, hora, duracion, ubicacion, descripcion, tipo_evento, idioma)
        self.capacidad = capacidad

def obtener_eventos(base_url):
    url = f"{base_url}/eventos"
    response = requests.get(url)
    if response.status_code == 200:
        eventos = response.json()
        eventos_transformados = []
        for e in eventos:
            eventos_transformados.append(crear_evento(e))
        return eventos_transformados
    else:
        print(f"No se pudieron obtener los eventos. Código de estado: {response.status_code}")
        return []

def obtener_evento_por_id(base_url, id_evento):
    url = f"{base_url}/eventos/{id_evento}"
    response = requests.get(url)
    if response.status_code == 200:
        evento = response.json()
        return crear_evento(evento)
    else:
        print(f"No se pudo obtener el evento")
        return None

def agregar_evento(base_url, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento, tipo, capacidad=None):
    url = f"{base_url}/eventos"
    payload = {
        "nombre": nombre_evento,
        "hora": hora_evento,
        "duracion": duracion_evento,
        "ubicacion": ubicacion_evento,
        "descripcion": descripcion_evento,
        "tipo_evento": tipo_evento,
        "idioma": idioma_evento
    }
    if tipo == "capacidad limitada":
        payload["capacidad"] = capacidad
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Evento agregado exitosamente")
    else:
        print(f"No se pudo agregar el evento")

def crear_evento(evento):
    if "tipo" in evento:
        if evento["tipo"] == "capacidad limitada":
            return CapacidadLimitada(
                evento["id"],
                evento["nombre"],
                evento["hora"],
                evento["duracion"],
                evento["ubicacion"],
                evento["descripcion"],
                evento["tipo_evento"],
                evento["idioma"],
                evento["capacidad"]
            )
    else:
        return Evento(
            evento["id"],
            evento["nombre"],
            evento["hora"],
            evento["duracion"],
            evento["ubicacion"],
            evento["descripcion"],
            evento["tipo_evento"],
            evento["idioma"]
        )

def actualizar_evento(base_url, id_evento, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento):
    url = f"{base_url}/eventos/{id_evento}"
    payload = {
        "nombre": nombre_evento,
        "hora": hora_evento,
        "duracion": duracion_evento,
        "ubicacion": ubicacion_evento,
        "descripcion": descripcion_evento,
        "tipo_evento": tipo_evento,
        "idioma": idioma_evento
    }

    response = requests.put(url, json=payload)
    if response.status_code == 200:
        print("Evento actualizado exitosamente")
    else:
        print(f"No se pudo actualizar el evento")

def main():
    base_url = "http://127.0.0.1:5000"
    while True:
        print("Opciones")
        print("1: Ver todos los eventos")
        print("2: Ver evento por ID") 
        print("3: Agregar un evento nuevo")
        print("4: Actualizar un evento existente")  # Puedes implementar esta opción si deseas
        print("5: Eliminar un evento existente")  # Puedes implementar esta opción si deseas
        print("6: Salir")

        option = int(input("Seleccione una opción: "))

        if option == 1:
            print("Ver eventos")
            eventos = obtener_eventos(base_url)
            if eventos:
                for e in eventos:
                    print(Evento.describe(e))
            else:
                print("No se pudieron obtener los eventos")

        elif option == 2:
            print("Ver evento con ID")
            id_evento = input("Ingrese el ID del evento: ")
            evento = obtener_evento_por_id(base_url, id_evento)
            if evento:
                print(evento.describe())
            else:
                print(f"No se encontró ningún evento con ID: {id_evento}")

        elif option == 3:
            print("Agregar evento")
            nombre_evento = input("Nombre del evento: ")
            hora_evento = input("Hora del evento: ")
            duracion_evento = input("Duración del evento: ")
            ubicacion_evento = input("Ubicación del evento: ")
            descripcion_evento = input("Descripción del evento: ")
            tipo_evento = input("El evento es presencial o virtual?: ")
            idioma_evento = input("Idioma del evento: ")
            tipo = input("¿Evento de capacidad limitada? (Sí/No): ").lower()

            if tipo == "sí":
                while True:
                    try:
                        capacidad_evento = int(input("Capacidad del evento: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número válido para la capacidad.")

                agregar_evento(base_url, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento, "capacidad limitada", capacidad_evento)
            else:
                agregar_evento(base_url, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento, "normal")

        elif option == 4:
            print("Actualizar evento")
            id_evento = input("ID del evento a actualizar: ")
            nombre_evento = input("Nuevo nombre del evento: ")
            hora_evento = input("Nueva hora del evento: ")
            duracion_evento = input("Nueva duración del evento: ")
            ubicacion_evento = input("Nueva ubicación del evento: ")
            descripcion_evento = input("Nueva descripción del evento: ")
            tipo_evento = input("El evento es presencial o virtual?: ")
            idioma_evento = input("Nuevo idioma del evento: ")

            actualizar_evento(base_url, id_evento, nombre_evento, hora_evento, duracion_evento, ubicacion_evento, descripcion_evento, tipo_evento, idioma_evento)

        elif option == 6:
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
