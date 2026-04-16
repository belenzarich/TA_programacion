from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (calcular_senal_promedio, calcular_maximo_senal, calcular_minimo_senal, calcular_fc_desde_datos)

datos = cargar_datos("datos/PulseLab_mock_data.csv")

if len(datos) == 0:
    print('No se pudieron cargar datos')

else:
    id_participante_str = input('ID que desea buscar: ')
    
    if id_participante_str in ['todos', 'Todos', 'TODOS']:
        datos_part = datos
        
        try:
           promedio = calcular_senal_promedio(datos_part) #tal vez podemos poner todas las funciones en un mismo try y despues valueerror as e
        except ValueError as e:
            print("Error:", e)
        try:
            maximo = calcular_maximo_senal(datos_part)
        except ValueError as e:
            print("Error:", e)
        try:
            minimo = calcular_minimo_senal(datos_part)
        except ValueError as e:
            print("Error:", e)
        try:
            frecuencia = calcular_fc_desde_datos(datos_part)
        except ValueError as e:
            print("Error: ", e)

        print("Promedio:", promedio)
        print("Máximo:", maximo)
        print("Mínimo:", minimo)
        print("Frecuencia cardíaca:", frecuencia)
     
    else:

        try:
            id_participante = int(id_participante_str)
        except ValueError:
            print('El ID debe ser un numero')
        
        else:
    
            datos_part = filtrar_por_participante(datos, id_participante)
            
            if len(datos_part) == 0:
                print('No se encontraron datos para ese participante')
                
            else:
                try:
                   promedio = calcular_senal_promedio(datos_part)
                except ValueError as e:
                    print("Error:", e)
                try:
                    maximo = calcular_maximo_senal(datos_part)
                except ValueError as e:
                    print("Error:", e)
                try:
                    minimo = calcular_minimo_senal(datos_part)
                except ValueError as e:
                    print("Error:", e)
                try:
                    frecuencia = calcular_fc_desde_datos(datos_part)
                except ValueError as e:
                    print("Error: ", e)
        
                print("Promedio:", promedio)
                print("Máximo:", maximo)
                print("Mínimo:", minimo)
                print("Frecuencia cardíaca:", frecuencia)

# tal vez todo lo de arriba de los try/except y los print podrían ser una funcion