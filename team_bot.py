from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ⬇️ Вставь сюда токен от BotFather
TOKEN = '8172053890:AAHQOzGj82DzrW1ELbK8CuBNFm9PvM3Tx_s'  # ⬅️

# ⬇️ Сюда впиши юзернеймы людей, которых нужно тегать
TEAM = [
    '@mrxrio13', '@katya_21k', '@AlenCinq', '@umertviee', '@anereminaa',
    '@mikassaxd', '@frontendri', '@Antohaha90', '@SeroevaAV', '@anmalva',
    '@Morkovka228', '@Blezzzzzzor', '@Poposha_25', '@ollkull', '@serafi_mao',
    '@alyonyshka_b', '@heyhedgehog',  # запятая после nick
    '@FrankIinSAint', '@Killllreal', '@lararri', '@gordonsix', '@polliwww20'
]
async def call_team(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mention_text = ' '.join(TEAM)
    await update.message.reply_text(f'{mention_text}, ПРОСЬБА ПОДКЛЮЧИТЬСЯ 1 ЧЕЛОВЕКА ОТ 30 МИНУТ ДЛЯ УСИЛЕНИЯ! 🔔')

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler('callteam', call_team))

print("✅ Бот запущен. Ожидаю команду /callteam")
app.run_polling()


