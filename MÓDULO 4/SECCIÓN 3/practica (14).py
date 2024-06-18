from os import strerror

srcname = input("Ingresa el nombre del archivo fuente: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Ingresa el nombre del archivo destino: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()
    