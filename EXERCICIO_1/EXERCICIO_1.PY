import tkinter as tk
from tkinter import ttk
import sys

class animal:
    def __init__(self, tipo, quantidade, valor):
        self.tipo = tipo
        self.quantidade = quantidade
        self.valor = valor
        pass

boi = animal('Boi', 0, 10)
vaca = animal('Vaca', 0, 5)
bezerro = animal('Bezerro', 0, 0.5)

def validate(lista):
    if len(lista) > 3:
        print('Você inseriu mais de três valores. Insira apenas três valores.')
        return False
    else:   
        try:           
            for valor in lista:
                int(valor)
                if int(valor) < 0:
                    print('Um dos valores inseridos é negativo.')
                    return False           
                else:
                    return True                
        except Exception as error:
            print('Um dos valores inseridos não é um número inteiro ou não é um número.')
            print(error)

def compra_animal(bois_comprados, vacas_compradas, bezerros_comprados):
    if (boi.valor*int(bois_comprados) +
        vaca.valor*int(vacas_compradas) +
        bezerro.valor*int(bezerros_comprados) == 100) and (int(bois_comprados) +
        int(vacas_compradas) + int(bezerros_comprados) == 100):
        print('Correto!')
        sys.exit
    else:
        print('Incorreto')

def main_loop():
    while True:
        print('Digite o número de bois, vacas e' \
        'bezerros a serem comprados, nesta ordem e' \
        'separados por uma vírgula (,):')
        
        animais_comprados = input()
        print(animais_comprados)  

        lista_valores = [animais.strip() for animais in animais_comprados.strip().split(',')]
        print(lista_valores)

        validar_lista = validate(lista_valores)

        if validar_lista == True:

            compra_animal(*lista_valores)

main_loop()