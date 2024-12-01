import requests
from texto_a_voz import *           # Convierte texto en audio
from reconocimiento_de_voz import * # Detecta audio y convierte a texto


def informar_clima(pedido):
    try:
     
    # Buscar la ciudad en el pedido
        if 'en' in pedido:
            ciudad = pedido.split('en', 1)[1].strip()
        else:
            hablar("Por favor, repite incluyendo la ciudad para verificar el clima.", id1)
            return
    
        # URL de la API de OpenWeatherMap
        api_key = '053698ef0869b1271759e6ae9d361996' # Reemplazar con tu propia API key 
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    
        # Realizar la solicitud a la API
        respuesta = requests.get(url)
        datos = respuesta.json()
        print(datos)
    
        if datos['cod'] == 200:
            # Obtener los datos del clima
            temp = datos['main']['temp']
            descripcion = datos['weather'][0]['description']
            mensaje = f"El clima en {ciudad} es de {temp} grados Celsius con {descripcion}."
            # Decir el clima
            hablar(mensaje, id1)
        else:
            hablar(f"No pude obtener el clima para {ciudad}. Por favor verifica el nombre.", id1)
    except Exception as e:
        print(f"Error al consultar el clima: {e}")
        hablar("Hubo un problema al obtener el clima. Inténtalo de nuevo más tarde.", id1)