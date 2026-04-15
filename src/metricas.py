def calcular_senal_promedio(lista):
    if len(lista) == 0:
        raise ValueError("Lista no puede estar vacia")
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

Raises:
ValueError: Si la lista esta vacia
'''

def calcular_maximo_senal(lista):
  if len(lista) == 0:
    raise ValueError("La lista esta vacia")
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

Raises:
ValueError: si la lista esta vacia
'''


def calcular_minimo_senal(lista):
    if len(lista) == 0:
      raise ValueError("La lista está vacía")
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

Raises:
ValueError: si la lista esta vacia
'''

def calcular_frecuencia_cardiaca(picos):
    if len(picos) < 2:
        raise ValueError("No hay suficientes picos para calcular la frecuencia")
    
    picos_numericos = []
    for p in picos:
        try:
            picos_numericos.append(float(p))
        except ValueError:
            raise ValueError("Los picos deben ser numeros")

    suma_intervalos = 0

    for i in range(1, len(picos_numericos)):
        intervalo = picos_numericos[i] - picos_numericos[i-1]
        suma_intervalos += intervalo

    intervalo_promedio = suma_intervalos / (len(picos_numericos) - 1)

    if intervalo_promedio == 0:
        raise ValueError("El intervalo promedio no puede ser 0")
   
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
    
Raises:
ValueError: si no hay suficientes picos para calcular la frecuencia, 
            si los picos no son numeros, y si el intervalo promedio es 0
'''

from src.utils_ecg import detectar_picos_qrs 

def calcular_fc_desde_datos(datos): 
    tiempos = [] 
    senal = [] 
    for d in datos: 
        tiempos.append(d["tiempo"]) 
        senal.append(d["valor"]) 
    picos = detectar_picos_qrs(tiempos, senal) 
    return calcular_frecuencia_cardiaca(picos)

'''
Funcion que calcula la frecuencia cardiaca a partir de una lista de datos 

Parámetros:
datos: list
    lista de diccionarios donde cada diccionario contiene las claves "tiempo" y "valor" 
    
Retorna:
frecuencia: float
    La frecuencia cardiaca calculada en latidos por minuto.
'''
