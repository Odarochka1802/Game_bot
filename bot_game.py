import telebot
from telebot import types
from random import randint

token='5912567534:AAH7VYXVeIgmDDxVrk7ZdrOnz8fQ1K0wurc'
bot=telebot.TeleBot(token)

class User:
    def __init__(self, name):
        self.name = name


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! Сыграем в игру?')

player1 = ""
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, "Отлично!\nУсловие задачи: На столе лежит 101 конфета. Играют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,\nчтобы забрать все конфеты у своего конкурента?\nНапиши 'Вперед' для начала игры!")
    if message.text == 'Вперед':
        bot.send_message(message.chat.id, "Введите имя")

@bot.message_handler(content_types=['text'])
def main(message):
    if player1 == "":
        player1 = message.text
        bot.send_message(message.chat.id,f"{player1}, Начинаем!")





def input_col(name):
    global x
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 9: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def bot_up():
    player1 = "Player"
    player2 = "Bot_up"
    value = 2021
    flag = randint(0, 2)  # флаг очередности
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    counter1 = 0
    counter2 = 0

    while value > 28:
        if flag:
            k = input_col(player1)
            counter1 += k
            value -= k
            flag = False
            p_print(player1, k, counter1, value)
        else:
            k = value % 29
            counter2 += k
            value -= k
            flag = True
            p_print(player2, k, counter2, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")


print("start")

bot.infinity_polling()
