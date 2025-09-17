import requests
from datetime import datetime
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


# 🔹 Конвертер валют (CNY → USD → UZS)
def convert_currency(amount_cny: float):
    """
    Конвертирует юани (CNY) в USD и UZS.
    Пример: 100 CNY → (100, 14.0, 175000.0)
    """
    # Можно потом подключить API, пока статично
    cny_to_usd = 0.14   # 1 юань ≈ 0.14 USD
    usd_to_uzs = 12500  # 1 доллар ≈ 12 500 сум

    usd = amount_cny * cny_to_usd
    uzs = usd * usd_to_uzs
    return round(amount_cny, 2), round(usd, 2), round(uzs)


# 🔹 Прогноз погоды через бесплатный сервис wttr.in
def get_weather(city="Sanya"):
    """
    Получает погоду через wttr.in (без API-ключа).
    Возвращает строку, например: '+28°C ☀️ Clear'
    """
    try:
        url = f"https://wttr.in/{city}?format=%t+%C"
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.text.strip()
        return "Нет данных"
    except Exception:
        return "Ошибка погоды"


# 🔹 Автоматическая рассылка плана дня
async def send_daily_plan(app, chat_id, day_data):
    """
    Отправляет утренний план дня с погодой и маршрутом.
    """
    today = datetime.now().strftime("%d.%m.%Y")
    weather = get_weather("Sanya")

    text = f"📅 План на {today}\n\n"
    text += f"🌤 Погода: {weather}\n\n"

    for step in day_data["steps"]:
        text += f"🕘 {step['time']} — {step['title']}\n"

    text += "\n📍 Карта маршрута: " + day_data["steps"][0]["map"]

    kb = [[InlineKeyboardButton("Открыть подробный план", callback_data=day_data["id"])]]

    await app.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=InlineKeyboardMarkup(kb)
    )
