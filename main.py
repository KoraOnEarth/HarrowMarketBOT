import discord
from discord.ext import commands
import settings

logger = settings.logging.getLogger("bot")

async def is_developer(ctx):
    return ctx.author.id == settings.DEV_ID



def run():
    intents=discord.Intents.default()
    intents.message_content=True
    intents.members=True

    bot = commands.Bot(command_prefix="!", intents=intents, activity=discord.Game('мониторинг Warframe Market', status=discord.Status.online))

    @bot.event
    async def on_ready():
        logger.info(f'User: {bot.user} (ID: {bot.user.id}')
        logger.info(f"Guild ID: {bot.guilds[0].id}")
        print("---------")
        for cog_file in settings.COGS_DIR.glob("*.py"):
            if cog_file != "__init__.py":
                await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

        # bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        # await bot.tree.sync(guild=settings.GUILDS_ID)

    @bot.command()
    @commands.check(is_developer)
    async def load(ctx, cog: str):
        await bot.load_extension(f"cogs.{cog.lower()}")
        await ctx.send("Success!")

    @load.error
    async def say_error(ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Permission denied")


    @bot.command()
    @commands.check(is_developer)
    async def unload(ctx, cog: str):
        await bot.unload_extension(f"cogs.{cog.lower()}")
        await ctx.send("Success!")

    @unload.error
    async def say_error(ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Permission denied")


    @bot.command()
    @commands.check(is_developer)
    async def reload(ctx, cog: str):
        await bot.reload_extension(f"cogs.{cog.lower()}")
        await ctx.send("Success!")

    @reload.error
    async def say_error(ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send("Permission denied")

    bot.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()