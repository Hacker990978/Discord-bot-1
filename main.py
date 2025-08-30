import discord
from discord.ext import commands
import os

# --- Setup Bot ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = 1406918069963460728  # Replace with your server ID

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    
    # Load cogs after the bot is ready
    await load_cogs()

    try:
        # Syncing commands after cogs are loaded
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

# --- Load Cogs Asynchronously ---
async def load_cogs():
    # List your cogs here
    initial_cogs = ["fun", "tools", "games", "admin"]  # Add more cogs as required
    
    for cog in initial_cogs:
        try:
            # Asynchronously load cogs
            await bot.load_extension(f"cogs.{cog}")
            print(f"✅ Loaded cog: {cog}")
        except Exception as e:
            print(f"❌ Failed to load cog {cog}: {e}")

# --- Run Bot ---
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("❌ Bot token not found! Set it in Railway Variables.")

bot.run(TOKEN.strip())
