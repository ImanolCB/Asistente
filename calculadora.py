from texto_a_voz import *           # Convierte texto en audio
from reconocimiento_de_voz import * # Detecta audio y convierte a texto

import re
import math

def operar(pedido):
    
    # Eliminar 'calcula' al inicio
    operacion = pedido.replace('calcula', '', 1).strip()
    
    # Reemplazar palabras clave por operadores matemáticos
    operacion = operacion.replace('por', '*')
    operacion = operacion.replace('más', '+')
    operacion = operacion.replace('menos', '-')
    operacion = operacion.replace('entre', '/')
    operacion = operacion.replace('dividido por', '/')
    operacion = operacion.replace('elevado a', '**')
    
    try:
        resultado = eval(operacion)
     # Decir el resultado
        hablar(f"El resultado es {resultado}", id1)
    except Exception as e:
        print(e)
        hablar("No pude realizar el cálculo.", id1)
    