import random
# -----------------------------------------------------------------
zxc = 0 # Количество очков
random_number1 = random.randint(10, 100000) # Число которое дано
random_number2 = random.randint(1, 9) # То что нужн ололучить
victory = False # Победа
# -----------------------------------------------------------------
# Установка уровня сложности
while 0 == 0:
    qwe = int(input("Дорово\nВыбери уровень сложности\n > 1 = Лёгкий \n > 2 = Нормальный \n > 3 = Сложный"))
    if qwe == 1:
        zxc = 700
        break
    elif qwe == 2:
        zxc = 500
        break
    elif qwe == 3:
        zxc = 300
        break
    else:
        print("Ты даун?")
# -----------------------------------------------------------------
# Проверка какую операцию выбрал игрок
def examination_operation(item, item2):
    global zxc
    if x == "+" and item2 < 100:
        addition(item2)
    elif x == "-" and item2 < 100:
        subtraction(item2)
    elif x == "*" and item2 < 100:
        multiplication(item2)
    elif x == "/" and item2 < 100:
        division(item2)
    elif x == "$" and item2 < 100:
        zxc = 0
    else:
        print("Такой операции нету или число больше 99")
# -----------------------------------------------------------------
# Вывод на экран задачи
print(f"Вам дано: {random_number1} | Нужно получить: {random_number2} | Кол. действий {zxc}")
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
    global zxc
    global victory
    if random_number1 == random_number2:
        victory = True
        zxc = 0
# -----------------------------------------------------------------
# Сама игра
while 0 < zxc:
    x = input("Введи действие (+ - * / $): ")
    if x == "$":
        break
    else:
        xx = int(input("Ввиди число: "))
        examination_operation(x, xx)
        check_for_victory()
        print(f"У тебя: {random_number1} | Нужно получить: {random_number2} | Кол. действий {zxc}")
# -----------------------------------------------------------------
# Проверка на победу после окончания действий
check_for_victory()
if victory == True:
	print("Победа")
else:
	print("Порожение")

