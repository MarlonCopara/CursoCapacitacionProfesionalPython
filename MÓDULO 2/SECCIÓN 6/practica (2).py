try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")
    