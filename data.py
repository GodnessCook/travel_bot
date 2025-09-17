# data.py

days = {
    "day1": {
        "title": "🌴 День 1 — Пляжи Санья",
        "steps": [
            {
                "time": "09:00",
                "title": "Пляж Ялонг Бэй",
                "desc": "Белый песок и прозрачная вода.",
                "photo": "photos/day1_1.jpg",
                "map": "https://goo.gl/maps/1yVhSgRtq"
            },
            {
                "time": "13:00",
                "title": "Пляж Дадунхай",
                "desc": "Популярное место с кафе и магазинами.",
                "photo": "photos/day1_2.jpg",
                "map": "https://goo.gl/maps/2yVhSgRtq"
            },
            {
                "time": "17:00",
                "title": "Пляж Санья Бэй",
                "desc": "Закаты и пальмовая аллея.",
                "photo": "photos/day1_3.jpg",
                "map": "https://goo.gl/maps/3yVhSgRtq"
            }
        ],
        "budget": {"taxi": 100, "food": 120, "entry": 0}
    },
    "day2": {
        "title": "🐒 День 2 — Острова и природа",
        "steps": [
            {
                "time": "09:00",
                "title": "Остров Обезьян",
                "desc": "Канатная дорога над морем и прогулка среди обезьян.",
                "photo": "photos/day2_1.jpg",
                "map": "https://goo.gl/maps/4yVhSgRtq"
            },
            {
                "time": "13:00",
                "title": "Остров Вужичжоу",
                "desc": "Рай для дайвинга и снорклинга.",
                "photo": "photos/day2_2.jpg",
                "map": "https://goo.gl/maps/5yVhSgRtq"
            }
        ],
        "budget": {"taxi": 150, "food": 140, "entry": 100}
    },
    "day3": {
        "title": "⛩ День 3 — Храм Наньшань",
        "steps": [
            {
                "time": "09:00",
                "title": "Буддийский центр Наньшань",
                "desc": "Статуя богини Гуаньинь высотой 108 м.",
                "photo": "photos/day3_1.jpg",
                "map": "https://goo.gl/maps/6yVhSgRtq"
            }
        ],
        "budget": {"taxi": 120, "food": 100, "entry": 80}
    },
    "day4": {
        "title": "🏝 День 4 — Остров Феникса и Край света",
        "steps": [
            {
                "time": "10:00",
                "title": "Остров Феникса",
                "desc": "Искусственный остров с небоскрёбами и отелями.",
                "photo": "photos/day4_1.jpg",
                "map": "https://goo.gl/maps/7yVhSgRtq"
            },
            {
                "time": "15:00",
                "title": "Парк Край света",
                "desc": "Романтичное место у моря с каменными глыбами.",
                "photo": "photos/day4_2.jpg",
                "map": "https://goo.gl/maps/8yVhSgRtq"
            }
        ],
        "budget": {"taxi": 140, "food": 120, "entry": 80}
    },
    "day5": {
        "title": "🐬 День 5 — Атлантис и шоу",
        "steps": [
            {
                "time": "10:00",
                "title": "Atlantis Аквариум и дельфинарий",
                "desc": "Огромный океанариум и шоу дельфинов.",
                "photo": "photos/day5_1.jpg",
                "map": "https://goo.gl/maps/9yVhSgRtq"
            },
            {
                "time": "16:00",
                "title": "Sanya Romance Park",
                "desc": "Театрализованные шоу о культуре Хайнаня.",
                "photo": "photos/day5_2.jpg",
                "map": "https://goo.gl/maps/10yVhSgRtq"
            }
        ],
        "budget": {"taxi": 160, "food": 140, "entry": 200}
    },
    "day6": {
        "title": "🌳 День 6 — Природа и шопинг",
        "steps": [
            {
                "time": "09:00",
                "title": "Парк Яноода",
                "desc": "Джунгли, мосты, водопады и этнические шоу.",
                "photo": "photos/day6_1.jpg",
                "map": "https://goo.gl/maps/11yVhSgRtq"
            },
            {
                "time": "14:00",
                "title": "Музей жемчуга",
                "desc": "Знакомство с историей жемчуга, сувениры.",
                "photo": "photos/day6_2.jpg",
                "map": "https://goo.gl/maps/12yVhSgRtq"
            },
            {
                "time": "16:00",
                "title": "Чайные плантации",
                "desc": "Дегустация чая и покупки.",
                "photo": "photos/day6_3.jpg",
                "map": "https://goo.gl/maps/13yVhSgRtq"
            }
        ],
        "budget": {"taxi": 120, "food": 130, "entry": 50}
    }
}

food_guide = {
    "Хайнаньская курица": "Фирменное блюдо – сочная курица с рисом (~60 CNY).",
    "Креветки на пару": "Свежие морепродукты (~80 CNY).",
    "Кокосовый десерт": "Традиционный десерт из кокоса (~30 CNY)."
}

phrasebook = {
    "Еда": {
        "Можно меню?": "请给我菜单 (Qǐng gěi wǒ càidān)",
        "Без острого": "不要辣 (Bù yào là)",
        "Счёт, пожалуйста": "请买单 (Qǐng mǎidān)"
    },
    "Транспорт": {
        "Такси": "出租车 (Chūzūchē)",
        "Сколько стоит поездка?": "去那里多少钱? (Qù nàlǐ duōshǎo qián?)",
        "Остановите здесь": "请在这里停 (Qǐng zài zhèlǐ tíng)"
    },
    "Экстренное": {
        "Помогите!": "救命! (Jiùmìng!)",
        "Позвоните в полицию": "打电话报警 (Dǎ diànhuà bàojǐng)",
        "Аптека": "药店 (Yàodiàn)"
    }
}

faq = {
    "Как вызвать такси?": "Рекомендуем использовать DiDi (аналог Uber в Китае).",
    "Где обменять деньги?": "Лучше всего в банках Китая или официальных обменниках.",
    "Как вести себя в храме?": "Не шуметь, не фотографировать монахов, одеваться скромно."
}
