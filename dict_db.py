import sqlite3
import json



def create_table():
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE en_dictionary (entry UNIQUE, definitions TEXT)")
    conn.commit()
    conn.close()

def insert(entry, definition):
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO en_dictionary(entry, definitions) VALUES(?, ?)", (entry, definition))
    conn.commit()
    conn.close()

def delete_entry(entry):
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM en_dictionary WHERE entry=?", (entry,))
    conn.commit()
    conn.close()

def update_entry(entry, new_definition):
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    defs = "".join([d[0] for d in cur.execute("SELECT definitions FROM en_dictionary WHERE entry=?", (entry,))]).split("\n")
    defs.append(new_definition)
    new_defs = "\n".join(defs)
    cur.execute("UPDATE en_dictionary SET definitions=? WHERE entry=?", (new_defs, entry))
    conn.commit()
    conn.close()

def view_entry(entry):
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    cur.execute("SELECT definitions FROM en_dictionary WHERE entry=?", (entry,))
    for row in cur:
        print(row)
    conn.close()


def if_exists(entry):
    conn=sqlite3.connect("dict.db")
    cur=conn.cursor()
    cur.execute('SELECT 1 FROM en_dictionary WHERE entry=? LIMIT 1', (entry,))
    entry_exists = cur.fetchone() is not None
    print(entry_exists)

insert("blablabla", "whatever")