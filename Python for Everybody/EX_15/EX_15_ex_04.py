print("examen 04, cap 15")

import json
import sqlite3

conn=sqlite3.connect("alumnos.sqlite")
cur=conn.cursor()

#protección para probar varias veces
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member
''')
cur.executescript('''
CREATE TABLE User (
    id INTEGER PRIMARY KEY,  
    name TEXT UNIQUE);

CREATE TABLE Course (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE);
    
CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id,course_id))
''')

##archivo a leer
fname="roster_data.json"

str_data=open(fname).read()
json_data=json.loads(str_data)

for line in json_data:
        
    name=line[0];
    title=line[1];
    role=line[2];
    
    #print((name, title, role))
    
     #tabla User#
    cur.execute("INSERT OR IGNORE INTO User (name) VALUES(?)", (name,))
    cur.execute("SELECT id FROM User WHERE name=?",(name,))
    user_id=cur.fetchone()[0]
    
    #tabla Course#
    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES(?)", (title,))
    cur.execute("SELECT id FROM Course WHERE title=?",(title,))
    course_id=cur.fetchone()[0]
    
  #tabla Member#
    cur.execute("INSERT OR REPLACE INTO Member (user_id,course_id,role) VALUES(?,?,?)", (user_id,course_id,role))
    

#grabar"
conn.commit()

cur.close()
print("base de datos actualizada")

exit()
            
