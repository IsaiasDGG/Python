print("ejercicio 5, cap 9.")
#Ejercicio 5: Este programa almacena el nombre del dominio (en vez de la dirección) desde donde fue enviado el mensaje en vez de quién envió el mensaje (es decir, la dirección de correo electrónica completa). Al final del programa, imprime el contenido de tu diccionario.

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
        correo_1=correo.split("@")
        dom=correo_1[1]
        t[dom]=t.get(dom,0)+1
        
print("cantidad de dominios usados\n",t)

for k,v in t.items():
    if count is None or count<v:
        email=k
        count=v
print("dominio más usado: ", email, "usado", count, "veces en total")