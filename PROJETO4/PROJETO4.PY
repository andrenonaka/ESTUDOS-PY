def is_numeric(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def is_even(n):
    result = n % 2
    if result == 0:
        return True
    else:
        return False
    #may also use return (n % 2 == 0)

def counting_while(n):
    count = 0
    #typically uses "i" for counters
    while (count <= n): 
        print(count)
        count = count + 1
        #may also use count += 1
    print("Contagem com while finalizada. Valor final: " + str(count-1))
    
def counting_for(n):
    for count in range(n+1):
        print(count)
    print("Contagem com for finalizada. Valor final: " + str(count))

print("Digite um número de 5 a 20")

num = input()
while is_numeric(num) == False:
    print("Este não é um número inteiro. Favor digital um número inteiro.")
    num = input()
    
num = int(num)
if num > 20:
    print("Este número é maior que 20")
elif num < 5:
    print("Este número é menor que 5")
else:
    if is_even(num):
        print("Este número é par")
    else:
        print("Este número é ímpar")
    if num > 10 or num < 10:
        print("Este número é diferente de 10")
    else:
        print("Este número é 10")
    print("Iniciando contagem de número")
    ##counting_while(num)
    counting_for(num)        
    




