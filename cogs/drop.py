import discord
import requests
import json
from discord.ext import commands
from discord import app_commands
from market_functions import warframes_to_url

def get_info_about_item(item):
    url_name = warframes_to_url(item)
    r = requests.get(f"https://api.warframe.market/v1/items/{url_name}/dropsources")
    r_json = r.json()

    with open('dropsources.json', 'w', encoding="utf-8") as file:
        json.dump(r_json, file, indent=4, ensure_ascii=False)


class Drop(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(description="Посмотреть откуда выпадает предмет")
    async def drop(self, interaction: discord.Interaction, item: str):
        get_info_about_item(item)

        await interaction.response.send_message(f"На данный момент команда не работает :<")
        

async def setup(bot):
    await bot.add_cog(Drop(bot))