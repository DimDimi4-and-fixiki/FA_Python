**Свежая документация python:**
    docs.python.org

**Книжки:**

- A byte of Python(для новичков)
- A dive into Python(для более продвинутых)


*Немного про строки:*

```python
s = "Hello"
print(s[0]) # выводит 1ый символ строки
print(s[2]) # выводит 3ий символ строки
print(s * 3) # выводит строку s 3 раза
```

**Регист символов важен в Python!**
*Пример:*

```python
a = 20
print(A) # переменная A не объявлена, есть только переменная a
# Такой код не работает
```

**Типы данных:**
-  int(целые числа)
-  float(дробные числа)
-  bool(True, False)
-  str(строка)

узнать тип переменной можно с помощью *type()*

**Переменные в коде:**

Лучше называть переменные так, чтобы название содержало больше информации(не называть переменные a или b и т.д)

```python
name_of_character = "John" # переменная типа str
age_of_character = 20 # переменная типа int
print("Once there lived" + name_of_character)
print(name_of_character + "was" + str(age_of_character))
print("He was born in" + str(2019 - age_of_character))
```

***Условные операторы в Python***

Условные операторы нужны, чтобы выполнить определенный код при каких-то условиях

```python
# eсли персонажу больше 45 лет, то выполниться код, вложенный в if
if age_of_character > 45: 
	print("He is so old")
	print("He wants to see he's grandchildren")
	print("He waits for his 100th birthday")

```
**В python выжны отступы, такой код, например, не работает:**

```python
if age_of_character > 45: 
        print("He is so old")
      print("He wants to see he's grandchildren")
     print("He waits for his 100th birthday")
```
***Различные сравнения***

	Строгое сравнение:
		2 > 3 возвращает False
		100 > 60 возвращает True

	Нестрогое сравнение :
		2 >= 3  возвращает False
		3 <= 5  возвращает True
	    
	Проверка на равентво:
		2 * 2 == 4 возвращает True

	Проверка на неравенство:
		2 != 3  возвращает True
		2 != 2  возвращает False

**Оператор *and* в python**
Нужен чтобы проверить выполнение несколько условий одновременно

*Пример:*

```python
a = 30

if a > 10 and a < 100:  #проверка что a > 10 и a < 100
	print("Kek")

if 10 < a < 100: # тоже самое, что и в предыдущем if
	print("Kek")
``` 
**Оператор elif**
Пишется после if или другого elif. В случае если предыдущее условие не выполнилось, то проверяется условие в elif.
```python
a = 40
if a > 100: # условие в *if* не выполняется, поэтому проверится условие в *elif*
	print("Lul")
elif a < 50: #условие в elif выполняется, поэтому на экран выведится Kek
	print("Kek")

```
**Оператор else**
    используется чтобы выполнить код, если условия  *if* и *elif* не выполнились, пишется после всех *if* и *elif*
```python
a = 0
if 10 < a < 100: #проверка что a > 10 и a < 100
	print("if")
elif a == 5:
	print("elif")
else:
	print("else") # при a = 0 ни условие в if ни в elif  не выполняются, поэтому выполнится код в else
```

**Задание1. По кол-ву баллов ученика вывести его оценку:**

```python
rating = int(input("Введите свои баллы")) #считываем количество баллов и переводим его в int
if 0 <= rating < 50:
    print("Неудачник")
if 50 <= rating < 70:
    print("Ну такое...")
if 70 <= rating < 86:
    print("Что, не мог подучить?")
if 86 <= rating <= 100:
    print("Покатит!")
else:
    print("Ты что не можешь число ввести? Может тебе не сюда?")
```

**Задание2. По номеру года вывести високосный он или обычный:**

*Решение:*

```python
year = int(input("Введите год -> "))

if (year % 400 == 0) or ((year % 4) == 0 and (year % 100 != 0)):
    print("Leap")
else:
    print("Regular")

```

**Задание 3. Вводится 3ех значное число. Вывести сумму его цифр**

*Решение1:*

```python
number = int(input("Введите число -> "))

a = number // 100 # число сотен
b = (number // 10) % 10 # число десятков
c = number % 10 # число единиц

print(a + b + c)

```

*Решение2:*

```python
number = str(input("Введите число "))
a = int(number[0]) # первая цифра
b = int(number[1]) # вторая цифра
c = int(number[2]) # третья цифра

print(a + b + c)
```
**Задание 4. Вводится число градусов Фаренгейт или Цельсий. Перевести Цельсий в Фаренгейт или наоборот**

*Решение:*

```python
string = input("Введите -> ")

temperature = float(string([0:-1]))
scale = string[-1]

if scale == "C":
    res = round(temperature * 1.8 + 32, 3)
    print(str(res) + "F")
elif scale == "F":
    res = round((temperature - 32) / 1.8, 3)
    print(str(res) + "C")
else:
    print("Каво?")
```

**Задание 5. Даны числа a, b, c. Решить квадратное уравнение ax^2 + bx + c = 0**

*Решение:*

```python

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b ** 2 - 4 * a * c #считаем дискриминант

equation = str(a) + "x^2 +" + str(b) + "x +" + str(c)

print("Решаем уравнене", equation)

if D < 0:
    print("Действительных корней нет")
elif D == 0:
    x = - b / (2 * a)
    print("Единственный корень", x)
else:
    x1 = (-b + D**(1/2)) / (2 * a)
    x2 = (-b - D**(1/2)) / (2 * a)
    print("Первый корень:", x1)
    print("Второй корень:", x2)

    
```
