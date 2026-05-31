from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Saya AI Seller Assistant.\n\n"
        "Kirim nama produk dan saya akan membantu membuat judul Shopee, deskripsi, caption TikTok, dan hashtag."
    )

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    hasil = f"""
🛍 Judul Shopee:
{text} Premium | Viral | Fashion Wanita Terbaru

📝 Deskripsi:
{text} dengan bahan nyaman dipakai sehari-hari, model kekinian dan cocok untuk berbagai aktivitas.

🎵 Caption TikTok:
Model terbaru yang lagi viral! Yuk cek sekarang sebelum kehabisan.

#️⃣ Hashtag:
#fyp #viral #shopee #tiktokshop #fashionwanita
"""

    await update.message.reply_text(hasil)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
