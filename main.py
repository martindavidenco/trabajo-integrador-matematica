# main.py

# Importamos nuestro módulo y ahora también 'datetime' para las edades
import operaciones_conjuntos as ops
from datetime import datetime

def procesar_dnis():
    """Función para toda la lógica de la Parte A."""
    print("--- Parte A: Operaciones con DNIs ---")
    
    dni_A_str = "22775850"
    dni_B_str = "42304272"
    print(f"DNI A: {dni_A_str}\nDNI B: {dni_B_str}\n")

    conjunto_A = ops.generar_conjunto_unico(dni_A_str)
    conjunto_B = ops.generar_conjunto_unico(dni_B_str)
    
    # Corregí este print para que sea más claro
    print(f"Conjunto A: {conjunto_A}")
    print(f"Conjunto B: {conjunto_B}")
    print("-" * 20)

    # --- CORRECCIÓN AQUÍ ---
    # Ahora llamamos a las funciones con sus nuevos nombres (sin "_manual")
    union = ops.union(conjunto_A, conjunto_B)
    interseccion = ops.interseccion(conjunto_A, conjunto_B)
    diferencia = ops.diferencia(conjunto_A, conjunto_B)
    d_simetrica = ops.diferencia_simetrica(conjunto_A, conjunto_B)

    print(f"Unión: {union}")
    print(f"Intersección: {interseccion}")
    print(f"Diferencia A-B: {diferencia}")
    print(f"Diferencia Simétrica: {d_simetrica}")
    print("-" * 20)
    
    print("Evaluando Expresiones Lógicas:")
    # --- CORRECCIÓN AQUÍ ---
    if ops.es_subconjunto(conjunto_A, conjunto_B):
        print("Expresión 1: Se cumple. A está contenido en B.")
    else:
        print("Expresión 1: No se cumple. A NO está contenido en B.")

    if len(d_simetrica) > 3:
        print("Expresión 2: Se cumple. Hay una alta diferencia (más de 3 elementos).")
    else:
        print("Expresión 2: No se cumple. La diferencia no es alta.")

def procesar_anios():
    """Función para toda la lógica de la Parte B."""
    print("\n--- Parte B: Operaciones con Años de Nacimiento ---")
    
    anios_nacimiento = [1999, 2003]
    print(f"Años de nacimiento: {anios_nacimiento}")
    print("-" * 20)
    
    pares = 0
    impares = 0
    for anio in anios_nacimiento:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Cantidad de nacidos en año par: {pares}")
    print(f"Cantidad de nacidos en año impar: {impares}")
    print("-" * 20)

    todos_son_z = True
    for anio in anios_nacimiento:
        if anio <= 2000:
            todos_son_z = False
            break
    
    if todos_son_z:
        print("Condición 'Grupo Z': Se cumple. ¡Todos los integrantes nacieron después del 2000!")
    else:
        print("Condición 'Grupo Z': No se cumple. Al menos un integrante nació en o antes del 2000.")
    print("-" * 20)

    alguno_bisiesto = False
    
    for anio in anios_nacimiento:
        if ops.es_bisiesto(anio):
            print(f"¡Tenemos un año especial! El año {anio} es bisiesto.")
            alguno_bisiesto = True
    if not alguno_bisiesto:
        print("Ningún integrante nació en un año bisiesto.")
    print("-" * 20)

    print("Cálculo del Producto Cartesiano (Años x Edades):")
    anio_actual = datetime.now().year
    edades_actuales = []
    for anio in anios_nacimiento:
        edad = anio_actual - anio
        if edad not in edades_actuales:
            edades_actuales.append(edad)
    
    print(f"Conjunto de años: {anios_nacimiento}")
    print(f"Conjunto de edades: {edades_actuales}")

    # --- CORRECCIÓN AQUÍ ---
    producto = ops.producto_cartesiano(anios_nacimiento, edades_actuales)
    print("El producto cartesiano es el conjunto de todos los pares (año, edad) posibles:")
    print(producto)

# --- Ejecución del Programa ---
procesar_dnis()
procesar_anios()