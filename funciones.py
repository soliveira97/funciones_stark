# STARK-2 # Santiago Oliveira - 1F
def mostrar_menu():
    '''
    Imprime un menú
    :return:
    '''
    print("\n\n1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB\n"
          "2. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
          "3. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
          "4. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\n"
          "5. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB \n"
          "6. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n"
          "7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
          "8. Determinar cuántos superhéroes tienen cada tipo de color de pelo. \n"
          "9. Listar todos los superhéroes agrupados por color de ojos.\n"
          "10. Listar todos los superhéroes agrupados por tipo de inteligencia\n"
          "11. Salir")
def ingresar_opcion() -> int:
    '''
    Ingresa un int y lo guarda en una variable para retornarla
    :return:
    '''
    opcion = int(input("\nIngrese una opcion: \n"))
    while opcion <= 0 or opcion > 11:
        opcion = int(input("Error, ingrese una opcion valida\n"))
    return opcion

def imprimir_nombre_genero_NB(list: list):
    '''
    Imprime los nombres de los heroes por genero NB
    :param list:
    :return:
    '''
    print("1. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    lista_genero = obtener_lista_de_lista_de_diccionario_con_clave_y_valor(list, "genero", "NB")
    if not lista_genero:
        print("No hay héroes con ese género.")
    else:
        print("Los héroes de género NB son:")
        for heroe in lista_genero:
            print(heroe['nombre'])

def superheroe_mas_alto_por_genero(list: list, value:str):
    '''
    Imprime el superheroe mas alto según el genero F
    :param list:
    :param opcion:
    :return:
    '''
    print(f"2/3. Recorrer la lista y determinar cuál es el superhéroe más alto de género {value}\n")
    lista = obtener_lista_de_lista_de_diccionario_con_clave_y_valor(list, "genero", value)

    diccionario = obtener_maximo_de_lista_y_clave(lista,'altura')
    print(f"El superheroe mas alto del genero {diccionario['genero']} es: {diccionario['nombre']} y mide {diccionario['altura']}")

def genero_mas_alto(list, opcion):
    '''
    Obtiene el genero mas alto
    :param list:
    :param opcion:
    :return:
    '''
    altura_mayor = None
    nombre_heroe = None
    for heroe in list:
        if opcion == 2:
            altura_float = float(heroe["altura"])
            if altura_mayor is None or altura_float > altura_mayor and heroe["genero"] == "M":
                altura_mayor = altura_float
                nombre_heroe = heroe["nombre"]
        else:
            altura_float = float(heroe["altura"])
            if altura_mayor is None or altura_float > altura_mayor and heroe["genero"] == "F":
                altura_mayor = altura_float
                nombre_heroe = heroe["nombre"]
    return nombre_heroe

def superheroe_mas_debil_por_genero(list:list, value:str):
    '''
    Obtiene el superhereo mas mas debil por genero a través del valor de una clave
    :param list:
    :param opcion:
    :return:
    '''
    print(f"4/5. Recorrer la lista y determinar cuál es el superhéroe más débil de género {value}")
    lista = obtener_lista_de_lista_de_diccionario_con_clave_y_valor(list, "genero", value)
    mensaje_error = "No hay heroes con ese genero."
    if not lista:
        print(mensaje_error)
    else:
        heroe = obtener_minimo_de_lista_y_clave(lista, "fuerza")
        print(f"El heroe mas debil por genero {heroe['genero']}: {heroe['nombre']}, su fuerza es de: {heroe['fuerza']}")

def superheroe_promedio_nb(list):
    '''
    Imprime el promedio de superheroes NB
    :param list:
    :return:
    '''
    print("\n6. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\n")
    lista_nb = obtener_lista_de_lista_de_diccionario_con_clave_y_valor(list, "genero", "NB")
    promedio = obtener_promedio_de_lista_y_clave(lista_nb, "fuerza")
    print(f"El promedio de los supeheroes de fuerza de los Superheroes NB es {promedio}")

def superheroes_tipo_color_ojos(list):
    '''
    Imprime una lista de superheroes por tipo de color de ojos
    :param list:
    :return:
    '''
    print("\n7. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n")
    lista_ojos = obtener_lista_de_lista_de_diccionario_con_clave(list, "color_ojos")
    for index in lista_ojos:
        print(index)

def superheroes_tipo_color_pelo(list):
    '''
    Obtiene una lista de superheroes por color de pelo
    :param list:
    :return:
    '''
    print("\nDeterminar cuántos superhéroes tienen cada tipo de color de pelo. \n")
    lista_ojos = obtener_lista_de_lista_de_diccionario_con_clave(list, "color_pelo")
    for index in lista_ojos:
        print(index)
        
def superheroes_enlistados_color_pelo(list):
    '''
    Imprime una lista de superheroes por color de pelo
    :param list:
    :return:
    '''
    diccionario_heroes_color_pelo = obtener_diccionario_desde_lista_de_diccionario_por_clave_valor(list, "color_pelo", "nombre")
    print("\n9. Listar todos los superhéroes agrupados por color de ojos.\n")
    for index in diccionario_heroes_color_pelo:
        print(f"{index} : {diccionario_heroes_color_pelo[index]}")

def superheroes_enlistados_inteligencia(list):
    '''
    Imprime una lista de superheroes por inteligencia
    :param list:
    :return:
    '''
    diccionario_heroes_inteligencia = obtener_diccionario_desde_lista_de_diccionario_por_clave_valor(list, "inteligencia", "nombre")
    print("\n10. Listar todos los superhéroes agrupados por tipo de inteligencia\n")
    for index in diccionario_heroes_inteligencia:
        print(f"{index} : {diccionario_heroes_inteligencia[index]}")

# GETTERS
def obtener_promedio_de_lista_y_clave(list: list, key) -> float:
    '''
    Obtiene el promedio de los valores de una clave de diccionario en una lista de diccionarios
    :param list:
    :param key:
    :return:
    '''
    suma = 0
    contador = 0
    promedio = 0
    error = "No se puede dividir por cero."
    for diccionario in list:
        suma += float(diccionario[key])
        contador += 1
    if contador > 0:
        promedio = suma / contador
    else:
        print(error)
    return promedio

def obtener_minimo_de_lista_y_clave(list: list, key) -> float:
    '''
    Obtiene el minimo de los valores de una clave de diccionario de una lista de diccionarios.
    :param list:
    :param key:
    :return:
    '''
    menor = None
    minimo = None
    for diccionario in list:
        menor_float = float(diccionario[key])
        if menor is None or menor_float < menor:
            menor = menor_float
            minimo = diccionario
    return minimo

def obtener_maximo_de_lista_y_clave(list: list, key) -> float:
    '''
    Obtiene el maximo de los valores de una clave de diccionario de una lista de diccionarios.
    :param list:
    :param key:
    :return:
    '''
    mayor = None
    maximo = None
    for diccionario in list:
        mayor_float = float(diccionario[key])
        if mayor is None or mayor_float > mayor:
            mayor = mayor_float
            maximo = diccionario
    return maximo
    
def obtener_lista_de_lista_de_diccionario_con_clave_y_valor(list: list, key, value) -> list:
    '''
    Obtiene una lista específicando la clave de diccionario y un valor equivalente entre indices
    :param list:
    :param key:
    :param value:
    :return:
    '''
    list_value = []
    for object in list:
        if object[key] == value:
            list_value.append(object)
    return list_value

def obtener_set_de_lista_de_diccionario_con_clave(list:list, key) -> set:
    '''
    Obtiene un set de una lista a través de una clave de diccionario específica
    :param list:
    :param key:
    :return:
    '''
    set_object = set()
    for index in list:
        set_object.add(index[key])
    return set_object

def obtener_lista_de_lista_de_diccionario_con_clave(list:list, key) -> list:
    '''
    Obtiene una lista a través de un set y una clave específica
    :param list:
    :param key:
    :return:
    '''
    lista_object = []
    set_object = obtener_set_de_lista_de_diccionario_con_clave(list, key)
    for index in set_object:
        contador = 0
        for indice in list:
            if indice[key] == index:
                contador += 1
        nuevos_valores = {index, contador}
        lista_object.append(nuevos_valores)
    return lista_object

# "9. Listar todos los superhéroes agrupados por color de ojos.\n"

def obtener_diccionario_desde_lista_de_diccionario_por_clave_valor(list:list, key, value) -> dict:
    '''
    Obtiene un diccionario de una lista, una clave específica y un valor 
    :param list:
    :param key:
    :param value:
    :return:
    '''
    set_object = obtener_set_de_lista_de_diccionario_con_clave(list, key)
    diccionario = {}
    for index_set in set_object:
        lista = []
        for indice_list in list:
            if indice_list[key] == index_set:
                lista.append(indice_list[value])
        diccionario[index_set] = lista
    return diccionario