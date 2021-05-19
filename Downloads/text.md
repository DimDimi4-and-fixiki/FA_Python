**Свежая документация python:**
    - docs.python.org

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
if a > 100: # условие в if не выполняется, поэтому проверится условие в elif
	print("Lul")
elif a < 50: #условие в elif выполняется, поэтому на экран выведится Kek
	print("Kek")

```
**Оператор else**
    используется чтобы выполнить код, если условия  if и elif не выполнились, пишется после всех if и elif
```python
a = 0
if 10 < a < 100: #проверка что a > 10 и a < 100
    print("if")
elif a == 5:
	print("elif")
else:
    print("else") # при a = 0 ни условие в if ни в elif  не выполняются, поэтому выполнится код в else
```






