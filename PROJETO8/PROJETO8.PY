import sqlite3
from pathlib import Path
import sys
import re

caminho = Path(__file__).parent
cursor = '' #global cursor so we can use it in any functions
connection = '' #global connection so we can use it in choose_DB function

def choose_DB():
    print('Choose a database from the available files below:')
    listaNomeArquivos = list(arquivo.name for arquivo in caminho.iterdir())
    listaDB = list(name for name in listaNomeArquivos if '.db' in name)
    if listaDB == '':
        print('No databases found. Closing application.')
        sys.exit()
    print(listaDB)
    chosenDB = input()
    if Path(chosenDB).is_file():
        try:
            global connection
            connection = sqlite3.connect(chosenDB)
            global cursor
            cursor = connection.cursor()
            main_menu()
        except Exception as e:
            print(e)
        finally:
            connection.close()
    else:
        print('This file does not exist.')
        choose_DB()

def main_menu():
    while True:
        print("""Choose an option or type nothing to quit:
            0 - Create a new table.
            1 - Read a table.
            """)
        command = input()
        if command == '':
            sys.exit()
        elif int(command) == 0:
            create_table()
        elif int(command) == 1:
            read_table()

def create_table():
    print('Type a name for the table:')
    tableNameChosen = input()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tableNameChosen,))
    while cursor.fetchone() is not None: #checking if table already exists and looping if it does.
        print('Table already exists. Choose another name.')
        tableNameChosen = input()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tableNameChosen,))
    while not re.fullmatch('[a-zA-Z_][a-zA-Z0-9_]*', tableNameChosen): #checking prohibited names and SQL injection with loop.
        print('Invalid name. Choose another')
        tableNameChosen = input()
    while True:    
        print('Type the names of the columns you want to include in the table, separated by a comma (,):')
        tableColumnsChosen = input()
        columnsList = [word.strip() for word in tableColumnsChosen.split(',')] #passing string to list using strip() and split()
        regexOk = True
        for column in columnsList: #checking regex with loop
            if not re.fullmatch('[a-zA-Z_][a-zA-Z0-9_]*', column):
                print('One or more invalid column names. Choose other names.')
                regexOk = False
                break
        if regexOk:
            break
        
        # Can also use a for / else loop in Python to break the for and while loops:
        # else:
        #     break
                   
    sqlColumns = ', '.join(f"{coluna} TEXT" for coluna in columnsList) #creating string that can be used for SQL query
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tableNameChosen} ({sqlColumns})")
    #"IF NOT EXISTS" redundant since we know it doesn't from previous checks but included anyway for study purposes
    #"IF NOT EXISTS" does not return any error if the table already exists. It simply does nothing in that case
    #"CREATE TABLE" by itself, on the other hand, returns an error if the table already exists 
    print(f'Table {tableNameChosen} created.')
    print(f'Current tables in current database:')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tableNames = cursor.fetchall()
    print(tableNames)
    main_menu()

def read_table():
    print('Choose a table to be read from the available tables below:')
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tableNames = cursor.fetchall()
    print(tableNames)
    tableChosen = input()   
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tableChosen,))
    #We use the comma on (string,) here because the .execute function requires
    #a tuple in the second argument, even if there is only one value on the var.
    while cursor.fetchone() is None:
        print('This table does not exist. Choose another.')
        tableChosen = input()   
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (tableChosen,))
        #We can use placeholder '?' here because we are not calling
        # the table name itself. Instead of that, we are giving a string to compare to the name.        
    cursor.execute(f"SELECT * FROM {tableChosen}")
    #Here we cannot use '?' as a placeholder because we are calling table name itself.
    showTable = cursor.fetchall()
    print(f'The contents of {tableChosen} are show below:')
    print(showTable)
    main_menu()

choose_DB()                   


