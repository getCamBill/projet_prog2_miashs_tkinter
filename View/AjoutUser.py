from Controller.BDD import *

first()
# create a database connection
database: str = "C:\\Users\\camil\\PycharmProjects\\Quarto\\Controller\\UserDatabase.db"
conn = create_connection(database)

choix = ""
while choix != 'q':

    choix = input("\n\n1/ Créer un pseudo \n"
                    "2/ Supprimer un joueur \n"
                    "3/ Consulter joueurs \n"
                    "4/ Consulter classement \n"
                    "5/ Ajouter victoire \n"
                    "6/ Ajouter défaite \n"
                    "7/ Tout supprimer \n"
                  "\nChoix : ")

    if choix == '1':
        pseudo = input("\nEntrer un pseudo : ")
        with conn:
            # create a new joueur
            user = (pseudo, 0, 0)
            user_id = create_joueur(conn, user)
    elif choix == '2':
        # supp d'un joueur
        pseudo = input("\nEntrer le pseudo à supp : ")
        with conn:
            delete_joueur(conn, pseudo)
    elif choix == '3':
        with conn:
            print("\n1. Liste des Joueurs")
            select_all_joueurs(conn)
    elif choix == '4':
        with conn:
            print("\n1. Classement des joueurs par victoire:")
            select_joueur_by_victory(conn)
    elif choix == '5':
        pseudo = input("\nEntrer un pseudo : ")
        with conn:
            update_partie_joueur(conn, (1, 0, pseudo))
    elif choix == '6':
        pseudo = input("\nEntrer un pseudo : ")
        with conn:
            update_partie_joueur(conn, (0, 1, pseudo))
    elif choix == '7':
        choix = input("y/n ?")
        if choix == 'y':
            with conn:
                delete_all(conn)

