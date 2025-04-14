import telebot
import random
import os

bot = telebot.TeleBot("7640320851:AAHGowt8e-ju4VOvFgBE5Oe2Qj6goA7VSj8")

mems = ('mem1.jpeg', 'mem2.jpeg', 'mem3.jpeg', 'mem4.jpg')

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот😁. Напиши что-нибудь! 🙌")

@bot.message_handler(commands=['commands', 'help', 'listcommands'])
def show_commands(message):
    commands_list = [
        ("/hello", "Приветствие"),
        ("/bye", "Пока!"),
        ("/pass", "Сгенерировать рандомный пароль (8 символов)"),
        ("/mem", "Отправить случайный мем"),
        ("/flip", "Подбросить монетку"),
        ("/pin", "Сгенерировать PIN-код"),
        ("/random", "Случайное число от 1 до 1000"),
    ]

    message_text = "Доступные команды:\n"
    for command, description in commands_list:
        message_text += f"- {command} - {description}\n"
    
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?😊")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!👋😸")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  
    bot.reply_to(message, "Вот твой сгенерированный пароль🖥: {}".format(password))

@bot.message_handler(commands=['flip'])
def coin_flip(message):
    result = "Орел 🦅" if random.choice([True, False]) else "Решка 🪙"
    bot.reply_to(message, f"Монета подброшена: {result}")

@bot.message_handler(commands=['pin'])
def send_pin(message):
    pin = ''.join(random.choice('0123456789') for _ in range(4))
    bot.reply_to(message, f"🔢 Ваш PIN-код: {pin}")

@bot.message_handler(commands=['random'])
def send_random(message):
    num = random.randint(1, 1000)
    bot.reply_to(message, f"🎲 Случайное число: {num}")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    if mems:  # Проверяем, есть ли файлы в папке
        mem = random.choice(mems)
        with open(f'images/{mem}', 'rb') as f:
            bot.send_photo(message.chat.id, f)
    else:
        bot.reply_to(message, "В папке нет мемов 😢")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(none_stop=True)
