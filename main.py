from carga_datos import cargar_datos
from procesamiento_datos import filtrar_por_participante
from metricas import (calcular_promedio_senal, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos)

datos = cargar_datos("datos_proyecto.csv")

id_participante = int(input("id que desea buscar: "))
datos_p1 = filtrar_por_participante(datos, id_participante)

promedio = calcular_promedio_senal(datos_p1)
maximo = calcular_maximo_senal(datos_p1)
minimo = calcular_minimo_senal(datos_p1)
frecuencia = calcular_fc_desde_datos(datos_p1)

print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Frecuencia cardíaca:", frecuencia)