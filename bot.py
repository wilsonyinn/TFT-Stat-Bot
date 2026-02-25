import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#set up and security 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#image mapping
IMAGE_MAP = {
    "chaos": "images/call_to_chaos.png",
    "package": "images/care_package.png",
    "expected": "images/expected_unexpectedness.png",
    "commit": "images/hard_commit.png",
    "lifting": "images/lifting_competition.png",
    "magic": "images/magic_roll.png",
    "missed": "images/missed_connections.png",
    "lives": "images/nine_lives.png",
    "slight": "images/slightly_magical_roll.png",
    "spoils": "images/spoils_of_war.png",
    "egg": "images/the_golden_egg.png",
    "treasure": "images/treasure_hunt.png",
    "warpath": "images/warpath_chest.png",
    "ixtal": "images/ixtal.png",
    "yordles": "images/yordle_grab_bag.png"
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def show(ctx, item: str):
    """Usage: !show <augment_keyword>"""
    item_key = item.lower()

    if item_key in IMAGE_MAP:
        file_path = IMAGE_MAP[item_key]
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                await ctx.send(f"Loot table for **{item_key.capitalize()}**:", file=discord.File(f))
        else:
            await ctx.send(f"Error: File `{file_path}` not found in the local images folder .")
    else:
        # Suggest valid keys if the user makes a typo
        options = ", ".join(IMAGE_MAP.keys())
        await ctx.send(f"Unknown command. Try one of these: {options}")
bot.run(TOKEN)