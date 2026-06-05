import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
URL = "https://mohammedzeony20-cell.github.io/Live_bot"
ADMIN_ID = 7545826713

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    
    btn = [[InlineKeyboardButton("💕 Do you love me?", web_app=WebAppInfo(url=URL))]]
    await update.message.reply_text("🐻 اضغط هنا! 👇", reply_markup=InlineKeyboardMarkup(btn))
    
    await context.bot.send_message(
        chat_id=user.id,
        text="أهلاً! 👋"
    )
    
    username = f"@{user.username}" if user.username else "مش عنده username"
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"👤 دخل حد جديد!\nالاسم: {user.first_name}\nUsername: {username}\nID: {user.id}",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("💬 فتح المحادثة", url=f"tg://user?id={user.id}")
        ]])
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
