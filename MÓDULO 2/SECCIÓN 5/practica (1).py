# Una función que verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Una lista de filas que representan el Sudoku.
rows = [ ]
for r in range(9):

ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):


# Comprobar si todas las columnas son correctas.
if ok:
    for c in range(9):


# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for r in range(0, 9, 3):


# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")
    