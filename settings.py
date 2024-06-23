
# ===================== Here you can change the bot settings =====================
embed_color = "" # Hex color for the embeds, without the #
footer = "" # Footer text for the embeds
# ================================================================================


# ===================== Do Not Change this part below =====================
from imports import *

# Transform the embed color into an integer for the embeds
if embed_color == "":
    embed_color = "f0f0f0"
embed_color = int("0x" + embed_color, 16)