import sqlite3

def create_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("create table if not exists store (item text, quantity integer, price real)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("insert into store values (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("select * from store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("delete from store where item=?", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("update store set quantity=?, price=? where item=?", (quantity, price, item))
    conn.commit()
    conn.close()

print(view())
insert("Water Glass", 8, 10.5)
#insert("Coffe Cup", 11, 15.5)
print(view())
update("Water Glass", 800, 100.5)
#insert("Coffe Cup", 11, 15.5)
print(view())
delete('Water Glass')
#delete('Coffe Cup')
print(view())
