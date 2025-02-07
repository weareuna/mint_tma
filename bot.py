import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot Token & WebApp URL from environment variables
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "373526599:AAHtyEkcyL8CLFIKo5YWnR4X0IZC-PF7mA0")
WEBAPP_URL = os.environ.get("WEBAPP_URL", "https://weareuna.github.io/mint_tma/")

# Your Telegram User ID (Only you can access the bot)
ALLOWED_USER_ID = 1073473563  # Replace with your actual Telegram ID

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id  # Get user ID of the requester

    # Restrict access: Allow only your Telegram user ID
    if user_id != ALLOWED_USER_ID:
        await update.message.reply_text("🚫 Access Denied: This bot is private.")
        return

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
    
    print("Bot is running... (Private Mode Enabled)")
    app.run_polling()

if __name__ == "__main__":
    main()
