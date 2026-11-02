print("examen 02, cap. 15")
#Organizaciones de conteo
#Esta aplicación leerá los datos del buzón de correo (mbox.txt) y contará el número de mensajes de correo electrónico por organización (es decir, nombre de dominio de la dirección de correo electrónico) utilizando una base de datos con el siguiente esquema para mantener los recuentos.
#CREAR TABLA Counts (org TEXTO, count ENTERO)
#Una vez que haya ejecutado el programa en mbox.txt, cargue el archivo de base de datos resultante arriba para su evaluación.
#Si ejecuta el programa varias veces para realizar pruebas o con archivos diferentes, asegúrese de vaciar los datos antes de cada ejecución.
#Puedes usar este código como punto de partida para tu aplicación: http://www.py4e.com/code3/emaildb.py .
#El archivo de datos para esta aplicación es el mismo que en las tareas anteriores: http://www.py4e.com/code3/mbox.txt .
#Dado que el código de ejemplo utiliza una instrucción UPDATE y guarda los resultados en la base de datos a medida que se lee cada registro en el bucle, el procesamiento de todos los datos puede tardar varios minutos. La instrucción COMMIT garantiza que todos los datos se guarden completamente en el disco cada vez que se ejecuta.
#El programa puede acelerarse considerablemente si se realiza la operación de confirmación fuera del bucle. En cualquier programa de base de datos, existe un equilibrio entre la cantidad de operaciones que se ejecutan entre confirmaciones y la importancia de no perder los resultados de las operaciones que aún no se han confirmado.

import sqlite3

conn=sqlite3.connect("correos.sqlite")
cur= conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts(org TEXTO, count INTEGER)")

while True:
    
    nombre_archivo=input("Ingresa nombre del archivo:\n")
    try:
        archivo_a_usar=open(nombre_archivo)
        print("leyendo archivo", nombre_archivo)
        break
    except:
        print ("archivo no encontrado")
        exit()

for linea in archivo_a_usar:
    if linea.startswith("From: "):
        partes=linea.split()
        correo=partes[1]
        partes_2=correo.split("@")
        orgs=partes_2[1]
    
    ##### relevante para examen ####
        cur.execute("SELECT count FROM Counts WHERE org=?",(orgs,))
        row=cur.fetchone()
        if row is None: 
            cur.execute("INSERT INTO Counts (org, count) VALUES(?,1)", (orgs,))
        else:
            cur.execute("UPDATE Counts SET count= count +1 WHERE org=?",(orgs,))

conn.commit()

stabla="SELECT org, count FROM COUNTS"

for row in cur.execute(stabla):
    print(str(row[0]), row[1])

cur.close()
    