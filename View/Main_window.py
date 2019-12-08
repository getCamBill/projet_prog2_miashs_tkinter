# import winsound
# import time
# winsound.PlaySound('fichier_son.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
# time.sleep(5)
# winsound.PlaySound(None, 0)

# ## Menus
#
# from tkinter import *
#
#
# def fctSousMenu1():  # Action associée au sous-menu 1 du menu 1
#     print('Action1')
#
#
# jeu = Tk()
#
# jeu.option_add('*tearOff', FALSE)  # Nécessaire avec windows
#
# menubar = Menu(jeu)  # Création d'un objet "barre de menus"
# jeu['menu'] = menubar  # Association de l'objet à la fenêtre
#
# # Ajout de menus
# menu1 = Menu(menubar)
# menu2 = Menu(menubar)
#
# # Ajout de sous-menus
# menubar.add_cascade(menu=menu1, label='Menu 1')
# menubar.add_cascade(menu=menu2, label='Menu 2')
#
# # Association de fonctions aux menus ou sous-menus
# menu1.add_command(label='Action 1', command=fctSousMenu1)
# menu1.add_separator()  # Barre de séparation
#
# menu1.add_command(label='Action 2', command=None)
#
# jeu.mainloop()

## Onglets

from tkinter import *
from tkinter import ttk
from View.Ajout_user_view import *

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


jeu = Tk()
app=FullScreenApp(jeu)

n = ttk.Notebook(jeu)  # Création du système d'onglets
n.pack()
o1 = ttk.Frame(n)  # Ajout de l'onglet 1
o1.pack()
o2 = ttk.Frame(n)  # Ajout de l'onglet 2
o2.pack()
n.add(o1, text='Onglet 1')  # Nom de l'onglet 1
n.add(o2, text='Onglet 2')  # Nom de l'onglet 2

Button(o1, text='Quitter', command=jeu.destroy).pack(padx=500, pady=250)
Button(o2, text='En attente', command=None).pack(padx=500, pady=250)

jeu.mainloop()