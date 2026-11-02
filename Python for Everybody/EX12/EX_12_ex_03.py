print("examen 03 cap 12.")
#En esta tarea, escribirás un programa en Python que amplía el código de http://www.py4e.com/code3/urllinks.py . El programa utilizará urllib para leer el HTML de los archivos de datos que se indican a continuación, extraerá los valores href= de las etiquetas de anclaje, buscará una etiqueta que se encuentre en una posición específica con respecto al primer nombre de la lista, seguirá ese enlace y repetirá el proceso varias veces, informando del último nombre encontrado.

#Para esta tarea, proporcionamos dos archivos. Uno es un archivo de ejemplo donde les damos el nombre para sus pruebas y el otro son los datos reales que necesitan procesar para la tarea.

#Ejemplo de problema: Comience en http://py4e-data.dr-chuck.net/known_by_Fikret.html. Encuentre el enlace en la posición 3 (el primer nombre es 1). Siga ese enlace. Repita este proceso 4 veces. La respuesta es el apellido que obtenga.
#Secuencia de nombres: Fikret Montgomery Mhairade Butchi Anayah.
#Apellido en la secuencia: Anayah.
#Problema real: Comience en: http://py4e-data.dr-chuck.net/known_by_Medina.html
#Encuentre el enlace en la posición 18 (el primer nombre es 1). Siga ese enlace. Repita este proceso 7 veces. La respuesta es el último nombre que obtenga.
#Sugerencia: El primer carácter del nombre de la última página que cargará es: V
#Estrategia
#Las páginas web modifican la altura entre los enlaces y ocultan la página después de unos segundos para dificultar la realización de la tarea sin escribir un programa en Python. Sin embargo, con un poco de esfuerzo y paciencia, se pueden superar estos intentos de complicar la tarea. Pero ese no es el objetivo. El objetivo es escribir un programa ingenioso en Python para resolver el problema.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import time

##ignora errores de certificado SSL
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    url=input ("ingrese link a analizar:\n")
    pos=input("ingrese posición:\n")
    cant=input("ingrese cantidad de repeticiones\n")
    if url == "fin" or pos =="fin" or cant=="fin": exit()
    try:
        pos=int(pos)
        cant=int(cant)
        break
    except:
        print("error, reintentar")
        exit()

#recuperar todas las etiquetas
#t=list()


#for etiqueta in etiquetas[pos-1:pos]:
    #print('ETIQUETA:', etiqueta)
    #print('URL:', etiqueta.get('href', None))
    #print('Contenido:', etiqueta.contents[0])
    #print('Atributos:', etiqueta.attrs)
    #n=int(etiqueta.contents[0])
    #t.append(n)





while cant >0:
    html= urllib.request.urlopen(url,context=ctx).read()
    sopa=BeautifulSoup(html,"html.parser")
    etiquetas=sopa("a")
    print(url,"cantidad",cant)
    for etiqueta in etiquetas[pos-1:pos]:
        url=etiqueta.get('href', None)
    cant= cant-1
    print (">>>>>",url,"cantidad",cant)
    time.sleep(0.5)
    


for etiqueta in etiquetas[pos-1:pos]:
    print(etiqueta.contents[0])