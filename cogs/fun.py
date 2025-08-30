
import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # /hello
    @app_commands.command(name="hello", description="Say hello to the bot!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"👋 Hello {interaction.user.mention}!")

    # /roll
    @app_commands.command(name="roll", description="Roll a dice (1-6).")
    async def roll(self, interaction: discord.Interaction):
        number = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 You rolled a **{number}**!")

    # /coinflip
    @app_commands.command(name="coinflip", description="Flip a coin.")
    async def coinflip(self, interaction: discord.Interaction):
        result = random.choice(["Heads", "Tails"])
        await interaction.response.send_message(f"🪙 The coin landed on **{result}**!")

    # /say
    @app_commands.command(name="say", description="Make the bot say something.")
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    # /joke
    @app_commands.command(name="joke", description="Get a random joke.")
    async def joke(self, interaction: discord.Interaction):
        jokes = [
            "Why don’t skeletons fight each other? Because they don’t have the guts.",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field.",
        ]
        await interaction.response.send_message(random.choice(jokes))

async def setup(bot):
    await bot.add_cog(Fun(bot))

