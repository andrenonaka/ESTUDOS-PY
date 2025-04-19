## PROGRAM THAT COUNTS UP TO A NUMBER AND OTHER STUFF

We want to count up to a number provided by the user. Then, we want to check if that number is within a specified range, if not we reject it. Then, we return to the user if the number is even or odd, and if the number is higher or lower than 10. Then we count up to the number and we print() each iteration of the count.

We start with a basic function to check if the number received is an int:

```python
def is_numeric(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
```
If the received input is not an int, we request new input with while until we receive an int.

```python
num = input()
while is_numeric(num) == False:
    print("Este não é um número inteiro. Favor digital um número inteiro.")
    num = input()
```
Then we convert num to int and check if the number is within acceptable range (in this case, between 5 and 20). If it's not, we state that in print and further actions are not performed. If it is, then we proceed to print the relevant information (if number is even or odd, if number is 10 or not).

```python
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
```
The function for determining if the number is even or odd is done using the % operator, which divides the var by a number and returns the remainder. In this example, we compare the remainder with 0 with == and the == operator returns True or False. We do not need to use the if to check the result of the == operator since == already returns True or False, but we added the check for clarity purposes.

```python
def is_even(n):
    result = n % 2
    if result == 0:
        return True
    else:
        return False
    #may also use return (n % 2 == 0)
```

Counting may be done using while or for. For is preferable since its cleaner and avoid infinite loops. Functions for while and for are defined for study purposes:

```python
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
```