from Controller.BDD import *

first()
database: str = 'C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db'
conn = create_connection(database)

pseudo: str = input("Entrez un pseudo : ")
create_joueur(conn, (pseudo, 0,0))
select_joueur_by_victory(conn)