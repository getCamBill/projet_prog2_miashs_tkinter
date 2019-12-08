from View.gameClass import Game
from Controller.BDD import *
from Model.Joueur import *

if __name__ == "__main__":
    first()
    g = Game('kmi', 'gg')
    g.start()

    database: str = "./Controller/UserDatabase.db"
    conn = create_connection(database)
    select_joueur_by_victory(conn)