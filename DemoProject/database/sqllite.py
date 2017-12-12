import sqlite3

conn = sqlite3.connect("test.db")

cur = conn.cursor()

cur.execute('''
SELECT name FROM sqlite_master
''')

table_exists = False

try:
    for row in cur.fetchall():
        if row[0] == "student":
            table_exists = True
            break
    
    if table_exists:
        print "Table already exists..."
    else:
        print "Table not exists..."
        cur.execute('''
        create table student(id real primary key, name text, marks real)
        ''')
        print "Table Created..."
        
except Exception as ex:
    raise Exception("Exception in creating table: %s" % ex)

flag = False

while flag:
    id = input("Enter Student Id: ")
    name = raw_input("Enter Name: ")
    marks = input("Ener Marks: ")

    cur.execute('''
    insert into student(id,name, marks) values(?,?,?)
    ''', (id, name, marks,))
    
    cont = raw_input("Record inserted... Continue?(Y/N): ")
    
    if cont == 'Y' or cont == 'y':
        flag = True
    else:
        flag = False

cur.execute('''
select id,name,marks from student
''')
records = cur.fetchall()

for record in records:
    print "%s\t%s\t%s" % (record[0], record[1], record[2])

conn.commit()
conn.close()
