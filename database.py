import sqlite3

def db_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_table():
    # connects to db (or creates one) and automatically closes it
    with db_connection('finances.db') as connection:

        # cursor object that interacts with the database
        cursor = connection.cursor()
        
        # no need to do connection.close(), its done automatically
        # print("Database created and connected successfully")
    
        # create table query
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Finances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            savings REAL NOT NULL, 
            wants REAL NOT NULL, 
            needs REAL NOT NULL,
            date TEXT NOT NULL
        );
        '''
        
        # Execute the SQL command
        cursor.execute(create_table_query)

        # commit the changes
        connection.commit()
        # print("Table 'finances' has been created!")
