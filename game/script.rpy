# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define s = Character('Тоторо', color="#f3ff00")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


init:
    $ a = True
    $ q = 0


# Игра начинается здесь:
label start:
    play music "sound/Totoro.mp3"
    scene room
    show eileen happy
    s "Хаюшки)"
    s "Я загодаю число, а ты попробуй отгадай."
    python:
        b = renpy.input("До какого числа мне загадывать?")
    $ n = renpy.random.randint(1, int(b))
    menu:
        "Ну ок, давай.":
            while a:
                $ q = q+1
                menu:
                    "Задавай вопросы."
                    "Оно четное?":
                        if n % 2 == 0:
                            s "Да."
                        else:
                            s "Нет."
                    "Оно меньше ...?":
                        call onev
                    "Оно больше ...?":
                        call twov
                    "Вы готовы дать ответ? ":
                        call threev
        "Пока!!!.":
             s "Все игра закончена("
    return

label onev:
    python:
        vb = renpy.input("Введите число: ")
    if n < int(vb):
        s "Да. Оно меньше [vb]"
    else:
        s "Нет. Оно больше [vb]"
    return

label twov:
    python:
        vm = renpy.input("Введите число: ")
    if n > int(vm):
        s "Да. Оно больше [vm]"
    else:
        s "Нет. Оно меньше [vm]"
    return

label threev:
    python:
        o = renpy.input("Введите число: ")
    if n == int(o):
        s "Да. Это было число [n]"
        $ q = q-1
        s "Вы выиграли! Поздравляю, игра закончена, вы назвали число за [q] вопросов)"
        $ a = False
    else:
        s "Нет. Это не [o]("
    return
