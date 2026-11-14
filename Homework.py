import sqlite3

connection = sqlite3.connect("shop.sl3")
cur = connection.cursor()
print("Підключення успішне")

cur.execute("CREATE TABLE IF NOT EXISTS animals (type TEXT,name TEXT)")

#cur.execute("INSERT INTO animals (type, name) VALUES ('савець', 'Мавпа')")
#cur.execute("INSERT INTO animals (type, name) VALUES ('птахи', 'орел')")
#cur.execute("INSERT INTO animals (type, name) VALUES ('земноводні', 'Морська черепаха')")
connection.commit()

cur.execute("SELECT * FROM animals")
print(cur.fetchall())

cur.execute("SELECT * FROM animals WHERE type = 'савець'")
print(cur.fetchall())

cur.execute("UPDATE animals SET name = сокіл WHERE name = 'орел'  ")
connection.commit()

cur.execute("DROP TABLE animals")
connection.commit()

connection.close()