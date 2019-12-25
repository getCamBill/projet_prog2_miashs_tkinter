from Controller.BDD import *
from tkinter import *
from tkinter import ttk
from Model.Joueur import *
from PIL import *

class AddUser():
    def __init__(self, onglet):

        self.root = onglet

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
        self.user_name_label = Label(self.fr1, text="Joueur 1")
        self.user_name_label.grid(row=0, column=0)

        self.user_name2 = Entry(self.fr1, width=30)
        self.user_name2.grid(row=1, column=1, padx=20)
        self.user_name_label2 = Label(self.fr1, text="Joueur 2")
        self.user_name_label2.grid(row=1, column=0)
        # --------------------------------------------------------------------------

        self.submit_btn = Button(self.fr1, text="JOUER", command=self.submit(self.user_name.get(),self.user_name2.get()))
        self.submit_btn.grid(row=2, column=1, padx=10, pady=10)

        # --------------------------------------------------------------------------

        # self.root.mainloop()




    # --------------------------------------------------------------------------
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