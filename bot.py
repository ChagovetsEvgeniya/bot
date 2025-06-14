import logging
import datetime
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Налаштування логування
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен бота з BotFather
TOKEN = "7665462092:AAEuWCTSVo-G6MazkkQuJI1Twqga6crfJDw"

# Обробники команд (асинхронні функції)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привіт! Я Люмен, твій бот підтримки. Використай /help, щоб подивитись доступні команди."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "/start - Привітання та інструкції\n"
        "/help - Список команд\n"
        "/ping - Щоденний чек-ін\n"
        "/sos - Екстрений режим (дихальні вправи)\n"
        "/music - Трек дня для підняття настрою\n"
        "/quote - Натхненна цитата\n"
        "/settings - Налаштування (поки не реалізовано)"
    )
    await update.message.reply_text(help_text)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    now = datetime.datetime.now().strftime("%H:%M, %d-%m-%Y")
    reply_text = f"Чек-ін від Люмена:\nЗараз {now}. Як ти себе почуваєш?"
    await update.message.reply_text(reply_text)

async def sos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    sos_text = (
        "Режим SOS активовано!\n\n"
        "Спробуй дихальну вправу 4-7-8:\n"
        "1. Вдихни на 4 секунди;\n"
        "2. Затримай дихання на 7 секунд;\n"
        "3. Видихни повільно на 8 секунд.\n"
        "Повтори кілька циклів, щоб заспокоїтись."
    )
    await update.message.reply_text(sos_text)

async def music(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tracks = [
        ("Brave – Sara Bareilles", "https://youtu.be/QUQsqBqxoR4"),
        ("Fight Song – Rachel Platten", "https://youtu.be/xo1VInw-SKc"),
        ("Stronger – Kelly Clarkson", "https://youtu.be/Xn676-fLq7I")
    ]
    track = random.choice(tracks)
    await update.message.reply_text(f"Трек дня: {track[0]}\n{track[1]}")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes = [
        "Найкращий спосіб передбачити майбутнє — створити його.",
        "Ризикуй — і побачиш нові горизонти.",
        "Життя – це пригода, кожен день дарує нові можливості."
    ]
    await update.message.reply_text(random.choice(quotes))

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Налаштування поки що не реалізовано, але я працюю над цим!")

def main():
    application = Application.builder().token(TOKEN).build()

    # Прив'язка обробників команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("sos", sos))
    application.add_handler(CommandHandler("music", music))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("settings", settings_command))

    # Запуск бота методом polling
    application.run_polling()

if __name__ == '__main__':
    main()
