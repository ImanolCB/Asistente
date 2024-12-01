import googletrans  # Traductor de Google
from texto_a_voz import *


def traducir_texto(frase):
    traductor = googletrans.Translator()
    traduccion = traductor.translate(frase, src='en', dest='es')
    # Obtener el texto traducido
    texto_traducido = traduccion.text
    return texto_traducido



def traducir(frase):
   # Eliminar 'traduce' al inicio
    pedido = frase.replace('traduce', '', 1).strip()

# Dividir la frase y el idioma destino
    partes = pedido.rsplit(' al ', 1)
    if len(partes) == 2:
        frase = partes[0].strip()
        idioma = partes[1].strip().lower()

        # Mapeo de idiomas a códigos de idioma
        codigo_idioma = {
            'inglés': 'en',
            'francés': 'fr',
            'alemán': 'de',
            'italiano': 'it',
            'español': 'es',
            'portugués': 'pt'
        }

        if idioma in codigo_idioma:
            traductor = googletrans.Translator()
            traduccion = traductor.translate(frase, src='es', dest=codigo_idioma[idioma])
            # Obtener el texto traducido
            texto_traducido = traduccion.text
            print(texto_traducido)

            # Decir la traducción
            hablar(f"La traducción en {idioma} es: ", id1)
            hablar(f"{texto_traducido}", id2)
        else:
                hablar("Lo siento, no soporto ese idioma.", id1)
    else:
        hablar("No entendí la frase o el idioma para traducir.", id1)
