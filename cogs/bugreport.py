import discord
from discord.ext import commands
from discord import app_commands
import settings

class FeedbackModal(discord.ui.Modal, title="Отправьте нам Ваш отзыв!"):
    fb_title = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label="Title",
        required=True,
        min_length=5,
        max_length=100,
        placeholder="Дайте заголовок Вашему сообщению!"
    )

    fb_message = discord.ui.TextInput(
        style=discord.TextStyle.long,
        label="Message",
        required=True,
        min_length=10,
        max_length=500,
        placeholder="Если Вы хотите - укажите в сообщении свой DiscordTag или электронную почту!"
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = interaction.guild.get_channel(settings.FEEDBACK_CH)

        embed = discord.Embed(title="Новый отчёт", color=discord.Colour.light_grey())
        embed.add_field(name="Заголовок", value=self.fb_title.value, inline=False)
        embed.add_field(name="Сообщение", value=self.fb_message.value)
        embed.set_author(name=interaction.user.name)

        await channel.send(embed=embed)
        await interaction.response.send_message(f"Спасибо за твой вклад, {interaction.user.mention}!", ephemeral=True)

    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(f"Возникла непредвиденная ошибка, {error}", ephemeral=True)

class BugReport(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        description="Отправить багрепорт"
    )
    async def bugreport(self, interaction: discord.Interaction):
        feedback_modal = FeedbackModal()
        feedback_modal.user = interaction.user
        await interaction.response.send_modal(feedback_modal)
        
        

async def setup(bot):
    await bot.add_cog(BugReport(bot))