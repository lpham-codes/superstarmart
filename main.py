# ------------------------------------------
# SUPER STAR MART BOT - BASIC STARTER
# Telegram Stars Store (skeleton)
# ------------------------------------------

import logging
from telegram import (
    Update, InlineKeyboardMarkup, InlineKeyboardButton,
    LabeledPrice
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, PreCheckoutQueryHandler
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

BOT_TOKEN = "7997403475:AAESngpsopLXiZr4iVfqDbLy0XFj7kCFsjg"
PROVIDER_TOKEN = ""  # Stars Payments

# ------------------------------------------
# START COMMAND
# ------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⭐ Stickers", callback_data="cat_stickers")],
        [InlineKeyboardButton("🖼 Wallpapers", callback_data="cat_wallpapers")],
        [InlineKeyboardButton("😎 Avatars", callback_data="cat_avatars")],
        [InlineKeyboardButton("😂 Memes", callback_data="cat_memes")],
        [InlineKeyboardButton("🎁 Gifts", callback_data="cat_gifts")],
    ]

    await update.message.reply_text(
        "⭐ *WELCOME TO SUPER STAR MART* ⭐\n\n"
        "Buy digital goods using Telegram Stars.\n"
        "Choose a category below:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

# ------------------------------------------
# BOOTSTRAP
# ------------------------------------------

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if _name_ == "_main_":
    main()
