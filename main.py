import asyncio
from datetime import date
from telebot import types
import variables as var
from parser import parser
import config
import keyboards


# Функция обработки первого сообщения в чат, команды \start
@config.zodiac_bot.message_handler(commands=['start'])  # декоратор в который передаем отслеживаемые команды
async def start(message):  # Декорируемая функция, принимает сообщение от пользователя
    mess = f'Привет, {message.from_user.first_name}!'
    # Отправляем сообщение в чат по id чата.
    await config.zodiac_bot.send_message(message.chat.id, mess, parse_mode='html')
    #                                         ^^^^^^^     ^^^^        ^^^^^
    #                               Обязательные параметры  Необязательный (Без него будет просто текст без html-тегов)

    await config.zodiac_bot.send_message(message.chat.id, 'Выбери гороскоп!', reply_markup=keyboards.start_keyboard())


# Функция обработки  команды \about
@config.zodiac_bot.message_handler(commands=['about'])
async def about(message):
    mess = f'О проекте:'
    await config.zodiac_bot.send_message(message.chat.id, mess, parse_mode='html')
    await config.zodiac_bot.send_message(message.chat.id, var.about_message, reply_markup=keyboards.back_keyboard())


# Функция обработки  команды \donate
@config.zodiac_bot.message_handler(commands=['donate'])
async def donate(message):
    # mess = f'Привет, {message.from_user.first_name}!'
    # await config.zodiac_bot.send_message(message.chat.id, mess, parse_mode='html')
    await config.zodiac_bot.send_message(message.chat.id, var.donate_message, reply_markup=keyboards.back_keyboard())


# Функция обработки всех последующих сообщений в чат

@config.zodiac_bot.message_handler(content_types=['text'])
async def get_user_choice(message):
    message_list = str(message.text).split()
    #    Создаем новую клавиатуру со знаками зодиака.
    if message.text in var.menu_dict:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        aries = types.KeyboardButton(f"{var.menu_dict[message.text]} Овен")
        taurus = types.KeyboardButton(f"{var.menu_dict[message.text]} Телец")
        gemini = types.KeyboardButton(f"{var.menu_dict[message.text]} Близнецы")
        cancer = types.KeyboardButton(f"{var.menu_dict[message.text]} Рак")
        leo = types.KeyboardButton(f"{var.menu_dict[message.text]} Лев")
        virgo = types.KeyboardButton(f"{var.menu_dict[message.text]} Дева")
        libra = types.KeyboardButton(f"{var.menu_dict[message.text]} Весы")
        scorpio = types.KeyboardButton(f"{var.menu_dict[message.text]} Скорпион")
        sagittarius = types.KeyboardButton(f"{var.menu_dict[message.text]} Стрелец")
        capricorn = types.KeyboardButton(f"{var.menu_dict[message.text]} Козерог")
        aquarius = types.KeyboardButton(f"{var.menu_dict[message.text]} Водолей")
        pisces = types.KeyboardButton(f"{var.menu_dict[message.text]} Рыбы")
        back = types.KeyboardButton("Назад")
        markup.add(
            aries, taurus, gemini, cancer, leo, virgo, libra,
            scorpio, sagittarius, capricorn, aquarius, pisces, back
        )
        await config.zodiac_bot.send_message(message.chat.id, 'Выбери свой знак зодиака!', reply_markup=markup)

    #  Выводим гороскоп в соответствии с категорией и знаком зодиака
    elif message_list[0] in var.symbols_dict:
        cur_url = f'{config.url}{var.zodiac_dict[message_list[1]]}{var.symbols_dict[message_list[0]]}'
        response = parser(cur_url)
        response = ''.join(response)
        current_date = date.today().strftime("%d.%m.%Y")
        await config.zodiac_bot.send_message(message.chat.id,
                                             f"Астрологический прогноз на сегодня <b><u>{current_date}</u></b>, \n"
                                             f"для знака зодиака <b><u>{message.text}</u></b>: \n"
                                             f"{response}", parse_mode='html')
    #  Возвращаемся к выбору категорий
    elif message.text == "Назад":
        await config.zodiac_bot.send_message(
            message.chat.id, 'Выбери гороскоп!',
            reply_markup=keyboards.start_keyboard()
        )

    else:
        await config.zodiac_bot.send_message(message.chat.id, f"Прости, но я не знаю такого знака зодиака.")


if __name__ == '__main__':
    asyncio.run(config.zodiac_bot.polling(none_stop=True))  # Запускает постоянное выполнение бота
