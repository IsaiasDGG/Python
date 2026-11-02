print("examen cap 11")
#Para esta tarea, les proporcionamos dos archivos. Uno es un archivo de ejemplo con la suma para que realicen sus pruebas, y el otro contiene los datos reales que deben procesar. Datos de ejemplo: http://py4e-data.dr-chuck.net/regex_sum_42.txt (Hay 90 valores con una suma de 445833) Datos reales: http://py4e-data.dr-chuck.net/regex_sum_2421216.txt (Hay 100 valores y la suma finaliza en 752)
#aperturar libros.
while True:
    fname=input("coloce nombre del archivo: ")
    if fname=="fin": exit()
    try:
        file=open(fname)
        print("Archivo encontrado.")
        break
    except:
        print("archivo no encontrado.")
        exit()

##examen.
t=list()
import re

for line in file:
    line.rstrip()
    numeros=re.findall("([0-9]+)",line)
    if len(numeros) == 0:continue
    for num in numeros:
        n=int(num)
        t.append(n)

#print(t)

print("sumatoria",sum(t))


    

