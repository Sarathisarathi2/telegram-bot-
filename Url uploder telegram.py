import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the URL uploader bot! Send me a URL link to a file to upload.")

def upload_file(update, context):
    url = update.message.text
    response = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(filename, "rb"))
    context.bot.send_message(chat_id=update.effective_chat.id, text="File uploaded successfully!")
    os.remove(filename)

def main():
    updater = Updater(token='6280672598:AAEClKBN-liRYpiR9xb_DLT6HLdYcWw6cUQ', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.regex('^(http|https):\/\/'), upload_file))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
