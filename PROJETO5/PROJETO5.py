lista = ['apple', 'car', 'cat', 'apple', 'dog']
operation = [0, 1, 2, 3, 4, 5]
#0 = add
#1 = add with position
#2 = remove
#3 = show all
#4 = show specific
#5 = check if item is on list

while True:
    print('Digite o número da operação (ou aperte "Enter" sem digitar nada para finalizar):')
    print('0 = adicionar item à lista')
    print('1 = adicionar item à lista e indicar posição de inserção')
    print('2 = remover item da lista')
    print('3 = mostrar lista inteira')
    print('4 = mostrar item específico da lista')
    print('5 = verificar se o item se encontra na lista')
    opnum = input()
    if opnum == '':
        break
    if int(opnum) in operation:
        if int(opnum) == 0:
            print("Digite o item a ser adicionado na lista")
            toAdd = input()
            lista.append(toAdd)
            #lista = [item for item in lista if item != toAdd] #force error to test.
            if toAdd in lista: #redundant. For testing and study purposes.
                print(toAdd + ' foi adicionado à lista')
            else:
                print('Algo deu errado. ' + toAdd + ' não foi adicionado à lista.')
        elif int(opnum) == 1:
            print('Digite o item a ser adicionado na lista')
            toAddPosition = input()
            print('Digite a posição em que o item deve ser inserido na lista')
            index = input()
            if 0 <= int(index) <= len(lista):
                lista.insert(int(index), toAddPosition)
            else:
                print('Essa posição não existe na lista. Gostaria de inserir este item na última posição? (S/N)') 
                if input().strip().lower() == 's':
                    lista.append(toAddPosition)
                else:
                    print('Inserção cancelada.')
        elif int(opnum) == 2:
            print("Digite o nome item que gostaria de remover da lista")
            toRemove = input()
            if toRemove in lista:
                lista = [item for item in lista if item != toRemove]
                #lista = lista.append(toRemove) #force error to test.
                if toRemove not in lista: #redundant. For testing and study purposes.
                    print ('Todas as instâncias de ' + toRemove + ' foram removidas da lista')
                else:
                    print('Algo deu errado. ' + toRemove + ' não foi removido da lista.')
            else:
                print('Este item não existe na lista')
        elif int(opnum) == 3:
            if lista == []:
                print('A lista está vazia')
            else:
                print(lista)
        elif int(opnum) == 4:
            print('Informe a posição do item que gostaria de verificar')
            toView = input()
            if 0<= int(toView) <= len(lista) and (int(toView) - 1) >= 0:
                print('O item nesta posição é: ' + lista[int(toView) - 1])
            else:
                print('Esta posição não existe.')
        elif int(opnum) == 5:
            print('Informe o item que quer verificar')
            toCheck = input()
            if toCheck in lista:
                indexCheck = [i for i, name in enumerate(lista) if name == toCheck]
                if len(indexCheck) == 1:
                    print('O item está na ' + str(int(indexCheck[0] + 1)) + 'ª posição.')
                elif len(indexCheck) > 1:
                    print('Foram identificados mais de um item com este nome. As posições serão listadas abaixo:')
                    for i in indexCheck:
                        print(str(int(i) + 1))          
            else:
                print('Este item não existe na lista.')
    else:
        print('Este comando não existe.')
              
