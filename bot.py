import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "373526599:AAHtyEkcyL8CLFIKo5YWnR4X0IZC-PF7mA0")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://weareuna.github.io/mint_tma/")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Create WebAppInfo object
    web_app = WebAppInfo(url=WEBAPP_URL)
    
    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("Play in 1 click", web_app=web_app)],
        [InlineKeyboardButton("Follow us on X ", url="https://x.com/MintDotIO")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with inline keyboard
    await update.message.reply_text(
        "Welcome to Mint.io! \n\nDescription here!",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    