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

    '''
    linea_str = linea.strip("\n")
    linea_spl = linea_str.split(",")
    valores = linea_spl


    id_participante = valores[0]
    tiempo = valores[1]
    valor = valores[2]
    fase = valores[3]
    condicion_experimental = valores[4]
    hit = valores[5]


    dic = {"id_participante": id_participante,
         "tiempo": tiempo, "valor": valor,
         "fase": fase, "condicion_experimental": condicion_experimental,
         "hit": hit}
  
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

    archivo = open(archivo, "r")

    lineas = archivo.readlines()

    for linea in lineas:
        registro = parsear_lineas(linea)
        datos.append(registro)

    archivo.close()

    return datos



