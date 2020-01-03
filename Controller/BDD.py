import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    """ créer une connexion de base de données à une base de données SQLite """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return connection


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
    conn.commit()
    return cur.lastrowid

def select_joueur(conn, pseudo):
    """
    selection d'un joueur de la bdd si existe déjà
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    try:
        sql = 'SELECT * FROM joueur WHERE pseudo=?'
        cur = conn.cursor()
        cur.execute(sql, (pseudo,))
        joueur = cur.fetchall()[0] # ex : (13, 'Olove', 0, 0)
        conn.commit()
        return joueur
    except:
        conn.commit()
        return False # code erreur si le joueur n'existe pas
    # except Error as e:
    #     print(e)

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

    conn.commit()

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
    return list(rows)


def first():
    filename = os.path.relpath('..\\Controller\\UserDatabase.db')
    database: str = filename
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS joueur (
                                                id integer PRIMARY KEY,
                                                pseudo text NOT NULL,
                                                win integer,
                                                lose integer
                                            ); """

    conn = create_connection(database)

    if conn is not None:
        # create Joueur table
        create_table(conn, sql_create_projects_table)
    else:
        print("Erreur! Impossible de créer une connection avec le Controller.")

    """ 
        TRIGGER A FINIR ...
    """
    conn.execute('''DROP TRIGGER IF EXISTS ajout_user''')
    conn.execute('''CREATE TRIGGER ajout_user
                 BEFORE INSERT ON joueur
                 BEGIN
                    CASE
                        WHEN (SELECT pseudo FROM joueur WHERE NEW.pseudo <> pseudo);
                         THEN
                        INSERT INTO joueur (pseudo,win,lose) VALUES (NEW.pseudo,NEW.win,NEW.lose);
                    END;

                 END
                 ;
                 ''')

# if __name__ == '__main__':
