print("examen 8.5")
# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

#codigo para ingresar archivo sin errores
while True:
    fname=input("nombre del archivo:")
    if fname=="fin": break
    try:
        texto=open(fname)
        print("texto encontrado")
        break
    except:
        print ("texto no encontrado, pruebe de nuevo.")
        continue

        
t1=list()
for linea in texto:
    linea=linea.rstrip()
    if linea.startswith("From:"):continue
    elif linea.startswith("From"):
        t=linea.split()
        print(t[1])
        t1.append(t[1])

count=len(t1)
print("There were",count, "lines in the file with From as the first word")
