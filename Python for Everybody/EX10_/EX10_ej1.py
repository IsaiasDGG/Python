print("ejercicio 1, cap 10.")
#Ejercicio 1: Revisa el programa anterior de este modo: Lee y analiza las líneas “From” y extrae las direcciones de correo. Cuenta el número de mensajes de cada persona utilizando un diccionario. Después de que todos los datos hayan sido leídos, imprime la persona con más envíos, creando una lista de tuplas (contador, email) del diccionario. Después ordena la lista en orden inverso e imprime la persona que tiene más envíos.


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
        correo=line[1]
        #correo_1=correo.split("@")
        #dom=correo_1[1]
        t[correo]=t.get(correo,0)+1
        
#print("cantidad de dominios usados\n",t)

li=list()
for k,v in list(t.items()):##crear lista valor, clave
    li.append((v,k))

print(max(li))##imprime valor maximo

li.sort(reverse=True)###ordena lista de mayor a menor.

for v,k in li:
    print(v,k)

#for k,v in t.items():
 #   if count is None or count<v:
  #      email=k
   #     count=v
#print("dominio más usado: ", email, "usado", count, "veces en total")