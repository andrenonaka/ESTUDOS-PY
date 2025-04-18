# PROJETO 2

**Program that asks for name and age and returns name, age and age+1.**

input() function always retuns string, so we need to make sure that the age var is aways an int.

We define a is_numeric() function to "try()" for int number. If int, return True. If not int, return False and warn user that number is not int:

```python
    def is_numeric(value):
        try:
            int(value)
            return True
        except ValueError:
            return False
```

We do not want to convert the age var to int using is_numeric() right away, since we may want to use this function for other checks later. We convert age to int in the block that asks for the age input. This block also prints 

```python
if is_numeric(age):
    age = int(age)
    print("Você tem " + str(age) + " anos")
    print("Você terá " + (str(age + 1)+ " anos no ano que vem"))
else:
    print("Esse valor não é um número inteiro")
```

We could, instead of age = int(age), create another var (such as "ageint") to make sure that the age var is kept pure, but in the context of this code there is no situation where we would use the age var as a str, so the block above works fine.



