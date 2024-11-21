import random
# -----------------------------------------------------------------
zxc = 0 # Количество очков
random_number1 = random.randint(10, 100) # Число которое дано
random_number2 = random.randint(1, 10) # То что нужн ололучить
victory = False # Победа
lvl = 0
# -----------------------------------------------------------------
# Установка уровня сложности
while 0 == 0:
    qwe = int(input("> 1 = Лёгкий \n > 2 = Нормальный \n > 3 = Сложный\nВыбери уровень сложности: "))
    if qwe == 1:
        zxc = 800
        break
    elif qwe == 2:
        zxc = 600
        break
    elif qwe == 3:
        zxc = 400
        break
    else:
        print("Ты даун?")
# -----------------------------------------------------------------
# Проверка какую операцию выбрал игрок
def examination_operation(item, item2):
    if item == "+" and item2 < 100000:
        addition(item2)
    elif item == "-" and item2 < 100000:
        subtraction(item2)
    elif item == "*" and item2 < 100000:
        multiplication(item2)
    elif item == "/" and item2 < 100000:
        division(item2)
    else:
        print("Такой операции нету или число больше 99999")
# -----------------------------------------------------------------
# Функции для операций
def addition(item):
    global zxc
    global random_number1
    if zxc >= (50+item):
        zxc-=(50+item)
        random_number1+=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def subtraction(item):
    global zxc
    global random_number1
    if zxc >= (50+item):
        zxc-=(50+item)
        random_number1-=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def multiplication(item):
    global zxc
    global random_number1
    if zxc >= (60+item):
        zxc-=(60+item)
        random_number1*=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def division(item):
    global zxc
    global random_number1
    if zxc >= (100+item):
        zxc-=(100+item)
        random_number1//=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")
# -----------------------------------------------------------------
# Проверка на победу заранее
def check_for_victory():
    global victory
    global end_game1
    if random_number1 == random_number2:
        victory = True
        end_game1 = False
# -----------------------------------------------------------------
# Игра
end_game = True
while end_game == True:
    end_game1 = True
# -----------------------------------------------------------------
# Вывод на экран задачи
    print(f"Вам дано: {random_number1} | Нужно получить: {random_number2} | Баланс: {zxc}")
# -----------------------------------------------------------------
# Сама игра
    while end_game1 == True:
        x = input("Введи действие (+ - * / $): ")
        if x == "$":
            end_game = False
            break
        elif x == "*" or x == "-" or x == "+" or x == "/":
            xx = int(input("Ввиди число: "))
            examination_operation(x, xx)
            check_for_victory()
            print(f"У тебя: {random_number1} | Нужно получить: {random_number2} | Баланс: {zxc}")
# -----------------------------------------------------------------
# Проверка на победу после окончания действий
    check_for_victory()
    if victory == True:
        lvl+=1
        print(f"ВЫ прошли на новый уровень {lvl}")
        zxc+=500
    else:
        print(f"Игра окончена ваш уровень {lvl-1}")
        break
    victory = False
    random_number2 = random.randint(1, (10*lvl*qwe)) # То что нужно получить

