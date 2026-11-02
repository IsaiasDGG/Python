print("ejercicio 2, cap 9.")
#Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo dependiendo del día de la semana en que se recibió. Para hacer esto busca las líneas que comienzan con “From”, después busca por la tercer palabra y mantén un contador para cada uno de los días de la semana. Al final del programa imprime los contenidos de tu diccionario (el orden no importa).

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
####
count=None
t=dict()

for line in file:
    line=line.rstrip()
    
    if line.startswith("From "):
        line=line.split()
        t[line[2]]=t.get(line[2],0)+1
        
print("cantidad de días encontrados\n",t)

for k,v in t.items():
    print(k,v)
    