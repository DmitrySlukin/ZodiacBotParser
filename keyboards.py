from telebot import types


def start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    usual = types.KeyboardButton("🙂 Повседневный")
    erotic = types.KeyboardButton("❤️ Любовный")
    career = types.KeyboardButton("🤑 Финансовый")
    sexual = types.KeyboardButton("💕 Сексуальный")
    women = types.KeyboardButton("♀️ Женский")
    men = types.KeyboardButton("♂️ Мужской")
    markup.add(usual, erotic, career, sexual, women, men)
    return markup

def back_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = types.KeyboardButton("Назад")
    markup.add(back)
    return markup
