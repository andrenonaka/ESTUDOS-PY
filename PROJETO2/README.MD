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

We do not want to convert the age var to int using is_numeric() right away, since we may want to use this function for other checks later. We convert age to int in the block that asks for the age input. This block also prints age and age +1.

```python
if is_numeric(age):
    print("Você tem " + age + " anos")
    print("Você terá " + (str((int(age) + 1))+ " anos no ano que vem"))
else:
    print("Esse valor não é um número inteiro")
```


