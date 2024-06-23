
# ===================== Here you can change the bot settings =====================
# ------ General settings ------
embed_color = "" # Hex color for the embeds, without the #
footer = "" # Footer text for the embeds

# ------ Moderation settings ------
mod_user_dm = True # Whether to DM the user when they are moderated
mod_log = True # Whether to log the moderation actions
mod_log_channel = 1254407998198251540 # The channel ID to log the moderation actions
# ================================================================================


# ===================== Do Not Change this part below =====================
from imports import *

# Transform the embed color into an integer for the embeds
if embed_color == "":
    embed_color = "f0f0f0"
embed_color = int("0x" + embed_color, 16)
