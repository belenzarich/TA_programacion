#Funcion de parsear 
def parsear_lineas(linea):
    '''
    Función que parsea líneas, separa sus elementos con una "," 
    y los agrega a un diccionario con las siguientes claves 
    "id_participante", "tiempo", "valor", "fase", "condicion_experimental"
    y "hit".

    Parameters
    ----------
    linea : str
        línea de archivo a parsear.

    Returns
    -------
    dic : diccionario
        diccionario con valores de cada elemento de una línea.
    
    Raises
        ValueError: si el valor para hit es inválido (distinto de 'true' o 'false') o si no se puede convertir algún dato

    '''
    linea_str = linea.strip()
    valores = linea_str.split(",")

    if len(valores) != 6:
        raise ValueError('Cantidad incorrecta de columnas')
    
    try:
        id_participante = int(valores[0])
        tiempo = float(valores[1])
        valor = float(valores[2])
        fase = valores[3]
        condicion_experimental = valores[4]
        hit_str = valores[5].strip().lower()
        if hit_str not in ['true', 'false']:
            raise ValueError('Valor invalido para hit')
            
        if hit_str == 'true':
            hit = True
        else:
            hit = False


        dic = {"id_participante": id_participante,
             "tiempo": tiempo, "valor": valor,
             "fase": fase, "condicion_experimental": condicion_experimental,
             "hit": hit}
    except Exception:
        raise ValueError('Error al convertir datos')
  
    return dic

#Funcion de cargar datos
def cargar_datos(archivo):
    '''
    Función que abre un archivo, lee cada línea, la parsea 
    con la función "parsear_lineas" y agrega cada diccionario 
    a una lista.

    Parameters
    ----------
    archivo : str
        archivo con datos.

    Returns
    -------
    datos : lista
        Lista con diccionarios de cada línea.

    '''
    datos = []
    
    try:
        archivo = open(archivo, "r")
        
    except FileNotFoundError:
        print('Error: Archivo no encontrado')
        return datos
    
    except Exception as e:
        print('Error al abrir el archivo:', e)
        return datos

    lineas = archivo.readlines()

    for linea in lineas:
        
        try:
            registro = parsear_lineas(linea)
            datos.append(registro)
            
        except Exception:
            linea_invalida = linea.strip()
            print('Línea inválida (se saltea):', linea_invalida)
            continue

    archivo.close()

    return datos
