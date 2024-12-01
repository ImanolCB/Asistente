# import pyttsx3                      # Transforma texto a voz
# import speech_recognition as sr     # Reconoce la voz del usuario
# import pywhatkit                    # Realizar búsquedas en la web y YouTube
# #import yfinance as yf              # Ver precios de las acciones
# import pyjokes                      # Obtiene chistes en diferentes idiomas
# from googletrans import Translator  # Traductor de Google

# import webbrowser
import datetime
from difflib import get_close_matches
from pathlib import Path

# import wikipedia
# Imports internos del proyecto
from busqueda_web_yt import *
from chistes import *
from fechas_horas import *
from reconocimiento_de_voz import *
from texto_a_voz import *
from traductor import *
from calculadora import *
from api_weather import *

# Ha sido necesario instalar pyAudio
# Desarrollado por Imanol Callejo Baranda


# Saludo del asistente
def saludo_inicial():

    #Declaramos una variable con los datos del tiempo actual
    hora = datetime.datetime.now()

    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches, soy tu asistente, ¿Que deseas?"

    elif  6 < hora.hour > 13:
        momento = "Buenas tardes, soy tu asistente, ¿Que deseas?"

    else :
        momento = "Buenos días, soy tu asistente, ¿Que deseas?"


    hora = f'{momento}'
    hablar(hora, id1)
    

# Obtener respuesta
import json
import random
from difflib import get_close_matches


ruta = Path(Path.cwd(), "./datos.json")
print(ruta)

# Leer el archivo JSON
try:
    with open(ruta, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("Error: el archivo no se ha encontrado.")
    datos = {}
except json.JSONDecodeError:
    print("Error: formato incorrecto.")
    datos = {}


# Funcion para responder al usuario 
def obtener_respuesta(mensaje):
    with open("./datos.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    mensaje = mensaje.lower()

    for intent in datos['intents']:
        patrones = [pattern.lower() for pattern in intent['patterns']]
        coincidencias = get_close_matches(mensaje, patrones, n=1, cutoff=0.6)  # Ajusta `cutoff` para la sensibilidad
        if coincidencias:
            return random.choice(intent['responses'])
    return None

# Función para añadir una respuesta nueva proporcionada por el usuario
def anadir_respuesta(mensaje_usuario):
    global datos
    
    hablar(f"No tengo la respuesta para: {mensaje_usuario}, ¿Quieres proporcionarme la respuesta para la próxima vez?", id1)
    option = transformar_audio_texto().lower()
    if "sí" in option or "si quiero" in option:
        hablar(f"¿Qué es lo que debería responder la próxima vez?", id1)
        nueva_respuesta = transformar_audio_texto().lower()
        
        if 'intents' not in datos:
            datos['intents'] = []
        contador_aprendidos = sum(1 for intent in datos['intents'])
        nuevo_tag = f'Tag aprendido {contador_aprendidos}'
        
        nuevo_intent = {
        "tag": nuevo_tag,
        "patterns": [mensaje_usuario],
        "responses": [nueva_respuesta]
        }
        # Añadir el nuevo intent al documento JSON
        datos['intents'].append(nuevo_intent)
   
        # Guardamos los cambios en el archivo JSON utilizando la misma ruta
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii= False)
        
        # Recargamos los datos desde el archivo JSON
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
   
        return nueva_respuesta
    
    elif "no" in option:
        hablar(f"De acuerdo", id1)

    else:
        hablar(f"No puesdo procesar esa respuesta", id1)

# Funcion central
def pedir_cosas():
    #Activar saludo inicial
    saludo_inicial()

    #Inicio variables de corte
    comenzar = True
    primera_vez = True

    while comenzar:
        if not primera_vez:
            hablar("¿Necesitas algo más?", id1)
        primera_vez = False

        pedido = transformar_audio_texto().lower()

        if "qué día es" in pedido:
            try:
                pedir_dia()
            except Exception as e:
                hablar(f"No ha podido obtener el día de la semana", id1)
                print(f"Error: {e}")
                
        elif "qué hora es" in pedido:
            try:
                pedir_hora()
            except Exception as e:
                hablar(f"No ha podido obtener la hora", id1)
                print(f"Error: {e}")

        elif "abre youtube" in pedido:
            try:
                abrir_youtube()
            except Exception as e:
                hablar(f"No ha podido abrir YouTube", id1)
                print(f"Error: {e}")

        elif "busca en wikipedia" in pedido:
            try:
                hablar("Dime qué buscar en Wikipedia", id1)
                termino = transformar_audio_texto()
                buscar_wikipedia(termino)
            except Exception as e:
                hablar(f"No pude buscar en Wikipedia: {termino}", id1)
                print(f"Error: {e}")
                
        elif "busca en internet" in pedido:
            try:
                buscar_internet()
            except Exception as e:
                hablar(f"No pude realizar la búsqueda", id1)
                print(f"Error: {e}")

        elif "reproduce" in pedido:
            try:
                reproducir_en_yt(pedido)
            except Exception as e:
                hablar(f"No se ha podido abrir YouTube: {pedido}", id1)
                print(f"Error: {e}")

        elif "chiste" in pedido:
            try:
                contar_chiste()
            except Exception as e:
                hablar(f"No he encontrado ningún chiste", id1)
                print(f"Error: {e}")

        elif "traduce" in pedido:
            try:
                traducir(pedido)
            except Exception as e:
                hablar(f"No ha podido hacer la traducción de {pedido}", id1)
                print(f"Error: {e}")

        elif "calcula" in pedido:
            try:
                operar(pedido)
            except Exception as e:
                hablar(f"No ha podido hacer la operación {pedido}", id1)
                print(f"Error: {e}")
        
        elif "qué tiempo" in pedido:
            try:
                informar_clima(pedido)
            except Exception as e:
                hablar(f"No ha podido obtener el clima de {pedido}", id1)
                print(f"Error: {e}")
        
        elif "eso es todo" in pedido or "adiós" in pedido or "chao" in pedido:
            hablar("¡Hasta la próxima!", id1)
            break

        else:
            respuesta = obtener_respuesta(pedido)
            print(respuesta)
            if respuesta is not None:
                hablar(respuesta,id1)
            else:
                 anadir_respuesta(pedido)

pedir_cosas()