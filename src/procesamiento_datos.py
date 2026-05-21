def filtrar_por_participante(lista, id_buscado):
    '''
    filtra una lista de diccionarios con un id buscado y devuelve los datos de ese id.

    Parameters
    ----------
    lista : list
        una lista que contiene diccionarios con datos de los pacientes.
    id_buscado : int
        numero de id del paciente cuyos datos se quieren obtener.

    Returns
    -------
    filtrados : list
        lista con diccionario de los datos del paciente buscado.

    '''
    if isinstance(id_buscado, str) and id_buscado.lower() == 'todos':
        return lista
    
    try:
        id_buscado = int(id_buscado)
    except ValueError:
        print('El ID debe ser un número o "todos"')
        return []
    
    filtrados = []
    

    for dato in lista:
        if dato["id_participante"] == id_buscado:
            filtrados.append(dato)  

    return filtrados


#Filtrado de participantes con PANDAS
def filtrar_por_participante_pandas(df, id_participante):
    """
    Filtra los datos correspondientes a un participante.

    Parámetros:
    ----------
    df : pandas.DataFrame
        DataFrame con todos los datos cargados.

    id_participante : int
        ID del participante que se desea buscar.

    Returns:
    -------
    pandas.DataFrame
        DataFrame filtrado con los datos
        del participante seleccionado.
    """

    df_filtrado = df[df["id"] == id_participante]

    return df_filtrado