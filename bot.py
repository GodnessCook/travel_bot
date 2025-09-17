import os
import requests
import datetime
import math
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    KeyboardButton, ReplyKeyboardMarkup
)
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes
)
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# --- Курсы ---
CNY_TO_UZS = 1700
CNY_TO_USD = 0.14

# --- Координаты для "Где я сейчас?" ---
locations = {
    "Dadonghai": (18.2272, 109.5167),
    "SanyaBay": (18.2369, 109.4517),
    "YalongBay": (18.2333, 109.6333),
    "Wuzhizhou": (18.3139, 109.7958),
    "MonkeyIsland": (18.4080, 109.7790),
    "Nanshan": (18.3011, 109.2067),
    "Tianya": (18.2992, 109.3606),
    "RomancePark": (18.2803, 109.5053),
    "Yanoda": (18.5100, 109.7000),
    "Atlantis": (18.3040, 109.7970),
    "PhoenixIsland": (18.2267, 109.5097),
}

# --- Данные по дням ---
days = {
    1: {
        "title": "День 1 — Дадунхай и Санья Бэй",
        "schedule": [
            "09:00 – выход из отеля",
            "09:10 – пляж Дадунхай (пешком 10 мин)",
            "12:00 – обед в кафе (~60–100 CNY)",
            "16:00 – такси в Санья Бэй (~20 CNY, 20 мин)",
            "20:00 – возвращение в отель"
        ],
        "cafes": ["Dadonghai Cafe (~60 CNY)", "Seafood Grill (~100 CNY)"],
        "budget": {"taxi": 20, "food": 150, "tickets": 0},
        "checklist": ["Паспорт", "Купальник", "Солнцезащитный крем", "Репеллент"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Dadonghai+Beach/Sanya+Bay/",
        "photos": ["photos/day1_1.jpg", "photos/day1_2.jpg"],
        "advice": "⚡ Вечером в Санья Бэй могут быть комары."
    },
    2: {
        "title": "День 2 — Ялонг Бэй",
        "schedule": [
            "09:00 – выезд из отеля",
            "09:40 – прибытие на Ялонг Бэй (такси ~80 CNY)",
            "12:30 – обед",
            "18:00 – возвращение в отель (~80 CNY)"
        ],
        "cafes": ["Beach Bar (~100 CNY)", "Fish Restaurant (~150 CNY)"],
        "budget": {"taxi": 160, "food": 120, "tickets": 0},
        "checklist": ["Купальник", "Очки", "Шлёпанцы"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Yalong+Bay/",
        "photos": ["photos/day2_1.jpg", "photos/day2_2.jpg"],
        "advice": "⚡ Берите зонт – мало тени."
    },
    3: {
        "title": "День 3 — Вужичжоу + Остров Обезьян",
        "schedule": [
            "08:00 – выезд из отеля",
            "09:00 – паром на Вужичжоу (~150 CNY)",
            "13:00 – такси к Острову Обезьян (~100 CNY)",
            "14:00 – канатная дорога (~120 CNY)",
            "18:00 – возвращение в отель"
        ],
        "cafes": ["Island Snack (~50 CNY)", "Seafood Cafe (~100 CNY)"],
        "budget": {"taxi": 200, "food": 100, "tickets": 270},
        "checklist": ["Фотоаппарат", "Шляпа", "Удобная обувь"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Wuzhizhou+Island+Wharf/Nanwan+Monkey+Island/",
        "photos": ["photos/day3_1.jpg", "photos/day3_2.jpg"],
        "advice": "⚡ Зарядите телефон – много фото!"
    },
    4: {
        "title": "День 4 — Наньшань + Край света",
        "schedule": [
            "08:30 – выезд из отеля",
            "09:30 – Наньшань (~120 CNY)",
            "13:00 – обед в Veggie Temple",
            "15:00 – Край света (~100 CNY)",
            "19:00 – возвращение в отель"
        ],
        "cafes": ["Veggie Temple (~60 CNY)", "Sea View Cafe (~90 CNY)"],
        "budget": {"taxi": 250, "food": 120, "tickets": 220},
        "checklist": ["Скромная одежда", "Головной убор"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Nanshan+Temple/Tianya+Haijiao/",
        "photos": ["photos/day4_1.jpg", "photos/day4_2.jpg"],
        "advice": "⚡ В храме закрывать плечи и колени."
    },
    5: {
        "title": "День 5 — Romance Park + Yanoda",
        "schedule": [
            "09:00 – выезд из отеля",
            "09:30 – Romance Park (~280 CNY)",
            "13:00 – такси в Yanoda (~100 CNY)",
            "14:00 – прогулка (~130 CNY)",
            "19:00 – возвращение в отель"
        ],
        "cafes": ["Rainforest Cafe (~80 CNY)", "Local Dishes (~100 CNY)"],
        "budget": {"taxi": 200, "food": 120, "tickets": 410},
        "checklist": ["Удобная обувь", "Репеллент", "Фотоаппарат"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Sanya+Romance+Park/Yanoda+Rainforest+Park/",
        "photos": ["photos/day5_1.jpg", "photos/day5_2.jpg"],
        "advice": "⚡ Возьмите репеллент."
    },
    6: {
        "title": "День 6 — Атлантис + Phoenix Island",
        "schedule": [
            "10:00 – выезд из отеля",
            "10:30 – Атлантис (~350 CNY)",
            "14:00 – обед",
            "16:00 – прогулка по Phoenix Island",
            "20:00 – возвращение в отель"
        ],
        "cafes": ["Atlantis Food Court (~120 CNY)", "Island Cafe (~150 CNY)"],
        "budget": {"taxi": 150, "food": 150, "tickets": 350},
        "checklist": ["Фотоаппарат", "Лёгкая одежда"],
        "map": "https://www.google.com/maps/dir/Sanya+Tibet+Hotel/Atlantis+Sanya/Phoenix+Island/",
        "photos": ["photos/day6_1.jpg", "photos/day6_2.jpg"],
        "advice": "⚡ Вечером красиво для фото."
    },
}

# --- Главное меню ---
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📅 План по дням", callback_data="plan_menu")],
        [InlineKeyboardButton("🌦 Погода", callback_data="weather")],
        [InlineKeyboardButton("📊 Общий бюджет", callback_data="total_budget")],
        [InlineKeyboardButton("💱 Конвертер валют", callback_data="converter")],
        [InlineKeyboardButton("📍 Где я сейчас?", callback_data="where_am_i")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[KeyboardButton("📍 Отправить локацию", request_location=True)]]
    await update.message.reply_text("Привет! Я твой гид по Санье 🌴", reply_markup=main_menu())
    await update.message.reply_text("Чтобы я показал ближайшие локации, отправь свою геопозицию.",
                                    reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True))

# --- Показ дня ---
async def show_day(update: Update, context: ContextTypes.DEFAULT_TYPE, day: int, photo_index: int = 0):
    d = days[day]
    budget = d["budget"]
    text = f"✨ {d['title']}\n\n" \
           f"🕐 План:\n- " + "\n- ".join(d["schedule"]) + "\n\n" \
           f"🍴 Где поесть:\n- " + "\n- ".join(d["cafes"]) + "\n\n" \
           f"📊 Бюджет:\n🚖 Такси: {budget['taxi']} CNY\n🍴 Еда: {budget['food']} CNY\n🎟 Билеты: {budget['tickets']} CNY\n" \
           f"💰 Итого: {sum(budget.values())} CNY\n\n" \
           f"🎒 Чек-лист:\n- " + "\n- ".join(d["checklist"]) + "\n\n" \
           f"{d['advice']}\n\n🗺 Маршрут: {d['map']}"

    kb = [
        [InlineKeyboardButton("⬅️ Фото", callback_data=f"photo_{day}_{(photo_index-1)%len(d['photos'])}"),
         InlineKeyboardButton("➡️ Фото", callback_data=f"photo_{day}_{(photo_index+1)%len(d['photos'])}")],
        [InlineKeyboardButton("⬅️ Назад", callback_data="plan_menu")],
        [InlineKeyboardButton("🏠 Главное меню", callback_data="home")]
    ]

    with open(d["photos"][photo_index], "rb") as photo:
        await update.callback_query.message.reply_photo(photo, caption=text, reply_markup=InlineKeyboardMarkup(kb))

# --- Общий бюджет ---
async def total_budget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    taxi = sum(d["budget"]["taxi"] for d in days.values())
    food = sum(d["budget"]["food"] for d in days.values())
    tickets = sum(d["budget"]["tickets"] for d in days.values())
    total = taxi + food + tickets
    text = f"📊 Общий бюджет (6 дней):\n🚖 Такси: {taxi} CNY\n🍴 Еда: {food} CNY\n🎟 Билеты: {tickets} CNY\n💰 Итого: {total} CNY"
    await safe_edit(update.callback_query, text, [[InlineKeyboardButton("🏠 Главное меню", callback_data="home")]])

# --- Погода ---
async def get_weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        res = requests.get("https://wttr.in/Sanya?format=3&lang=ru")
        text = "🌦 Погода: " + res.text
    except:
        text = "🌦 Погода недоступна."
    await safe_edit(update.callback_query, text, [[InlineKeyboardButton("🏠 Главное меню", callback_data="home")]])

# --- Конвертер ---
async def converter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await safe_edit(update.callback_query, "💱 Введи сумму в CNY:", [[InlineKeyboardButton("🏠 Главное меню", callback_data="home")]])
    context.user_data["awaiting_amount"] = True

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_amount"):
        try:
            amount = float(update.message.text)
            uzs = amount * CNY_TO_UZS
            usd = amount * CNY_TO_USD
            await update.message.reply_text(f"💱 {amount} CNY = {uzs:,} UZS ≈ {usd:.2f} USD")
        except:
            await update.message.reply_text("⚠️ Ошибка. Введи число.")
        context.user_data["awaiting_amount"] = False

# --- Где я сейчас ---
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = map(math.radians, [lat1, lat2])
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R*2*math.atan2(math.sqrt(a), math.sqrt(1-a))

async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_loc = update.message.location
    distances = {name: haversine(user_loc.latitude, user_loc.longitude, lat, lon) for name, (lat, lon) in locations.items()}
    nearest = min(distances, key=distances.get)
    await update.message.reply_text(f"📍 Ближайшая локация: {nearest} ({distances[nearest]:.1f} км)")

# --- Safe edit ---
async def safe_edit(query, text, kb):
    try:
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb))
    except:
        try:
            await query.message.delete()
        except:
            pass
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb))

# --- Callback ---
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if data == "home":
        await safe_edit(update.callback_query, "🏠 Главное меню", main_menu().inline_keyboard)
    elif data == "plan_menu":
        kb = [[InlineKeyboardButton(days[i]["title"], callback_data=f"plan_{i}")] for i in days]
        kb.append([InlineKeyboardButton("🏠 Главное меню", callback_data="home")])
        await safe_edit(update.callback_query, "📅 Выбери день:", kb)
    elif data.startswith("plan_"):
        day = int(data.split("_")[1])
        await show_day(update, context, day)
    elif data.startswith("photo_"):
        _, d, idx = data.split("_")
        await show_day(update, context, int(d), int(idx))
    elif data == "weather":
        await get_weather(update, context)
    elif data == "total_budget":
        await total_budget(update, context)
    elif data == "converter":
        await converter(update, context)
    elif data == "where_am_i":
        await update.callback_query.message.reply_text("📍 Отправь мне свою локацию кнопкой ниже ⬇️")

# --- MAIN ---
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
