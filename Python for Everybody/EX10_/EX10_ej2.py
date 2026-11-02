print("ejercicio 2, cap 10.")
#Ejercicio 2: Este programa cuenta la distribución de la hora del día para cada uno de los mensajes. Puedes extraer la hora de la línea “From” buscando la cadena horaria y luego dividiendo la cadena en partes utilizando el carácter colon. Una vez que hayas acumulado las cuentas para cada hora, imprime las cuentas, una por línea, ordenadas por hora tal como se muestra debajo.


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

#### inicio.
count=None
email=None
t=dict()

###apertura de lineas del libro++ diccionario.
for line in file:
    line=line.rstrip()
    
    if line.startswith("From "):
        line=line.split()
        #print(line)
        tiempo=line[5]
        #print (tiempo)
        hh=tiempo.split(":")
        hora=hh[0]
        t[hora]=t.get(hora,0)+1

##convierto dic a lista para trabajar en ella.
ls=list()
for k,v in t.items():
    ls.append((k,v))

ls.sort()

for k,v in ls:
    print(k,v)