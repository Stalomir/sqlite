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
    except Error as err:
        print(err)
    return conn

def add_sport(conn, sport):
    """Add a new sport into the sports table
    :param conn:
    :param sports:
    :return: sport id
    """
    sql = '''
    INSERT OR IGNORE INTO sports (name)
    VALUES(?)
    '''
    cur = conn.cursor()
    cur.execute(sql, sport)
    conn.commit()
    return cur.lastrowid
    
def add_sportsperson(conn, sportsperson):
    """Create a new task into the tasks table
    :param conn:
    :param sportsperson:
    :return: sportsperson id
    """
    sql = '''
    INSERT OR IGNORE INTO sportspeople(sport_id, first_name, last_name, nationality)
    VALUES(?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, sportsperson)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    
    db_file = "database.db"
    conn = create_connection(db_file)
    sport = ["Football"]
    sport_id = add_sport(conn, sport)
    sportsperson = (sport_id, "Thierry", "Henry", "France")
    sportsperson2 = (sport_id, "Franc", "Lampard", "England")
    sportsperson3 = (sport_id, "Michael", "Ballack", "Germany")
    add_sportsperson(conn, sportsperson)
    add_sportsperson(conn, sportsperson2)
    add_sportsperson(conn, sportsperson3)
        

