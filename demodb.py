import sqlite3

def rows_to_dict(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

with sqlite3.connect("books/books.db3") as conn:
    c = conn.cursor()
    c.execute("select id, title, price from book")
    for row in rows_to_dict(c):
        print(row)