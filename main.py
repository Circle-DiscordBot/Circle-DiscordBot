from settings import *

bot = ezcord.Bot(intents=discord.Intents.all(), language="en")

# Load all command translations
with open("utility/language/commands.yml", encoding="utf-8") as file:
    localizations = yaml.safe_load(file)

# Load english translations of all texts
with open("utility/language/en.yml", encoding="utf-8") as file:
    en = yaml.safe_load(file)

with open("utility/language/de.yml", encoding="utf-8") as file:
    de = yaml.safe_load(file)

# Localization settings
string_locals = {"en": en, "de": de}
ezcord.i18n.I18N(string_locals, fallback_locale="en")

if __name__ == "__main__":
    # Load Extensions and Localize Commands
    bot.load_cogs("extensions", subdirectories=True)
    bot.localize_commands(localizations)

    # Run the bot
    load_dotenv()
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
