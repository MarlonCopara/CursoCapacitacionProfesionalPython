from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    