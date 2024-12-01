# Asistente de Voz en Python

Este repositorio contiene un **Asistente de Voz** desarrollado en Python. Este proyecto integra diversas herramientas y tecnologías para ofrecer funcionalidades como reconocimiento de voz, síntesis de texto a voz, búsquedas en la web, consultas del clima, chistes, traducción de texto, y mucho más. Está diseñado para mostrar mis habilidades como desarrollador en proyectos prácticos e innovadores.

---

## **Características**
- **Reconocimiento de voz**: Utiliza `speech_recognition` para interpretar comandos hablados.
- **Síntesis de voz**: Usa `pyttsx3` para responder verbalmente.
- **Consultas climáticas**: Integra una API de tiempo para brindar información meteorológica.
- **Búsquedas en la web**: Capacidad para buscar información en internet o reproducir videos en YouTube usando `pywhatkit`.
- **Traducción de texto**: Implementa Google Translator para traducir entre idiomas.
- **Chistes y entretenimiento**: Ofrece chistes en diferentes idiomas usando `pyjokes`.

---

## **Tecnologías y herramientas utilizadas**
- `pyttsx3`: Conversión de texto a voz.
- `speech_recognition`: Reconocimiento de comandos hablados.
- `pywhatkit`: Búsquedas en internet y reproducción de videos en YouTube.
- `datetime`: Gestión de fechas y horas.
- `difflib`: Coincidencia aproximada de patrones de texto.
- `pyjokes`: Generación de chistes.
- `googletrans`: Traducción entre idiomas.
- `webbrowser`: Apertura de navegadores para búsquedas.
- API de clima: Información meteorológica en tiempo real.
- `wikipedia` (comentado): Posibilidad de realizar consultas en Wikipedia.

---

## **Requisitos del sistema**
- Python 3.7 o superior.
- Conexión a internet para funcionalidades basadas en APIs.
- Librerías especificadas en `requirements.txt`.

---

## **Instalación y uso**

Sigue los pasos a continuación para configurar y ejecutar el asistente:

### **1. Clonar el repositorio**
```bash
git clone https://github.com/ImanolCB/Asistente.git

cd asistente-voz-python

python -m venv venv

xcopy *.py venv\ /Y
xcopy requirements.txt venv\ /Y

venv\Scripts\activate

pip install -r requirements.txt


