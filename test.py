from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8990436863:AAGqLR3ufXDPocPYDo9LbAqfzKcyqa8nCEA"


class Planet:
    def __init__(
        self,
        kind: str,
        diameter: str,
        moons: str,
        gravity: str,
        day_length: str,
        year_length: str,
        temperature: str,
        atmosphere: str,
        distance: str,
    ):
        self.kind = kind
        self.diameter = diameter
        self.moons = moons
        self.gravity = gravity
        self.day_length = day_length
        self.year_length = year_length
        self.temperature = temperature
        self.atmosphere = atmosphere
        self.distance = distance

    def __str__(self):
        return (
            f" 🪐 Type\t\t: {self.kind}\n"
            f" 📏 Diameter\t\t: {self.diameter}\n"
            f" 🌙 Moons\t\t: {self.moons}\n"
            f" ⚖️ Gravity\t\t: {self.gravity}\n"
            f" ⏱ Day length\t\t: {self.day_length}\n"
            f" 📅 Year length\t\t: {self.year_length}\n"
            f" 🌡 Avg temp\t\t: {self.temperature}\n"
            f" 💨 Atmosphere\t\t: {self.atmosphere}\n"
            f" ☀️ From Sun\t\t: {self.distance}"
        )



DATA = {
    "mercury": Planet(
        "Rocky", "4,879 km", "0", "3.7 m/s²", "176 Earth days", "88 Earth days",
        "167 °C", "Almost none (thin exosphere)", "58 million km",
    ),
    "venus": Planet(
        "Rocky", "12,104 km", "0", "8.9 m/s²", "243 Earth days (retrograde)", "225 Earth days",
        "464 °C", "CO₂ with sulfuric acid clouds", "108 million km",
    ),
    "earth": Planet(
        "Rocky", "12,742 km", "1", "9.8 m/s²", "24 hours", "365.25 days",
        "15 °C", "Nitrogen + oxygen", "150 million km",
    ),
    "mars": Planet(
        "Rocky", "6,779 km", "2", "3.7 m/s²", "24.6 hours", "687 Earth days",
        "-63 °C", "Thin CO₂", "228 million km",
    ),
    "jupiter": Planet(
        "Gas giant", "139,820 km", "101", "24.8 m/s²", "9.9 hours", "11.9 Earth years",
        "-110 °C", "Hydrogen + helium", "778 million km",
    ),
    "saturn": Planet(
        "Gas giant", "116,460 km", "285", "10.4 m/s²", "10.7 hours", "29.4 Earth years",
        "-140 °C", "Hydrogen + helium", "1.43 billion km",
    ),
    "uranus": Planet(
        "Ice giant", "50,724 km", "28", "8.7 m/s²", "17.2 hours (retrograde)", "84 Earth years",
        "-195 °C", "Hydrogen, helium, methane", "2.87 billion km",
    ),
    "neptune": Planet(
        "Ice giant", "49,244 km", "16", "11.2 m/s²", "16.1 hours", "164.8 Earth years",
        "-200 °C", "Hydrogen, helium, methane", "4.50 billion km",
    ),
}


async def reply_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    planet = update.message.text.strip().lower()
    info = DATA.get(planet)

    if info:
        await update.message.reply_text(str(info))
    else:
        await update.message.reply_text(
            f"❌ '{update.message.text}' doesn't look like a valid planet name. Try again!\n"
            f"Known planets: {', '.join(name.title() for name in DATA)}"
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_info))
app.run_polling()
