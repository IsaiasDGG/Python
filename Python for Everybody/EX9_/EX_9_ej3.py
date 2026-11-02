print("ejercicio 3, cap 9.")
#Ejercicio 3: Escribe un programa para leer a través de un historial de correos, construye un histograma utilizando un diccionario para contar cuántos mensajes han llegado de cada dirección de correo electrónico, e imprime el diccionario.

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
        t[line[1]]=t.get(line[1],0)+1
        
#print("cantidad de emails\n",t)

for k,v in t.items():
    if count is None or count<v:
        email=k
        count=v
        

print("email más repecito\n", email,count)
    