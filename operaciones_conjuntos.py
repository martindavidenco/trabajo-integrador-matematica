# operaciones_conjuntos.py

def generar_conjunto_unico(dni_str):
    """
    Recibe un DNI como string y devuelve una lista de dígitos únicos (sin repetir).
    """
    digitos_unicos = []
    for digito in dni_str:
        if int(digito) not in digitos_unicos:
            digitos_unicos.append(int(digito))
    return digitos_unicos

def union(lista_a, lista_b):
    """
    Calcula la unión de dos listas. Devuelve una nueva lista con los elementos
    de ambas, sin repetir.
    """
    resultado_union = lista_a.copy() # Empezamos con todos los elementos de A
    for elemento in lista_b:
        if elemento not in resultado_union:
            resultado_union.append(elemento)
    return resultado_union

def interseccion(lista_a, lista_b):
    """
    Calcula la intersección de dos listas. Devuelve los elementos que están
    presentes en AMBAS listas.
    """
    resultado_interseccion = []
    for elemento in lista_a:
        if elemento in lista_b:
            resultado_interseccion.append(elemento)
    return resultado_interseccion

def diferencia(lista_a, lista_b):
    """
    Calcula la diferencia (A - B). Devuelve los elementos que están en la
    lista A pero NO en la lista B.
    """
    resultado_diferencia = []
    for elemento in lista_a:
        if elemento not in lista_b:
            resultado_diferencia.append(elemento)
    return resultado_diferencia

def diferencia_simetrica(lista_a, lista_b):
    """
    Calcula la diferencia simétrica. Son los elementos que están en A o en B,
    pero no en ambos.
    """
    diff_a_b = diferencia(lista_a, lista_b)
    diff_b_a = diferencia(lista_b, lista_a)
    # La diferencia simétrica es la unión de las dos diferencias
    resultado_simetrica = union(diff_a_b, diff_b_a)
    return resultado_simetrica

def es_subconjunto(lista_a, lista_b):
    """
    Evalúa si la lista A es subconjunto de la lista B.
    Todos los elementos de A deben estar en B.
    """
    for elemento in lista_a:
        if elemento not in lista_b:
            return False # Si encontramos uno que no está, ya es falso
    return True # Si el bucle termina, es que todos estaban

def es_bisiesto(anio):
    """
    Devuelve True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def producto_cartesiano(conjunto_a, conjunto_b):
    """
    Calcula el producto cartesiano entre dos listas (A x B).
    Devuelve una lista de tuplas con todos los pares posibles.
    """
    resultado_producto = []
    for elemento_a in conjunto_a:
        for elemento_b in conjunto_b:
            resultado_producto.append((elemento_a, elemento_b))
    return resultado_producto