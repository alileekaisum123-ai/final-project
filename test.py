from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8847199635:AAEAC4aCmEepIKm2NNOIskKnQ17itltJbU8"


class Country:
    def __init__(self, capital: str, population: str, currency: str, region: str):
        self.capital = capital
        self.population = population
        self.currency = currency
        self.region = region
    def __str__(self):
        return f" 🏛 Capital\t\t: {self.capital}\n 👥 Population\t\t: {self.population}\n 🪙Currency\t\t: {self.currency}\n 📍 Region\t\t: {self.region}"

    


DATA = {
    "cambodia": Country("Phnom Penh", "16.9 million", "Riel (KHR)", "Southeast Asia"),
    "japan": Country("Tokyo", "125.1 million", "Yen (JPY)", "East Asia"),
    "france": Country("Paris", "67.7 million", "Euro (EUR)", "Western Europe"),
}


async def reply_capital(update: Update, context: ContextTypes.DEFAULT_TYPE):
    country = update.message.text.strip().lower()
    info = DATA.get(country)

    if info:
        await update.message.reply_text(str(info))
    else:
        await update.message.reply_text(
            f"❌ '{update.message.text}' doesn't look like a valid country name. Try again!"
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_capital))
app.run_polling()