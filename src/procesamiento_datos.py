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
        lista con los datos del paciente buscado.

    '''
    filtrados = []
    
    for dato in lista:
        if dato["id_participante"] == id_buscado:
            filtrados.append(dato)
    
    return filtrados