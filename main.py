from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (calcular_senal_promedio, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos)

datos = cargar_datos("datos/PulseLab_mock_data.csv")

if len(datos) == 0:
    print('No se pudieron cargar datos')

else:
    id_participante_str = input('ID que desea buscar: ')
    
    try:
        id_participante = int(id_participante_str)
    except ValueError:
        print('El ID debe ser un numero')

    datos_part = filtrar_por_participante(datos, id_participante)
    
    if len(datos_part) == 0:
        print('No se encontraron datos para ese participante')
        
    else:
        promedio = calcular_senal_promedio(datos_part)
        maximo = calcular_maximo_senal(datos_part)
        minimo = calcular_minimo_senal(datos_part)
        frecuencia = calcular_fc_desde_datos(datos_part)
    
        print("Promedio:", promedio)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)
        print("Frecuencia cardíaca:", frecuencia)
