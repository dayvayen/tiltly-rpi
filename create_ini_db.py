import sqlite3
from sqlite3 import Error

db_file = raw_input("Database name: ")
beerName = raw_input("What are you naming your beer? ")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def sql_create_beer_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main(db_file, beerName):

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        sql_create_beer_table(conn, "create table " + beerName + """  (
          time datetime,
          temperature float,
          gravity float
        );""")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main(db_file, beerName)
