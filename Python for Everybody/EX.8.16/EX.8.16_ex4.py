print("ejercicio 4,cap 8.16")
# Ejercicio 4: Escribir un programa para abrir el archivo romeo.txt y leerlo línea por línea. Para cada línea, dividir la línea en una lista de palabras utilizando la función split. Para cada palabra, revisar si la palabra ya se encuentra previamente en la lista. Si la palabra no está en la lista, agregarla a la lista. Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden alfabético.

texto=open("romeo.txt")
t=list()
for linea in texto:
    palabra=linea.split()
    for pf in palabra:
        if pf in t: continue
        t.append(pf)

ori=t[:]
t.sort()
#print("palbras sin orden\n",ori)
print("orden alf.\n",t)

    