import telebot, json
from form import categories, answers, questions, rate, media

token = "6536459140:AAH0tFRBtRZelxJHHuCqJbi9aCBQzr3e9KQ"
bot = telebot.TeleBot(token)

help_message = "Я умею: \n/start - начать тестирование(при повторном прохождении произойдет перезапск) \n/help - выводить информацию о моих возможностях"
buttons = {}
for q in answers.keys():
    but_for_ques = {answers[q][i]: {'callback_data': f"{q, i}"} for i in range(len(answers[q]))}
    buttons[q] = telebot.util.quick_markup(but_for_ques, row_width=1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    id = str(call.from_user.id)
    users = get_info()
    num_of_que, var = map(int, call.data[1:-1].split(", "))
    last = users[id]["last"]
    #проверка на то, что каждый вопрос ответили по 1 разу
    if num_of_que < last:
        bot.send_message(int(id), text="На каждый вопрос можно ответить только 1 раз. Ответь на последний вопрос")
    else:
        ball = rate[num_of_que][var]
        for cat in range(len(categories)):
            users[id]["balls"][categories[cat]] += ball[cat]
        change_info(users)
        last = users[id]["last"]
        if last != len(questions):
            ask_question(id)
        else:
            show_result(id)


@bot.message_handler(commands=['start'])
def start(message):
    id = message.chat.id
    bot.send_message(id, text=f"Привет, {message.from_user.first_name} " + help_message)
    users = get_info()
    balls = {categories[i]: 0 for i in range(len(categories))}
    users[id] = {"last": 0, "balls": balls}
    change_info(users)
    ask_question(id)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_message)

def get_info():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return {}


def change_info(users):
    with open("users.json", "w") as f:
        json.dump(users, f, ensure_ascii=False)


def ask_question(id):
    users = get_info()
    last = users[str(id)]["last"]
    users[str(id)]["last"] += 1
    change_info(users)
    bot.send_message(id, text=questions[last + 1], reply_markup=buttons[last + 1])


def show_result(id):
    users = get_info()
    ball = users[id]["balls"]
    mx_ball = float("-inf")
    for thing in ball.items():
        if thing[1] > mx_ball:
            mx_ball = thing[1]
            present = thing[0]
    bot.send_message(int(id), text=f"По результатам теста больше всего тебе стоит попросить: {present}.")
    bot.send_photo(int(id), photo=media[present])
    bot.send_message(int(id), text = "Спасибо за участие!")

bot.polling()