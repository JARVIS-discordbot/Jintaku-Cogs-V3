from .xkcd import XKCD

async def setup(bot):
    n = XKCD(bot)  # Pass the 'bot' instance to the XKCD class
    bot.add_cog(n)
