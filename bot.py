import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
URL = "https://mohammedzeony20-cell.github.io/Live_bot"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    btn = [[InlineKeyboardButton("💕 Do you love me?", web_app=WebAppInfo(url=URL))]]
    await update.message.reply_text("🐻 اضغط هنا! 👇", reply_markup=InlineKeyboardMarkup(btn))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
