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
    filtrados = []
    if len(lista) == 0:
        print('Lista vacía')
    
    try:
        id_buscado = int(id_buscado)
        if isinstance(id_buscado, str) and id_buscado.lower() =='todos':
            return lista
        print('El ID debe ser un numero o ''todos''')
        
    except Exception:
        print("todo mal")
    
    else:
        for dato in lista:
            if dato["id_participante"] == id_buscado:
                filtrados.append(dato)  
        if len(filtrados) == 0:
            print('No se encontraron datos para ese participante')
        else:
            return filtrados