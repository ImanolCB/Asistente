import pywhatkit    # Realizar búsquedas en la web y YouTube
import wikipedia    # Libreria de wikipedia
import webbrowser   #Librería para ejecutar youtube

from texto_a_voz import *           # Convierte texto en audio
from reconocimiento_de_voz import * # Detecta audio y convierte a texto
from traductor import *             # Traduce del inglés al español y al reves

def buscar_internet():
    hablar("Dime qué buscar en internet", id1)
    termino = transformar_audio_texto()
    pywhatkit.search(termino)
    hablar("Esto es lo que encontré", id1)
                
def buscar_wikipedia(termino):
    
    pagina = wikipedia.page(termino)
    resultado_completo = pagina.content
    print("\n",resultado_completo, "\n")
    resultado = wikipedia.summary(termino, sentences=2)
    print('Fuente: ', resultado)
    resultado_traducido = traducir_texto(resultado)
    print('Traduccion: ', traducir_texto(resultado_traducido))
    hablar("Wikipedia dice lo siguiente: " + resultado_traducido, id1)
    
def abrir_youtube():
    hablar("Un momento, estoy abriendo YouTube", id1)
    webbrowser.open("https://youtube.es")
    
def reproducir_en_yt(pedido):
    hablar("Abriendo reproductor", id1)
    pedido = pedido.split("reproduce", 1)[1].strip()
    pywhatkit.playonyt(pedido)