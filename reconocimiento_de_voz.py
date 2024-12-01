import speech_recognition as sr     # Reconoce la voz del usuario

#Funcion para recoger el audio del micro para reconocer palabras
def transformar_audio_texto():
    r = sr.Recognizer()

    with sr.Microphone() as microfono:
        r.pause_threshold = 1

        print("Ya puedes hablar")

        audio = r.listen(microfono)

        try:
            texto = r.recognize_google(audio, language= "es-es")
            print("Dijiste: " + texto)
            return texto
        except sr.UnknownValueError:
            print("Ups, no entendí")
            return "Sigo esperando"
        except sr.RequestError:
            print("Ups, el servicio esta inactivo")
            return "Sigo esperando"
        except:
            print("Ups")
            return "Sigo esperando"