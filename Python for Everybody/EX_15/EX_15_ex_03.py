print("examen n°3, cap 15")
#Esta aplicación leerá un archivo de exportación de iTunes en formato CSV y generará una base de datos correctamente normalizada con esta estructura:
 #   CREAR TABLA Artista (
  #  id ENTERO NO NULO CLAVE PRIMARIA AUTOINCREMENTO ÚNICO,
   # nombre TEXTO ÚNICO
#);
#CREAR TABLA Género (
 #   id ENTERO NO NULO CLAVE PRIMARIA AUTOINCREMENTO ÚNICO,
  #  nombre TEXTO ÚNICO
#);
#CREAR TABLA Álbum (
#    id ENTERO NO NULO CLAVE PRIMARIA AUTOINCREMENTO ÚNICO,
#    ID_artista ENTERO,
#    Título TEXTO ÚNICO
#);
#CREAR TABLA Seguimiento (
#    id ENTERO NO NULO CLAVE PRIMARIA
#        AUTOINCREMENTO ÚNICO,
#    título TEXTO ÚNICO,
#    album_id ENTERO,
#    genre_id ENTERO,
#    longitud ENTERO, calificación ENTERO, recuento ENTERO
#);
#Si ejecuta el programa varias veces para realizar pruebas o con archivos diferentes, asegúrese de vaciar los datos antes de cada ejecución.
#Puedes usar este código como punto de partida para tu aplicación: http://www.py4e.com/code3/tracks.zip . El archivo ZIP contiene el archivo tracks.csv que se utilizará para esta tarea. Puedes exportar tus propias pistas desde iTunes y crear una base de datos, pero para la base de datos que entregues en esta tarea, usa únicamente los datos de tracks.csv proporcionados. Puedes adaptar la aplicación tracks_csv.py del archivo ZIP para completar la tarea.
#Para calificar esta tarea, el programa ejecutará una consulta como esta en la base de datos que hayas cargado y buscará los datos que espera encontrar:
#SELECT Track.title, Artist.name, Album.title, Genre.name 
#    FROM Track JOIN Genre JOIN Album JOIN Artist 
#    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
#        AND Album.artist_id = Artist.id
#    ORDER BY Artist.name LIMIT 3


import sqlite3

conn=sqlite3.connect("canciones.sqlite")
cur=conn.cursor()

#protección para probar varias veces
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track
''')
cur.executescript('''
CREATE TABLE Artist (
    id INTEGER PRIMARY KEY,  
    name TEXT UNIQUE);

CREATE TABLE Genre (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE);
    
CREATE TABLE Album (
    id INTEGER PRIMARY KEY, 
    artist_id INTEGER, 
    title TEXT UNIQUE);
    
CREATE TABLE Track (
    id INTEGER PRIMARY KEY, 
    title TEXT UNIQUE, 
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER);
''')

##archivo a leer
doc=open("tracks.csv")

for line in doc:
    line=line.strip()
    partes=line.split(",")
    if len(partes)<7:continue
    
    nombre=partes[0]
    artista=partes[1]
    album=partes[2]
    count=partes[3]
    rating=partes[4]
    length=partes[5]
    genero=partes[6]
    
    #print(nombre, artista, album, count, rating, length, genero)
    
    #tabla artista#
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES(?)", (artista,))
    cur.execute("SELECT id FROM Artist WHERE name=?",(artista,))
    artist_id=cur.fetchone()[0]
    
    #tabla genero#
    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES(?)", (genero,))
    cur.execute("SELECT id FROM Genre WHERE name=?",(genero,))
    genre_id=cur.fetchone()[0]
    
    #tabla album#
    cur.execute("INSERT OR IGNORE INTO Album (title,artist_id) VALUES(?,?)", (album,artist_id))
    cur.execute("SELECT id FROM Album WHERE title=?",(album,))
    album_id=cur.fetchone()[0]
    
    #tabla canciones#
    cur.execute("INSERT OR replace INTO Track (title,album_id,genre_id,len, rating, count) VALUES(?,?,?,?,?,?)", (nombre,album_id,genre_id,length,rating,count))
    
    #grabar"
    conn.commit()
cur.close()
print("base de datos actualizada")

exit()
            

