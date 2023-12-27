categories = ["абонемент на изучение английского", "разные вкусняшки", "фитнес-браслет", "набор для лепки из глины", "чехол на телефон", "свитер", "билет на выставку"]
questions = {1: "Чем занимаешься в свободное время?",
             2: "На какой бюджет подарка расчитываешь?",
             3: "Что больше всего ценишь в жизни(главное не задумывайся слишком сильно)?",
             4: "Что самое важное в подарке",
             5: "Какой любимые предмет был/есть в школе?",
             6: "Какая категория подарков близка?"}
answers = {1: ["Саморазвиваюсь", "Гуляю с друзьями", "Играю в игры на компе", "Играю в спортивные игры на улице", "Люблю поделать что-то своими руками", "Смотрю сериалы/фильмы/видео на Ютубчике"],
           2: ["500-1000 руб", "1000-3000 руб", "3000-6000 руб"],
           3: ["Друзей, родственников", "Усовершенствование себя", "Мою внешность", "Путешествия"],
           4: ["Воспоминания о празнике", "Красота", "Функциональность", "Эмоциии дарящего"],
           5: ["Математика", "Информатика", "Литература", "Физра", "Английский", "ИЗО"],
           6: ["Предмет", "Поход в какое-то новое место", "Абонемент"]}
#В зависимости от ответа начасляются баллы к каждой из категорий
rate = {1: [[6, 0, 1, 1, 1, 0, 4], [0, 1, 3, 0, 2, 1, 2], [0, 0, 0, 0, 3, 1, 0], [0, 0, 3, 0, 1, 0, 0], [1, 1, 0, 6, 1, 1, 2], [1, 6, 0, 1, 0, 3, 0]],
        2: [[0, 7, 2, 2, 7, 1, 0], [1, 1, 3, 5, 0, 4, 2], [7, 0, 0, 2, 0, 1, 4]],
        3: [[0, 1, 0, 1, 2, 0, 4], [6, 1, 6, 4, 0, 0, 6], [0, 0, 7, 0, 3, 7, 2], [7, 0, 4, 0, 0, 0, 3]],
        4: [[0, 3, 0, 5, 0, 6, 0], [0, 0, 0, 4, 3, 3, 2], [5, 0, 6, 0, 7, 0, 0], [0, 0, 0, 0, 0, 0, 0]],
        5: [[0, 0, 0, 0, 0, 0, 2], [3, 0, 0, 0, 4, 0, 0], [1, 0, 0, 0, 0, 1, 2], [0, 0, 5, 0, 0, 0, 0], [8, 0, 0, 0, 0, 0, 0], [1, 1, 0, 8, 1, 0, 5]],
        6: [[0, 6, 6, 6, 7, 6, 0], [1, 0, 1, 0, 0, 0, 8], [8, 0, 0, 2, 0, 0, 4]]}
media = {"абонемент на изучение английского": "https://imgur.com/IE70poI", "разные вкусняшки": "https://imgur.com/0jAjYJq", "фитнес-браслет": "https://imgur.com/VRjUN9c", "набор для лепки из глины": "https://imgur.com/e70PJtz", "чехол на телефон": "https://imgur.com/IgksXyN", "свитер": "https://imgur.com/xuclDL2", "билет на выставку": "https://imgur.com/GaALYDn"}