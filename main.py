from src.carga_datos import cargar_datos_pandas
from src.procesamiento_datos import filtrar_por_participante_pandas
from src.metricas import (calcular_senal_promedio_pandas, calcular_maximo_senal_pandas, calcular_minimo_senal_pandas, calcular_fc_desde_datos_pandas)

datos = cargar_datos_pandas("datos/PulseLab_mock_data.csv")

if datos.empty:
    print("No se pudieron cargar datos")


else:
    id_participante = int(input('ID que desea buscar: '))
    
    datos_part = filtrar_por_participante_pandas(datos, id_participante)

    if datos_part.empty:
        print("No se encontraron datos para ese participante")

    else:
        try:
           promedio = calcular_senal_promedio_pandas(datos_part)
           maximo = calcular_maximo_senal_pandas(datos_part)
           minimo = calcular_minimo_senal_pandas(datos_part)
           print("Promedio:", promedio)
           print("Máximo:", maximo)
           print("Mínimo:", minimo)
           
        except ValueError as e:
            print("Error en las métricas básicas:", e)
        
        try:
           frecuencia = calcular_fc_desde_datos_pandas(datos_part) 
           print("Frecuencia cardíaca:", frecuencia)
        except ValueError as e:
            print("Error en la frecuencia:", e)

    

