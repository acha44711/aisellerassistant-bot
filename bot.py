from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛍 AI Seller Assistant Aktif\n\n"
        "Kirim nama produk.\n"
        "Contoh:\n"
        "Celana kulot wanita premium"
    )

async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    produk = update.message.text

    hasil = f"""
🛍 JUDUL SHOPEE
{produk} Wanita Premium Kekinian Viral Fashion Terbaru

📝 DESKRIPSI
{produk}

✔ Bahan nyaman dipakai
✔ Model kekinian
✔ Cocok untuk aktivitas harian
✔ Jahitan rapi dan nyaman digunakan

🎵 CAPTION TIKTOK
Model terbaru yang lagi banyak dicari 😍
Nyaman dipakai dan cocok untuk berbagai aktivitas.
Yuk cek sekarang sebelum kehabisan!

🏷 HASHTAG
#fyp #viral #shopee #tiktokshop #fashionwanita #kulotwanita
"""

    await update.message.reply_text(hasil)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate))

    app.run_polling()

if __name__ == "__main__":
    main()
