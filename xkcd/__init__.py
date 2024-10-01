from .xkcd import XKCD

async def setup(bot):  # Async setup for Redbot/discord.py 2.0
    n = XKCD(bot)  # Pass the bot instance to the XKCD cog
    await bot.add_cog(n)  # Use 'await' with add_cog for asynchronous behavior
