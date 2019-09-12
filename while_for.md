***Циклы в Python***


***Цикл while*

*Синтаксис: *

```python
while True:  # это бесконечный цикл
    print("Hello, world!")

i = 0

while i < 5: # этот цикл выведет Hello world 5 раз
    i += 1 # тоже самое что i = i + 1
    print("Hello world")


```

**Задание 1. Вывести сумму цифр числа**

```python

num = int(input())
sum = 0

if num < 0:
    num *= -1

while num != 0:
    sum += num % 10 # добавляем цифру к сумме 
    num //= 10 #  делим число на 10 

print(sum)
    

```

**Задание 2. Дано число, посчитать его факториал**

*Решение :*

```python

num = int(input("Введите число -> "))
fact = 1


while num > 1:
    fact *= num
    num -= 1

print("Факториал", fact)

```

**Задание 3. Дано число, вывести составное оно или простое**

*Решение: *

```python
num = int(input())
res = "Простое"

candidate = 2

while candidate < num:
    if num % candidate == 0:
        res = "Составное"
    candidate += 1

print(res)
```
