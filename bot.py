from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7939511701:AAE87lvxWicGinme7aI_z68p_eETt5Pw2Xc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    name = user.first_name or "Teman"

    # tombol inline
    keyboard = [
        [InlineKeyboardButton("DAFTAR DISINI 🎉", url="https://t.ly/betcoin")],
        [InlineKeyboardButton("HUBUNGI MIMIN 🥰", url="https://direct.lc.chat/1284")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # kirim foto + caption + tombol
    with open("banner.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=(
                f"Halo {name}, akhirnya kamu gabung juga! 🥰\n\n"
                "Jangan lupa daftar dan main di [Betcoin](https://t.me/BetcoinAsia) 💧"
            ),
            reply_markup=reply_markup,
            parse_mode="Markdown"  # biar link jadi klikable
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot sudah jalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
