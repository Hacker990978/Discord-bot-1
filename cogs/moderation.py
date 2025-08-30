import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 🔨 Kick
    @app_commands.command(name="kick", description="Kick a member from the server")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"👢 {member} was kicked. Reason: {reason}", ephemeral=True)

    # 🔨 Ban
    @app_commands.command(name="ban", description="Ban a member from the server")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"🔨 {member} was banned. Reason: {reason}", ephemeral=True)

    # 🔓 Unban
    @app_commands.command(name="unban", description="Unban a member")
    async def unban(self, interaction: discord.Interaction, user_id: int):
        user = await self.bot.fetch_user(user_id)
        await interaction.guild.unban(user)
        await interaction.response.send_message(f"✅ {user} was unbanned.", ephemeral=True)

    # 🧹 Clear Messages
    @app_commands.command(name="clear", description="Clear messages in a channel")
    async def clear(self, interaction: discord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"🧹 Cleared {amount} messages!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
