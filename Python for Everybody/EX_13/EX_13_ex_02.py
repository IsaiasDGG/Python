print("Examen  N°1 Cap 13_json")
#En esta tarea, escribirás un programa en Python similar a http://www.py4e.com/code3/json2.py . El programa te pedirá una URL, leerá los datos JSON de esa URL usando urllib y luego analizará y extraerá el número de comentarios de los datos JSON, calculará la suma de los números en el archivo e ingresará la suma a continuación:
#Para esta tarea, les proporcionamos dos archivos. Uno es un archivo de ejemplo con la suma para que realicen sus pruebas, y el otro contiene los datos reales que deben procesar.
#Datos de muestra: http://py4e-data.dr-chuck.net/comments_42.json (Suma=2553)
#Datos reales: http://py4e-data.dr-chuck.net/comments_2421221.json (La suma termina en 48)

import urllib.request, urllib.parse, urllib.error
import json
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
        uh=urllib.request.urlopen(url, context=ctx)##open link.
        data=uh.read().decode()##lectura de toda la data.
        print("recibiendo", len(data),"caracteres")
        
        info= json.loads(data)##importante hace que se lea como json//dicccionario.
        break
        
    except:
        print("error, reintentar")
        exit()

#examen!!!

nums=list()
print("usuarios", len(info["comments"]))
#print(info["comments"])

for elemento in info["comments"]:
    #print(elemento["count"])
    nums.append(int(elemento["count"]))

print(">>>>>lista",nums)
print("Total\n",sum(nums))

exit()
