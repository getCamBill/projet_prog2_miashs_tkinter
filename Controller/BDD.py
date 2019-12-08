import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ créer une connexion de base de données à une base de données SQLite """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ créer une table à partir de l'instruction create_table_sql
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_joueur(conn, user):
    """
    Créer un nouveau joueur dans la table joueur
    :param conn:
    :param user:
    :return: user id
    """
    sql = ''' INSERT INTO joueur(pseudo,win,lose)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid

def update_partie_joueur(conn, task):
    """
    met à jour le nombre de victoire et de défaite apres une partie
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE joueur
              SET win = win + ? ,
                  lose = lose + ?
              WHERE pseudo = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def delete_joueur(conn, pseudo):
    """
    supprime un joueur de la bdd
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM joueur WHERE pseudo=?'
    cur = conn.cursor()
    cur.execute(sql, (pseudo,))
    conn.commit()

def delete_all(conn):
    """
        supprime tous les joueurs
        :param conn:  Connection to the SQLite database
        :return:
        """
    sql = 'DELETE FROM joueur'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def select_all_joueurs(conn):
    """
    affiche tous les joueurs
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM joueur")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_joueur_by_victory(conn):
    """
    affiche tous les joueurs pars nb de victoire
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM joueur ORDER BY win DESC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def first():
    database: str = "./Controller/UserDatabase.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS joueur (
                                                id integer PRIMARY KEY,
                                                pseudo text NOT NULL,
                                                win integer,
                                                lose integer
                                            ); """
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create Joueur table
        create_table(conn, sql_create_projects_table)
    else:
        print("Erreur! Impossible de créer une connection avec le Controller.")

    """ 
        TRIGGER A FINIR ...
    """
    # conn.execute('''DROP TRIGGER IF EXISTS ajout_user''')
    # conn.execute('''CREATE TRIGGER ajout_user
    #              BEFORE INSERT ON joueur
    #              BEGIN
    #                 CASE
    #                     WHEN (SELECT pseudo FROM joueur WHERE NEW.pseudo <> pseudo);
    #                      THEN
    #                     INSERT INTO joueur (pseudo,win,lose) VALUES (NEW.pseudo,NEW.win,NEW.lose);
    #                 END;
    #
    #              END
    #              ;
    #              ''')


if __name__ == '__main__':

    first()

    # create a database connection
    database: str = "./Controller/UserDatabase.db"
    conn = create_connection(database)

    # with conn:
    #     # create a new joueur
    #     user = ('kmi', 0, 1)
    #     user_id = create_joueur(conn, user)
    #
    # with conn:
    #     update_partie_joueur(conn, (1, 0, 'kmi'))
    #
    # with conn:
    #     print("1. Classement des joueurs par victoire:")
    #     select_joueur_by_victory(conn)
    #
    # # supp d'un joueur
    # with conn:
    #     delete_joueur(conn, 'kmi')

    with conn:
        print("1. Classement des joueurs par victoire:")
        select_joueur_by_victory(conn)