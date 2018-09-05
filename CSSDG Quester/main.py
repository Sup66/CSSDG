import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='Un bot special conceput pentru Sectantii CCSDG.')

@bot.event
async def on_ready():
    print('Logat ca')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def salut(ctx):
    await ctx.send(":smiley: :wave: Hai salut, coaie!")
    await ctx.send(":smiley:Tot virgin, tot virgin?:smiley:")

@bot.command()
async def curve(ctx):
    await ctx.send("Ah, vrei sa futi si tu ceva no?:ok_hand::point_left:")
    await ctx.send("Ia d-aici sectantul meu, prietenii la nevoie se cunosc :heart:")
    await ctx.send("https://www.publi24.ro/anunturi/matrimoniale/")
    

bot.run('<TOKEN>')