print("Examen  N°2 Cap 13_json")
#En esta tarea, escribirás un programa en Python similar a http://www.py4e.com/code3/opengeo.py . El programa solicitará una ubicación, se conectará a un servicio web, recuperará el JSON del servicio, analizará esos datos y obtendrá el primer código de ubicación (plus_code) del JSON. Un código de ubicación abierta (Open Location Code) es un identificador textual que funciona como una dirección basada en la ubicación.
#Puntos finales de la API
#Para completar esta tarea, deberá utilizar este punto final de la API que contiene un subconjunto estático de los datos de OpenStreetMap.
#http://py4e-data.dr-chuck.net/opengeo?
#Esta API no tiene límite de solicitudes, por lo que puede realizar pruebas con la frecuencia que desee. Si accede a la URL sin parámetros, recibirá la respuesta "No hay dirección...".
#Para llamar a la API, debe proporcionar la dirección que está solicitando como parámetro q=, la cual debe estar codificada correctamente en formato URL utilizando la función urllib.parse.urlencode() como se muestra en http://www.py4e.com/code3/opengeo.py

import urllib.request, urllib.parse, urllib.error
import json
import ssl


##ignora errores de certificado SSL
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

##servidor que se usará para el examen.
serviceurl="http://py4e-data.dr-chuck.net/opengeo?"

while True:
    address=input ("ingrese dirección:\n")
    if address == "fin" : exit()
    try:
        address=address.strip()
        parametros=dict()
        parametros["q"]=address
        
        url=serviceurl+urllib.parse.urlencode(parametros)
        
        print("recibiendo información de: ", url)
        uh=urllib.request.urlopen(url, context=ctx)##open link.
        data=uh.read().decode()##lectura de toda la data.
        print("recibiendo", len(data),"caracteres")
        
        info= json.loads(data)##importante hace que se lea como json//dicccionario.
        break
        
    except:
        print("error, reintentar")
        exit()

#examen!!!


print(json.dumps(info["features"][0]["properties"]["plus_code"], indent=4))


exit()