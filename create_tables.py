import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       cur = conn.cursor()
       cur.execute(sql)
   except Error as err:
       print(err)

if __name__ == "__main__":

    create_sports_sql = """
    -- sports table
    CREATE TABLE IF NOT EXISTS sports (
        id integer PRIMARY KEY,
        name text unique NOT NULL    
    );
    """

    create_sportspeople_sql = """
    -- sportspeople table
    CREATE TABLE IF NOT EXISTS sportspeople (
        id integer PRIMARY KEY,
        sport_id int NOT NULL,
        first_name text NOT NULL,
        last_name text NOT NULL,
        nationality text,
        FOREIGN KEY (sport_id) REFERENCES sports (id)
    );
    """

    db_file = "database.db"

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_sports_sql)
        execute_sql(conn, create_sportspeople_sql)
        conn.close()