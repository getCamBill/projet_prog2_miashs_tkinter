from Controller.BDD import *
from tkinter import *
from tkinter import ttk
from PIL import *

class AddUser():
    def __init__(self, onglet):

        self.root = onglet
        # self.root.title("Liste des Joueurs")

        self.database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
        self.conn = create_connection(self.database)
        # --------------------------------------------------------------------------
        self.fr1 = Frame(self.root)
        self.fr1.grid(row=0, column=0)
        self.fr2 = Frame(self.root)
        self.fr2.grid(row=0, column=1)
        # --------------------------------------------------------------------------
        self.user_name = Entry(self.fr1, width=30)
        self.user_name.grid(row=0, column=1, padx=20)

        self.user_name_label = Label(self.fr1, text="Pseudo")
        self.user_name_label.grid(row=0, column=0)
        # --------------------------------------------------------------------------

        self.submit_btn = Button(self.fr1, text="Ajouter pseudo", command=self.submit)
        self.submit_btn.grid(row=2, column=1, padx=10, pady=10)
        # --------------------------------------------------------------------------
        self.scrollbar = Scrollbar(self.fr2)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.fr2, width=35)
        self.listbox.pack()
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.montrer()
        # --------------------------------------------------------------------------

        # self.root.mainloop()
    def submit(self):
        # clear champ texte
        if not self.user_name.get() == "":
            user = (self.user_name.get(), 0, 0)
            create_joueur(self.conn, user)
            self.user_name.delete(0, END)
            self.montrer()

    # --------------------------------------------------------------------------
    def montrer(self):
        self.listbox.delete(0, END)
        listeJ = select_joueur_by_victory(self.conn)
        for i in listeJ:
            info = "Pseudo :"+ i[1]+" Victoire : "+str(i[2])+" Défaite : "+str(i[3])
            self.listbox.insert(END, info)
    # --------------------------------------------------------------------------

if __name__ == '__main__':
    fenetre = Tk()
    fenetre.title("Quarto !! ")

    n = ttk.Notebook(fenetre)  # Création du système d'onglets

    n.pack()
    o1 = ttk.Frame(n)  # Ajout de l'onglet 1
    o1.pack()
    n.add(o1, text='Quarto')  # Nom de l'onglet 1

    o1 = Tk()
    a = AddUser(o1)
    fenetre.mainloop()
    a.conn.close()