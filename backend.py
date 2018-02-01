import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("create table if not exists book (id integer primary key,\
                                                  title text, author text,\
                                                  year integer,\
                                                  isbn integer)")
    conn.commit()
    conn.close()

def add(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()

def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("select * from book where title=? \
                 or author=? or year=? or isbn=?",(title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("update book set title=?, author=?, year=?, \
                 isbn=? where id=?",(title, author, year, isbn, id))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute("select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
#print(view())
#add("livro 1","Me",1955,15151515)
#update(1,"livro 1444","Mew",1955,15151515)
#delete(2)
#print(search(year=1955))
