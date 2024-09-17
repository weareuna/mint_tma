import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "7505688846:AAH1tr0-AzvnofBKZPrfH0qWZOby1knaIhU")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://weareuna.github.io/gamefactory_tma/")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create WebAppInfo object
    web_app = WebAppInfo(url=WEBAPP_URL)
    
    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("Play in 1 click 🕹️", web_app=web_app)],
        [InlineKeyboardButton("Follow us on X ", url="https://x.com/SlingShotDAO")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with inline keyboard
    await update.message.reply_text(
        "Welcome to the GameFactory! 🦄\n\nUpgrade your factory, boost your production, and race to the top of the leaderboard. The more you produce, the more you win. Invite your friends to earn even more rewards!",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()