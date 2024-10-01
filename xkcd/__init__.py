

from .xkcd import XKCD


async def setup(bot):
    cog = XKCD(bot)
    await bot.add_cog(cog)
