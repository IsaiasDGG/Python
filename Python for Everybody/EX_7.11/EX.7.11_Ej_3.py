print("Ejerciccio 3, cap 7.11")
#Ejercicio 3: Algunas veces cuando los programadores se aburren o
#quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
#a su programa. Modifica el programa que pregunta al usuario por el
#nombre de archivo para que imprima un mensaje divertido cuando el
#usuario escriba “na na boo boo” como nombre de archivo. El programa
#debería funcionar normalmente para cualquier archivo que exista o no
#exista. Aquí está un ejemplo de la ejecución del programa”.

nfile=input("ingrese el nombre del archivo con el que desea trabajar por favor: ")
if nfile == "na na boo boo":
    print("NA NA BOO BOO PARA TI - te he atrapado")
    exit()
    
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



    
        