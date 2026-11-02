print("Examen  N°1 Cap 13_XML")
#El programa solicitará una URL, leerá los datos XML de esa URL usando urllib y luego analizará y extraerá el número de comentarios de los datos XML, calculando la suma de los números en el archivo.
#Para esta tarea, les proporcionamos dos archivos. Uno es un archivo de ejemplo con la suma para que realicen sus pruebas, y el otro contiene los datos reales que deben procesar.
#Datos de muestra: http://py4e-data.dr-chuck.net/comments_42.xml (Suma=2553)
#Datos reales: http://py4e-data.dr-chuck.net/comments_2421220.xml (La suma termina en 69)
#No es necesario guardar estos archivos en tu carpeta, ya que tu programa leerá los datos directamente desde la URL. Nota: Cada estudiante tendrá una URL de datos distinta para la tarea; por lo tanto, utiliza únicamente tu propia URL de datos para el análisis.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


##ignora errores de certificado SSL
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    url=input ("ingrese link a analizar:\n")
    if url == "fin" : exit()
    try:
        print("recibiendo información de:",url)
        uh=urllib.request.urlopen(url)##open link.
        data=uh.read()##lectura de toda la data.
        print("recibiendo", len(data),"caracteres")
        tree=ET.fromstring(data)##importante hace que se lea como XML.
        break
    except:
        print("error, reintentar")
        exit()

#examen!!!
lst=tree.findall("comments/comment")##busca las etiquetas.
nums=list()

for n in lst:
    #print("contenido:", n.find("count").text)
    nums.append(int(n.find("count").text))
    #print (n)

print(">>>>>lista",nums)
print("Total\n",sum(nums))

exit()
