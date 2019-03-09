import sqlite3
from difflib import get_close_matches

# connect to database and create cursor object
db = sqlite3.connect("dict.db")
cursor = db.cursor()

# word search function
def word_search(query):
    # create list of entries from database
    data = [entry[0] for entry in cursor.execute("SELECT entry FROM en_dictionary")]
    alternate = None
    
    # check if word is present in dictionary (as typed, in lowercase, uppercase and title case)
    if query in data:
        return (query, return_def(query), alternate)
    
    elif query.lower() in data:
        return (query.lower(), return_def(query.lower()), alternate)

    elif query.upper() in data:
        return (query.upper(), return_def(query.upper()), alternate)

    elif query.title() in data:
        return (query.title(), return_def(query.title()), alternate)
    
    # if word is not found, check if there are up to 3 similar words and return them
    else:
        alternate = get_close_matches(query.lower(), data, n=3, cutoff=0.8)
        
        if alternate:
            return None, None, alternate
        
        else:
            return "Sorry, that word is not listed", None, None
        
# return all definitions of the word as a list
def return_def(word):
    defs = "".join([d[0] for d in cursor.execute("SELECT definitions FROM en_dictionary WHERE entry=?", (word,))]).split("\n")
    return defs

def close_db():
    db.close()