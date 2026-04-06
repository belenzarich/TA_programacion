def calcular_senal_promedio(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for dato in lista:
        valor = dato["valor"]
        suma += valor
    promedio = suma / len(lista)
    return promedio
'''
Funcion que calcula el promedio de la señal de una lista de diccionarios

Parámetros:
lista: list
    Lista de diccionarios donde cada diccionario representa los datos de un paciente

Retorna:
promedio: float
   El promedio de los valores 
'''

def calcular_maxima_senal(lista):
    if len(lista) == 0:
        return 0
    maximo = lista[0]["valor"]

    for dato in lista:
        valor = dato["valor"]
        if valor > maximo:
            maximo = valor
    return maximo
'''
Funcion que busca el valor máximo de señal en una lista de diccionarios

Parámetros:
lista: list
    Lista de diccionarios donde cada diccionario representa los datos de un paciente

Retorna:
maximo: int
   El valor máximo encontrado.  
'''


def calcular_minima_senal(lista):
    if len(lista) == 0:
        return 0
    minimo = lista[0]["valor"]
    for dato in lista:
        valor = dato["valor"]
        if valor < minimo:
            minimo = valor
    return minimo
'''
Funcion que busca el valor mínimo de señal en una lista de diccionarios

Parámetros:
lista: list
    Lista de diccionarios donde cada diccionario representa los datos de un paciente

Retorna:
minimo: int
   El valor mínimo encontrado.  
'''

def calcular_frecuencia_cardiaca(picos):
    if len(picos) < 2:
        return "no se puede calcular la FC porque no hay suficientes picos"
    
    suma_intervalos = 0

    for i in range(1, len(picos)):
        intervalo = picos[i] - picos[i-1]
        suma_intervalos += intervalo

    intervalo_promedio = suma_intervalos / (len(picos) - 1)
    frecuencia = 60 / intervalo_promedio

    return frecuencia
'''
Funcion que calcula la frecuencia cardiaca a partir de una lista de picos 

Parámetros:
picos: list
    lista de valores numericos que representan los tiempos en los que ocurren los picos. 
    
Retorna:
frecuencia: float
    La frecuencia cardiaca calculada en latidos por minuto.
'''