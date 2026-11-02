print("ejercicio 1. cap 8.13")
#Ejercicio 1: Escribe una función llamada recortar que toma una lista y la modifica, removiendo el primer y último elemento, y regresa None. Después escribe una función llamada medio que toma una lista y regresa una nueva lista que contiene todo excepto el primero y último elementos.

def recortar (x):
    del x[0] 
    del x[len(x)-1:]
    
t=list() #crea lista sin elementos.

while True:
    n=input("ingrese un número:\n")
    if n == "fin": break
    try:
        ent=int(n)
        t.append(ent)
    except:
        print("no es un número valido,\n intenta de nuevo")
        continue
print("elementos de la lista",t)

#crea nueva lista
medio=t[1:len(t)-1]
print("medio:", medio, "de lista", t)

#modifica la lista
t2=recortar(t)
print( "lista t2",t2)
print("lista t1",t)


    