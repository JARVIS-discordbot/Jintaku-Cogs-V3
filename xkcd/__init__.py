from .xkcd import XKCD
async def setup(bot):
    cog = XKCD
    await bot.add_cog(cog)
