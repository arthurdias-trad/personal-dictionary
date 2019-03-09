from tkinter import * 
from search_func import word_search
from tkinter import messagebox

window = Tk()
window.title("English Dictionary")
window.grid_rowconfigure(1,weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
# window.geometry("500x500")

def start_search():
    w = word.get()
    if w == "":
        return 0
    
    # use tuple of variables to control possibilities: word or message, list of definitions, list of possible alternatives
    w, defs, alternate = word_search(w)
    t1.delete(0, END)
    
    if not defs and not alternate:
        t1.insert(END, "{}".format(w))
    elif not defs and alternate:
        try:
            w, defs, alternate = confirm_alternate(alternate)
            t1.insert(END, "{}:\n".format(w))
            dfn_num = 1
            for dfn in defs:
                t1.insert(END, "{} - {}\n".format(dfn_num, dfn))
                dfn_num += 1
        except:
            pass
    elif defs:
        t1.insert(END, "{}:\n".format(w))
        dfn_num = 1
        for dfn in defs:
            t1.insert(END, "{} - {}\n".format(dfn_num, dfn))
            dfn_num += 1

def confirm_alternate(alternate):
    for word in alternate:
        MsgBox = messagebox.askquestion('Word Not Found','Did you mean {}?'.format(word),icon = 'warning')
        if MsgBox == 'yes':
            return word_search(word)
    else:
        t1.insert(END, "Sorry, that word is not listed. Consider adding a definition.")

word = StringVar()
e1 = Entry(window, textvariable=word)
e1.grid(row=0, column=0, columnspan=3, sticky=W+E+N+S, padx=5, pady=2)


b1 = Button(window, text="Find definitions", anchor=CENTER, command=start_search)
b1.grid(row=0, column=3, padx=2, pady=2)

t1 = Listbox(window, width=75)
t1.grid(row=1, column=0, columnspan=4,sticky=W+E+N+S, padx=5, pady=2)



window.mainloop()