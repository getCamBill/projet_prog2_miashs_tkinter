from Controller.BDD import *
from tkinter import *
from PIL import *
#
# first()

#
# pseudo: str = input("Entrez un pseudo : ")
# create_joueur(conn, (pseudo, 0,0))
# select_joueur_by_victory(conn)

root = Tk()
root.title("Liste des Joueurs")
# root.iconbitmap()
# root.geometry("400x400")

database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
conn = create_connection(database)
# --------------------------------------------------------------------------
fr1 = Frame(root, width=200, height=200)
fr1.grid(row=0, column=0)
fr2 = Frame(root, width=200, height=200)
fr2.grid(row=0, column=1)
# --------------------------------------------------------------------------

def submit():
    # clear champ texte
    if not user_name.get() == "":
        conn = create_connection(database)
        user = (user_name.get(), 0, 0)
        create_joueur(conn, user)
        user_name.delete(0, END)
        montrer()

# --------------------------------------------------------------------------
def montrer():
    listbox.delete(0, END)
    conn = create_connection(database)
    listeJ = select_joueur_by_victory(conn)
    for i in listeJ:
        listbox.insert(END, i[1])
# --------------------------------------------------------------------------

user_name = Entry(fr1, width=30)
user_name.grid(row=0, column=1, padx=20)

user_name_label = Label(fr1, text="Pseudo")
user_name_label.grid(row=0, column=0)
# --------------------------------------------------------------------------

submit_btn = Button(fr1, text="Ajouter pseudo", command=submit)
submit_btn.grid(row=2, column=1, padx=10, pady=10)
# --------------------------------------------------------------------------
scrollbar = Scrollbar(fr2)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(fr2)
listbox.pack()
# conn = create_connection(database)
# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
montrer()
# --------------------------------------------------------------------------

conn.close()
root.mainloop()

