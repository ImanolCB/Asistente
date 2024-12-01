import pyttsx3                      # Transforma texto a voz

#Función para que el asistente pueda ser escuchado, el asistente habla
"""
#Script para mostrar las voces del equipo
engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)
"""
 
id1="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
id2="HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"

def hablar(mensaje, id):
    #Inicializamos el moto de pyttsx3
    engine = pyttsx3.init()
    #Seleccionamos la voz
    engine.setProperty("voice",id)
    #Más propiedades de la voz
    engine.setProperty("rate",150) #Velocidad de la voz
    engine.setProperty("volumen",1) #Volumen de la voz
    #Ponemos a la cola el mensaje
    engine.say(mensaje)
    #Ejecutamos el motor y esperamos a que termine
    engine.runAndWait()