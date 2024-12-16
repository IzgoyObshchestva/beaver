import random
# -----------------------------------------------------------------
zxc = 0 # Количество очков
random_n1 = random.randint(10, 100) # Число которое дано
random_n2 = random.randint(1, 10) # То что нужн ололучить
victory = False # Победа
# -----------------------------------------------------------------
# Установка уровня сложности
def slo():
    while True:
        qwe = input("> 1 = Лёгкий \n > 2 = Нормальный \n > 3 = Сложный\nВыбери уровень сложности: ")
        match qwe:
            case "1":
                return 1, 800
            case "2":
                return 2, 600
            case "3":
                return 3, 400
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
    global zxc, random_n1
    if zxc >= (50+item):
        zxc-=(50+item)
        random_n1+=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def subtraction(item):
    global zxc, random_n1
    if zxc >= (50+item):
        zxc-=(50+item)
        random_n1-=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def multiplication(item):
    global zxc, random_n1
    if zxc >= (60+item):
        zxc-=(60+item)
        random_n1*=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")

def division(item):
    global zxc, random_n1
    if zxc >= (100+item):
        zxc-=(100+item)
        random_n1//=item
    else:
        print(f"У вас не достатьчно средств | Ваш баланс: {zxc}")
# -----------------------------------------------------------------
# Проверка на победу заранее
def check_for_victory(x, xx):
    if x == xx:
        return True, False
    else:
        return False, True
# -----------------------------------------------------------------
# Игра
def main():
    global zxc, random_n1, random_n2
    lvl = 1
    Lera, zxc = slo()
    end_game = True
    while end_game == True:
        end_game1 = True
    # -----------------------------------------------------------------
    # Вывод на экран задачи
        print(f"Вам дано: {random_n1} | Нужно получить: {random_n2} | Баланс: {zxc}")
    # -----------------------------------------------------------------
    # Сама игра
        while end_game1 == True:
            x = input("Введи действие (+ - * / $): ")
            if x == "$":
                end_game = False
                break
            elif x in "*-+/":
                xx = input("Ввиди число: ")
                try:
                    xx = int(xx)
                except ValueError:
                    continue
                else:
                    examination_operation(x, xx)
                    victory, end_game1 = check_for_victory(random_n1, random_n2)
                    print(f"У тебя: {random_n1} | Нужно получить: {random_n2} | Баланс: {zxc}")
    # -----------------------------------------------------------------
    # Проверка на победу после окончания действий
        if victory == True:
            lvl+=1
            print(f"ВЫ прошли на новый уровень {lvl}")
            zxc+=500
        else:
            print(f"Игра окончена ваш уровень {lvl-1}")
            break
        victory = False
        random_n2 = random.randint(1, (10*lvl*Lera)) # То что нужно получить

if __name__ == '__main__':
    main()