"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    results = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            char = columns[0]
            value = int(columns[1])
            if char in results:
                current_max, current_min = results[char]
                results[char] = (max(current_max, value), min(current_min, value))
            else:
                results[char] = (value, value)

    results_list = [(char, max_val, min_val) for char, (max_val, min_val) in results.items()]
    results_list.sort(key=lambda x: x[0])
    return results_list