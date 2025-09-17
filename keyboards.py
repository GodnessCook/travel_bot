from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
def main_menu():
    kb = [
        [InlineKeyboardButton("📅 План по дням", callback_data="days")],
        [InlineKeyboardButton("🗣 Разговорник", callback_data="phrasebook")],
        [InlineKeyboardButton("ℹ️ FAQ", callback_data="faq")],
        [InlineKeyboardButton("🍜 Еда", callback_data="food")],
    ]
    return InlineKeyboardMarkup(kb)


# Меню разговорника
def phrasebook_menu():
    kb = [
        [InlineKeyboardButton("🍽 Еда", callback_data="phrase_food")],
        [InlineKeyboardButton("🚖 Транспорт", callback_data="phrase_transport")],
        [InlineKeyboardButton("⚕️ Экстренное", callback_data="phrase_emergency")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="main")],
    ]
    return InlineKeyboardMarkup(kb)


# Меню FAQ
def faq_menu():
    kb = [
        [InlineKeyboardButton("1️⃣ Как вызвать такси?", callback_data="faq_0")],
        [InlineKeyboardButton("2️⃣ Где обменять деньги?", callback_data="faq_1")],
        [InlineKeyboardButton("3️⃣ Как вести себя в храме?", callback_data="faq_2")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="main")],
    ]
    return InlineKeyboardMarkup(kb)


# Меню еды
def food_menu():
    kb = [
        [InlineKeyboardButton("1️⃣ Wenchang Chicken", callback_data="food_0")],
        [InlineKeyboardButton("2️⃣ Hele Crab", callback_data="food_1")],
        [InlineKeyboardButton("3️⃣ Coconut Rice", callback_data="food_2")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="main")],
    ]
    return InlineKeyboardMarkup(kb)
