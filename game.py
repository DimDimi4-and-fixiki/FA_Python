***Пишем игру***

```python
from random import randint #подключаем рандом
total_games, wins = 0, 0

while True: #зацикливаем игру   
    total_games += 1

    print("До скольки загадывать")
    print("1 - короткая игра(от 1 до 10)")
    print("2 - средняя игра(от 1 до 100)")
    print("3 - длинная игра(от 1 до 1000)")
    level = input("Ну так как играем?")
    UPPER_BOUND = 100 # верхняя граница 
    tries = 7
    
    
    if level == "1":
        UPPER_BOUND = 10
        tries = 4
    elif level == "2":
        UPPER_BOUND = 100
        tries = 7
    elif level == "3":
        UPPER_BOUND = 1000
        tries = 10
    
    print("Выбери уровень сложности:")
    print("1 - новичок")
    print("2 - мастер")
    print("3 - хардкор")
    level = input("Ну так как играем?")
    
    if level == "1":
        tries *= 2
    elif level == "2":
        pass
    elif level == "3":
        tries //= 2
    else:
        print("Вы ввели что-то не то")
        UPPER_BOUND = 10
        tries = 4
        
    secret_number = randint(1, UPPER_BOUND)
    # Пользователь начинает угадывать
    while tries > 0:
        print("У вас осталось", tries, "попыток")
        user_number = int(input("Введите свою догадку: "))
#     Проверка угадал ли он 
        if UPPER_BOUND >= user_number >= 1:
            if user_number == secret_number:
                print("Вы угадали!")
                wins += 1
                break
            elif user_number < secret_number:
                print("Нужно число больше")
            elif user_number > secret_number:
                print("Нужно число меньше")
            tries = tries - 1
        else:
            print("Вы ввели некорректное число!")
#    Вывод текущего счета
    print()
    print("==============")
    print("Игра закончена")
    print("==============")
    print("Вы выйграли", wins, "раз")
    print("А я выйграли", total_games - wins, "раз")
    print()
    print("Может уже хватит?")
    resp = input("Введите n чтобы звкончить игру")
    if resp == "n":
        break
```
