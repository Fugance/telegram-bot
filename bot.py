import telebot
from telebot import types

TOKEN = 'token'
ADMIN_ID = 'Telegram ID'  # Admin's Telegram ID
CHANNEL_ID = '-Channel ID'  # Channel ID

bot = telebot.TeleBot(TOKEN)

submissions = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = ("Привет, тут ты можешь добавить своё предложение новости, пожалуйста, пришли ниже какую-либо новость "
                    "чтобы администрация могла просмотреть твой ответ. Также рекомендуем иногда перезапускать бота.")
    bot.reply_to(message, welcome_text)

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def handle_submission(message):
    content_type = message.content_type
    review_text = "Подтверди или отклони это предложение:"

    if content_type == 'text':
        if len(message.text) < 20:
            bot.reply_to(message, "Ваше сообщение содержит меньше 20 символов. Пожалуйста, отправьте более подробное предложение.")
            return
        submissions[message.message_id] = (message.chat.id, content_type, message.text)
        review_text += f"\n\n{message.text}"
    else:
        file_id = None
        if content_type == 'photo':
            file_id = message.photo[-1].file_id  # Highest resolution photo
        elif content_type == 'video':
            file_id = message.video.file_id
        elif content_type == 'document':
            if message.document.mime_type == 'video/mp4':  # Handling GIFs sent as mp4
                content_type = 'gif'
            file_id = message.document.file_id

        submissions[message.message_id] = (message.chat.id, content_type, file_id)
        bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

    markup = types.InlineKeyboardMarkup()
    approve_button = types.InlineKeyboardButton('Подтвердить', callback_data=f'approve_{message.message_id}')
    reject_button = types.InlineKeyboardButton('Отклонить', callback_data=f'reject_{message.message_id}')
    markup.add(approve_button, reject_button)
    bot.send_message(ADMIN_ID, review_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_approval(call):
    action, message_id = call.data.split('_')
    message_id = int(message_id)
    chat_id, content_type, item = submissions[message_id]

    if action == 'approve':
        if content_type in ['text', 'photo', 'video', 'gif']:
            send_media(CHANNEL_ID, content_type, item)
        bot.answer_callback_query(call.id, "Подтверждено")
    elif action == 'reject':
        bot.send_message(chat_id, "Ваше предложение было отклонено.")
        bot.answer_callback_query(call.id, "Отклонено")

    del submissions[message_id]

def send_media(channel_id, content_type, file_id):
    if content_type == 'text':
        bot.send_message(channel_id, file_id)
    elif content_type == 'photo':
        bot.send_photo(channel_id, file_id)
    elif content_type == 'video' or content_type == 'gif':
        bot.send_video(channel_id, file_id)
    elif content_type == 'document':
        bot.send_document(channel_id, file_id)

bot.infinity_polling()
