from redbot.core import commands
from .xkcd import XKCD

async def setup(bot):
    n = XKCD(bot)
    await bot.add_cog(n)
