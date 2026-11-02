print("Ejerciccio 2, cap 7.11")
#Ejercicio 2: Escribe un programa que solicite un nombre de archivo y después lea ese archivo buscando las líneas que tengan la siguiente forma: X-DSPAM-Confidence: 0.8475 **Cuando encuentres una línea que comience con “X-DSPAM-Confidence:” ponla aparte para extraer el número decimal de la línea. Cuenta esas líneas y después calcula el total acumulado de los valores de “spam-confidence”. Cuando llegues al final del archivo, imprime el valor medio de “spam confidence”.

nfile=input("ingrese el nombre del archivo con el que desea trabajar por favor: ")

try: 
    ofile=open(nfile)
    print("archivo encontrado")
except:
    print("archivo no encontrado, ingrese de nuevo por favor")
    exit()

total=0
clinea=0

for line in ofile:
    if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        pos=line.find(":")
        num=float(line[pos+1:])
        #print(num)
        #print(type(num))
        total=total+num
        clinea=clinea+1
print("total de valores: ",total)
print("total lineas validas: ",clinea)
print("valor medio: ",total/float(clinea))



    
        