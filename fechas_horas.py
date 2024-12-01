import datetime
from texto_a_voz import hablar, id1, id2


#Informar del dia
def pedir_dia():

    #creamos una variable con los datos de hoy
    dia = datetime.date.today()
    print(dia)
    dia_semana = dia.weekday()
    calendario = {
        0: "lunes",
        1: "martes",
        2: "miercoles",
        3: "jueves",
        4: "viernes",
        5: "sabado",
        6: "domingo"
    }
    hablar(f'Hoy es {calendario[dia_semana]},', id1)


#Informar de la hora
def pedir_hora():

    #creamos una variable con los datos de hoy
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas, {hora.minute} minutos, {hora.second} segundos'
    hablar(hora, id1)