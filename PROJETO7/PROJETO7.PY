from pathlib import Path
import os
import sys

def validate(c):
    prohibited = '<>:"/\\|?*'
    if any(character in c for character in prohibited):
        print('Invalid name.')
        main_menu()

def main_menu():
    Path.cwd()
    print("""Type the number of the operation you want to perform or type nothing to close:
        0 - create folder
        1 - check files on folder
        2 - create or change .txt file
        3 - check text on .txt file""")
    comando = input()
    if comando == "":
        sys.exit()
    elif int(comando) == 0:
        create_folder()
    elif int(comando) == 1:
        check_files()
    elif int(comando) == 2:
        create_txt()
    elif int(comando) == 3:
        read_txt()
          
def create_folder():
        try:
            print('Type the name of the folder you want to create:')
            pasta = input()
            validate (pasta)
            os.mkdir(pasta)
            print('Folder created')
        except FileExistsError:
            print('This folder already exists')
        main_menu()
        
def check_files():
    print('Type the name of the folder where the files are:')
    pasta = input()
    validate (pasta)
    if os.path.exists(pasta):
        arquivos = os.listdir(pasta)
        if arquivos == []:
            print('This folder is empty')
        else:
            print(arquivos)
    else:
        print('This folder does not exist')
    main_menu()

def create_txt():
    print('Type the name of the folder where the file you want to create or change is:')    
    pasta = input()
    validate (pasta)
    if os.path.exists(pasta):
        print('Type the title of the .txt document you want to create or change')
        titulo = input()
        validate (titulo)
        print('Type the text you want to put in the .txt document')
        texto = input()
        validate (texto)
        with open(pasta + '/' + titulo + '.txt', 'w', encoding="utf-8") as f:
            txtFile = f.write(texto)                 
    main_menu()

def read_txt():
    print('Type the name of the folder where the file you want to read is:')
    pasta = input()
    validate (pasta)
    print('Type the name of the file you want to read:')
    titulo = input()
    validate (titulo)
    with open(pasta + '/' + titulo + '.txt', 'r', encoding="utf-8") as f:
        txtFile = f.read()
        print(txtFile)
    main_menu()
    
main_menu()

