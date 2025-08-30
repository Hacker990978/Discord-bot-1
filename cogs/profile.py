import discord
from discord.ext import commands
from discord import app_commands

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 🎭 Change Activity
    @app_commands.command(name="setactivity", description="Change the bot's activity")
    async def setactivity(self, interaction: discord.Interaction, activity: str):
        await self.bot.change_presence(activity=discord.Game(name=activity))
        await interaction.response.send_message(f"✅ Activity set to: {activity}", ephemeral=True)

    # 👤 Change Nickname
    @app_commands.command(name="setnick", description="Change the bot's nickname in this server")
    async def setnick(self, interaction: discord.Interaction, nickname: str):
        await interaction.guild.me.edit(nick=nickname)
        await interaction.response.send_message(f"✅ Nickname changed to: {nickname}", ephemeral=True)

    # 🖼️ Change Avatar
    @app_commands.command(name="setavatar", description="Change the bot's avatar (paste an image URL)")
    async def setavatar(self, interaction: discord.Interaction, url: str):
        async with self.bot.http._HTTPClient__session.get(url) as resp:
            if resp.status != 200:
                return await interaction.response.send_message("❌ Failed to fetch image.", ephemeral=True)
            data = await resp.read()
            await self.bot.user.edit(avatar=data)
            await interaction.response.send_message("✅ Avatar updated!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Profile(bot))
