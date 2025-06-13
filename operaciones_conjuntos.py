#Recibo un DNI como string y devuelve una lista de dígitos únicos.
def generar_conjunto_unico(dni_str):
    digitos_unicos = []
    for digito in dni_str:
        if int(digito) not in digitos_unicos:
            digitos_unicos.append(int(digito))
    return digitos_unicos

# Calcula la unión de dos listas. Devuelve una nueva lista con los elementos de ambas, sin repetir.
def union(lista_a, lista_b):
    resultado_union = lista_a.copy() # Empezamos con todos los elementos de A
    for elemento in lista_b:
        if elemento not in resultado_union:
            resultado_union.append(elemento)
    return resultado_union

# Calcula la intersección de dos listas. Devuelve los elementos que están
#     presentes en AMBAS listas.
def interseccion(lista_a, lista_b):
    resultado_interseccion = []
    for elemento in lista_a:
        if elemento in lista_b:
            resultado_interseccion.append(elemento)
    return resultado_interseccion

    # Devuelve los elementos que están en la
    # lista A pero NO en la lista B.
def diferencia(lista_a, lista_b):
    resultado_diferencia = []
    for elemento in lista_a:
        if elemento not in lista_b:
            resultado_diferencia.append(elemento)
    return resultado_diferencia

 # La diferencia simétrica es la unión de las dos diferencias
def diferencia_simetrica(lista_a, lista_b):
    diff_a_b = diferencia(lista_a, lista_b)
    diff_b_a = diferencia(lista_b, lista_a)
    resultado_simetrica = union(diff_a_b, diff_b_a)
    return resultado_simetrica


#Evalúa si la lista A es subconjunto de la lista B. Todos los elementos de A deben estar en B.
def es_subconjunto(lista_a, lista_b):
    for elemento in lista_a:
        if elemento not in lista_b:
            return False # Si encontramos uno que no está, ya es falso
    return True # Si el bucle termina, es que todos estaban


#Devuelve True si el año es bisiesto, False en caso contrario.
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


#Devuelve una lista de tuplas con todos los pares posibles.
def producto_cartesiano(conjunto_a, conjunto_b):
    resultado_producto = []
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            resultado_producto.append((elemento_a, elemento_b))
    return resultado_producto