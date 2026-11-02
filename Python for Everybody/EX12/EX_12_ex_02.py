print("examen 02 cap 12.")
#Extracción de números de HTML con BeautifulSoup En esta tarea, escribirás un programa en Python similar a http://www.py4e.com/code3/urllink2.py . El programa utilizará urllib para leer el HTML de los archivos de datos que se indican a continuación, analizar los datos, extraer los números y calcular la suma de los números en el archivo.
#
#Para esta tarea, les proporcionamos dos archivos. Uno es un archivo de ejemplo con la suma para que realicen sus pruebas, y el otro contiene los datos reales que deben procesar.
#
#Datos de muestra: http://py4e-data.dr-chuck.net/comments_42.html (Suma=2553)
#Datos reales: http://py4e-data.dr-chuck.net/comments_2421218.html (La suma termina en 14)
#Debes encontrar todas las etiquetas <span> en el archivo, extraer los números de cada etiqueta y sumarlos.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

##ignora errores de certificado SSL
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    url=input ("ingrese link a analizar:\n")
    if url == "fin": exit()
    try:
        html= urllib.request.urlopen(url,context=ctx).read()
        sopa=BeautifulSoup(html,"html.parser")
        break
    except:
        print("link no encontrado")
        exit()

#recuperar todas las etiquetas
t=list()

etiquetas=sopa("span")
for etiqueta in etiquetas:
    print('ETIQUETA:', etiqueta)
    #print('URL:', etiqueta.get('href', None))
    print('Contenido:', etiqueta.contents[0])
    #print('Atributos:', etiqueta.attrs)
    n=int(etiqueta.contents[0])
    t.append(n)


#print("suma solicitada\n",sum(t))

    