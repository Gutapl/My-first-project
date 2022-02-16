truea = 0
massiveest = set() #массив с буквами которые человек уже угадал
massivenet = set() #массив с тем каких букв тут нету
massivea = set() #массив с данным словом
count = 0
while truea != 1: # соблюдает ли слово нужные нам условия
    a = input('Здравствуйте, сегодня сыграем виселицу загадайте русское слово:') #проверка на правильность ввода
    a = a.lower()
    for i in a:
        if not((1072 <= ord(i) <= 1103) or (ord(i) == 1105)): #проверка на русские буквы
            print("Неправильное слово!")
            truea = 0
            massivea = set()
            break
        else:
            truea = 1
            massivea.add(i)
while count == 0:
    count = int(input("Введите количество промахов на отгадку!"))
    if (count < 2) or (count >= 33): # количество промахов не должно быть больше чем букв в алфавите
        print("Попыток не может быть меньше двух, столько же или больше чем букв в русском алфавите!")
        count = 0   
print("Вы загадали в слово! Позовите второго игрока, чтобы он угадал!")
print("Теперь к правилам:")
print("Вы не можите угадать несколько букв, вы можите угадать слово целиком или угадывать по ОДНОЙ букве (я не агрессирую, просто обращаю внимание)")
print('Введите "!comands", чтобы получить кучу полезных команд')
star = ("*" * len(a))
print(star)
star = list(star)
count1 = count #сколько было попыток
b = input("Угадайте букву") #буква которую человек вводит чтобы угадать есть ли она в слове
while count != 0:
    b = b.lower()
    if not(b in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя') and (len(b) == 1):
        print("Это не является русской буквой")
        b = input('Угадайте букву')
        continue
    if (b == a) and (len(b) > 1):# проверка на правильность всей строки
        print("Ты угадал!!!")
        print()
        print(count, 'это твоё оставшиеся количество попыток на промах из', count1)
        break
    elif (len(b) == 1) and (b in a):
        if b in massiveest: # проверка на та была ли буква
            print('вы уже вводили данную букву')
        print("'" + b + "'", "есть в этом слове")
        counta = -1
        for i in a:
            counta += 1
            if b == i:
                for i in star:
                    if i == '*':
                        star[counta] =  b 
        for i in star:
            print(i, end='')      
        massiveest.add(b)
    elif len(b) == 1 and not(b in a):#есть ли в слове эта буква
        print(b, 'этой буквы нету в слове')
        count -= 1
        print()
        massivenet.add(b)
    elif b == '!help':
        print("Советую начать с отгадки гласных")
        print()
    elif b == '!Never':
        print(massivenet)
        print()
    elif b == '!slovo':
        for i in massivea:
            print(i, end=' ')     
        print()
        count = 1
    elif b == '!popitka':
        print(count, "это твоё оставшиеся количество попыток на промах из", count1)
    elif b == '!comands':
        print('"!comands" для выведения всех команд')
        print('!"!Never" комнда показывающая неправильные буквы, который вы ввели')
        print('"!help" даёт классный совет')
        print('!slovo мини режим, в котором у тебя будет одна попытка на то, что бы угадать слово (в этом слове будут даны уже все буквы вперемешку и один раз)')
        print('"!popitka" сколько осталось')
    elif '!' in b:
        print("Нет такой команды")
    else:
        print("Неверно!!!") #когда человек ввёл слово, но не отгадал
        break
    if (massivea == massiveest): #проверка на то угадал ли человек слово 
        print()
        print('Ты угадал все буквы!!! ', "Это слово", a)
        print()
        print(count, 'это твоё оставшиеся количество попыток на промах из', count1)
        break
    b = input('Угадайте букву')
    print()