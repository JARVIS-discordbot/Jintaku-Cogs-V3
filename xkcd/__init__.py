from .xkcd import XKCD

async def setup(bot):
    n = XKCD()
    bot.add_cog(n)
