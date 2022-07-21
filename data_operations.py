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

def select_all(conn, table):
    """
    Query all rows in the table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    return rows

def select_where(conn, table, **query):
    """
    Query tasks from table with data from **query dict
    :param conn: the Connection object
    :param table: table name
    :param query: dict of attributes and values
    :return:
    """
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    return rows    

def update_parameter(conn, table, id, **query):
    """
    update first_name, last_name and nationality of the sportsperson
    :param conn: 
    :param table:
    :param id: 
    :param query: dict of attributes and values
    :return:
    """
    parameters = [f"{k} = ?" for k in query]
    parameters = ", ".join(parameters)
    values = tuple(v for v in query.values())
    values += (id, )

    sql = f''' UPDATE {table}
               SET {parameters}
               WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()        
    except sqlite3.OperationalError as e:
        print(e)

def delete_all(conn, table):
    """
    Delete all rows from table
    :param conn: Connection to the SQLite database
    :param table: table name
    :return:
    """
    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def delete_where(conn, table, **query):
    """
    Delete from table where attributes from
    :param conn:  Connection to the SQLite database
    :param table: table name
    :param kwargs: dict of attributes and values
    :return:
    """
    qs = []
    values = tuple()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    
if __name__ == "__main__":
    conn = create_connection("database.db")
    select=select_where(conn, "sportspeople", last_name="Ballack")
    change_name=update_parameter(conn, "sportspeople", 2, first_name="Janusz")
    delete=delete_where(conn,"sportspeople", first_name="Janusz")
    