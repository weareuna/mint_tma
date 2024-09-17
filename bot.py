from telegram import Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import KeyboardButton, ReplyKeyboardMarkup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app = WebAppInfo(url="https://weareuna.github.io/gamefactory_tma/")
    keyboard = [[KeyboardButton("Play Now", web_app=web_app)]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome! Click the button below to play GameFactory",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token("7505688846:AAH1tr0-AzvnofBKZPrfH0qWZOby1knaIhU").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()