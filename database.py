import sqlite3

from main import calculate_monthly_spending, get_date

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

def insert_data():
    monthly_spending = calculate_monthly_spending()
    needs = monthly_spending[0]
    wants = monthly_spending[1]
    savings = monthly_spending[2]

    date = get_date()
    
    data = (savings, wants, needs, date)

    with db_connection('finances.db') as connection:
        cursor = connection.cursor()

        insert_query = '''
            INSERT INTO Finances (savings, wants, needs, date)
            VALUES (?, ?, ?, ?)
        '''

        cursor.execute(insert_query, data)
        print("Record inserted successfully!")

def list_all_records():
    with db_connection('finances.db') as connection:
        cursor = connection.cursor()
        select_query = '''
            SELECT * FROM Finances;
        '''
        cursor.execute(select_query)

        # In the future find a better way of representing this data to
        # make it look better
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        
