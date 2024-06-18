from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    print("El archivo no pudo ser abierto:", strerror(exc.errno))
    