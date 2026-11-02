print("examen 9.4")
#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#open archivo
while True:
    fname=input("nombre del archivo:")
    if fname=="fin": break
    try:
        texto=open(fname)
        print("texto encontrado")
        break
    except:
        print ("texto no encontrado, pruebe de nuevo.")
        contine    

#definiciones previas

book=dict()
word=None
word_count=None

for line in texto:
    if line.startswith("From "):
        email=line.split()
        #print(email)
        #print(email[1])##hasta aqui funciona.
        book[email[1]]=book.get(email[1],0)+1

        
for x,y in book.items():
    if word_count is None or y >word_count:
        word=x
        word_count=y

print(word,word_count)
        