print("Ejerciccio 1, cap 7.11")
#Ejercicio 1: Escribe un programa que lea un archivo e imprima su contenido (línea por línea), todo en mayúsculas.

opfile=open("mbox-short.txt")
for linea in opfile:
    linea=linea.upper().rstrip()
    print(linea)
    