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
        zxc = 7
        break
    elif qwe == 2:
        zxc = 5
        break
    elif qwe == 3:
        zxc = 3
        break
    else:
        print("Ты даун?")
# -----------------------------------------------------------------
# Проверка какую операцию выбрал игрок
def examination_operation(item, item2):
    global zxc
    if x == "+" and item2 < 100:
        addition(item2)
        zxc-=1
    elif x == "-" and item2 < 100:
        subtraction(item2)
        zxc-=1
    elif x == "*" and item2 < 100:
        multiplication(item2)
        zxc-=1
    elif x == "/" and item2 < 100:
        division(item2)
        zxc-=1
    else:
        print("Такой операции нету или число больше 99")
# -----------------------------------------------------------------
# Вывод на экран задачи
print(f"Вам дано: {random_number1} | Нужно получить: {random_number2} | Кол. действий {zxc}")
# -----------------------------------------------------------------
# Функции для операций
def addition(item):
	global random_number1
	random_number1+=item

def subtraction(item):
	global random_number1
	random_number1-=item

def multiplication(item):
	global random_number1
	random_number1*=item

def division(item):
	global random_number1
	random_number1//=item
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
	x = input("Введи действие (+ - * /): ")
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

