print("examen 01 capitulo 12.")
#Explorando el Protocolo de Transporte de Hipertexto
#
#Debes recuperar el siguiente documento utilizando el protocolo HTTP de forma que puedas examinar los encabezados de respuesta HTTP.
#
#http://data.pr4e.org/intro-short.txt
#Existen tres maneras de recuperar esta página web y examinar los encabezados de respuesta:

#Opción recomendada: Modifique el programa socket1.py para recuperar la URL anterior e imprimir los encabezados y los datos. Asegúrese de modificar el código para recuperar la URL anterior, ya que los valores son diferentes para cada URL.
#Abra la URL en un navegador web con una consola de desarrollador o FireBug y examine manualmente los encabezados que se devuelven.
#Introduzca los valores del encabezado en cada uno de los campos siguientes y pulse "Enviar".


import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    datos=mysock.recv(512)
    if len(datos)<1: break
    print(datos.decode(),"end=")

mysock.close()