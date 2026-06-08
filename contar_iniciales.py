# Escriba la función contar_iniciales(oracion) que retorne
# un diccionario asociando a cada letra la cantidad de veces
# que aparece al principio de una palabra.


# Esta version de la función usa el metodo string.split() para separar las palabras y luego obtener la primera letra de cada una
def contar_iniciales(frase):
    resultado = dict() # Inicializamos un diccionario vacio
    for palabra in frase.lower().split(): # Separamos cada una de las palabras
        inicial = palabra[0]
        if inicial not in resultado:
            resultado[inicial] = 0 # Añadimos las letras que no estén de antes en el diccionario, inicializando un contador en cero
        resultado[inicial] += 1 # Incrementamos el contador cada vez que nos encontremos esa inicial
    return resultado

# Esta version de la función recorre cada caracter, ocupando una marca/bandera/flag de tipo bool para recordar cuando el último caracter encontrado fue un espacio,
# y por lo tanto el caracter actual sería una inicial que hay que contar.
def contar_iniciales_v2(frase):
    resultado = {} # Inicializamos un diccionario vacio
    flag = True
    for caracter in frase.lower():
        if caracter == " ":
            flag = True
            continue
        if flag: # Esta es la inicial de una palabra
            if caracter not in resultado:
                resultado[caracter] = 1 # Añadimos las letras que no estén de antes en el diccionario, con valor uno
            else:
                resultado[caracter] += 1 # Incrementamos el contador cada vez que nos volvamos a encontrar esa inicial
        flag = False
    return resultado

# Esta version usa el metodo string.title() que pone en mayúscula la inicial de cada palabra y luego cuenta solo las mayúsculas.
def contar_iniciales_v3(frase):
    frase = frase.title()
    resultado = dict()
    for caracter in frase:
        if caracter >= "A" and caracter <= "Z": # Si la letra está entre la A y la Z mayúscula
            if caracter not in resultado:
                resultado[caracter] = 0
            resultado[caracter] += 1
    return resultado

# Esta versión de la función recorre cada caracter hasta encontrar un espacio. En ese caso, cuenta el caracter siguiente y avanza 2.
# Dado que la cantidad de iteraciones depende de la cantidad de espacios, aquí usamos un ciclo while.
# Asunciones:
# - Que el primer caracter es letra
# - Que los espacios están de a uno
def contar_iniciales_v4(frase):
    frase = frase.lower()
    if frase == "": # El resto de la funcion no está preparada para ercibir un string vacío, así que lo ponemos como caso aparte
        return({})
    resultado = {frase[0]: 1} # Inicializamos un diccionario solo con la primera inicial
    i = 0
    while i < len(frase):
        if frase[i] == " ": # Si hallamos un espacio, la siguiente es inicial
            if frase[i + 1] not in resultado:
                resultado[frase[i + 1]] = 0
            resultado[frase[i + 1]] += 1
            i += 2 # Nos saltamos el espacio y la inicial
        else:
            i += 1 # avanzamos un caracter, para buscar el siguiente espacio
    return resultado

# Esta versión arma primero una lista con todas las inciales (con las repeticiones que corresponda)
# y luego usa el método list.count() para obtener la cantidad de veces que se repite.
def contar_iniciales_v5(frase):
    iniciales = []
    for palabra in frase.lower().split():
        iniciales.append(palabra[0])
    resultado = dict()
    for inicial in iniciales:
        resultado[inicial] = iniciales.count(inicial)
        # Nótese que esta asignación se hace una vez por cada elemento de la lista,
        # por lo que los valores asociados a las iniciales que se repitan se irán sobreescribiendo con el mismo valor.
    return resultado

# Igual a la anterior, pero usando la técnica de 'list comprehension' (no es parte de la materia del curso, pero lo dejo como curiosidad)
def contar_iniciales_v5_abreviada(frase):
    iniciales = [palabra[0] for palabra in frase.lower().split()]
    return dict([(inicial, iniciales.count(inicial)) for inicial in iniciales])



print(contar_iniciales('El elefante avanza hacia Asia'))
# Debería mostrar {'e': 2, 'h': 1, 'a': 2}

print(contar_iniciales('Varias vacas vuelan sobre Venezuela'))
# Debería mostrar {'s': 1', 'v': 4}
