from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo:", ccnt)
	print("Líneas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
    