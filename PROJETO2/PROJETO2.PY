def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

print("Olá, qual é o seu nome?")
name = input()
print("Seu nome é " + name)
print("Qual é a sua idade?")
age = input()

if is_numeric(age):
    print("Você tem " + age + " anos")
    print("Você terá " + (str((int(age) + 1))+ " anos no ano que vem"))
else:
    print("Esse valor não é um número inteiro")
