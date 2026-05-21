#Funcion que convierta a float y valide 
def convertir_float(linea):
    '''
    Funcion que convierte valor de str a float. 

    Parameters
    ----------
    linea : str
        Linea de archivo.

    Returns
    -------
    valor float
    
    Raises
    -------
    ValueError: si el str no se puede convertir a float.
    '''
    try:
        return float(linea)
    except ValueError:
        raise ValueError('Error al convertir valor a float')

def validar_categoria(valor, opciones_validas, nombre_campo):
    '''
    Funcion que valida que el valor este dentro de las opciones validas.
    Parameters
    ----------
    valor : str
        Nombre de la condicion o de las fases.
    opciones_validas : lista
        Lista con las opciones validas.
    nombre_campo : str
        Nombre del campo que se esta validando.

    Returns
    -------
    None.
    
    Raises
    ------
    ValueError: si la opcion elegida es invalida.

    '''
    if valor not in opciones_validas:
        raise ValueError(f"{nombre_campo} invalido. Opciones validas: {opciones_validas}")

def validar_entero_positivo(valor, nombre_campo):
    '''
    Funcion que valida que los valores ingresados sean enteros y positivos

    Parameters
    ----------
    valor : int
        El numero a validar.
    nombre_campo : str
        Nombre del tipo de dato a validar.

    Returns
    -------
    None.
    
    Raises
    ------
    ValueError: si el valor es menor o igual a cero.

    '''
    if valor <= 0:
        raise ValueError(f"{nombre_campo} debe ser mayor a 0")

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
    
    try: #acortar el try para indicar el error o usar if y raises
        id_participante = int(valores[0])
        validar_entero_positivo(id_participante, "id_participante")
        tiempo = convertir_float(valores[1]) 
        valor = convertir_float(valores[2])
        fase = valores[3]
        validar_categoria(fase, ["baseline", "tarea"], "fase")
        condicion_experimental = valores[4]
        validar_categoria(condicion_experimental, ["competencia", "cooperacion"], "condicion_experimental")
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





#Función cargar datos con PANDAS
import pandas as pd
import os 

def cargar_datos_pandas(archivo):
    
    """
  Carga un archivo CSV utilizando Pandas y realiza
  validaciones vectorizadas sobre los datos.

  Parámetros:
  ----------
  archivo : str
    Ruta del archivo CSV.

  Returns:
  -------
  pandas.DataFrame
    DataFrame con los datos cargados y validados.

  Raises:
  ------
  FileNotFoundError
    Si el archivo no existe.

  ValueError
    Si los datos contienen errores o inconsistencias.
    """
  
    #Validación de ruta física/exista archivo
    if not os.path.exists(archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo}")

    #Carga de datos (CSV)
    ## El archivo CSV no contiene encabezados,por eso se utilizan header=None y names=[]
    df = pd.read_csv(archivo, header=None, names=["id_participante", "tiempo", "valor", "fase", "condicion_experimental", "hit"])

    #Validar valores vacíos
    if df.isna().any().any():
        raise ValueError("El archivo contiene valores vacíos o NaN.")
  
    #Validar tiempos negativos
    if (df["tiempo"] < 0).any():
        raise ValueError("Existen tiempos negativos inválidos.")

    #Validar señal negativa
    if (df["valor"] < 0).any():
        raise ValueError("Existen valores negativos inválidos en la señal.")

    #Validar orden temporal
    if not df["tiempo"].is_monotonic_increasing:
        print("Advertencia: los tiempos no están completamente ordenados.")

    #Validar valores permitidos en fase
        fases_validas = ["baseline", "tarea"]

    if not df["fase"].isin(fases_validas).all():
        raise ValueError("Se detectaron fases experimentales inválidas.")

    return df