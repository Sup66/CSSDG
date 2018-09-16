import discord
from discord.ext import commands
import quests

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
    # TODO: Scrape publi24 for bitches
    # TODO: Use the scraped info to give user perview of the hoe - Image, Description, Age, Location
    # TODO: Make it so the user can filter by certain criteria (hair:blonde, age:18-25, marime-sani:D?location-radius:5km?)
    await ctx.send("Ah, vrei sa futi si tu ceva no?:ok_hand::point_left:")
    await ctx.send("Ia d-aici sectantul meu, prietenii la nevoie se cunosc :heart:")
    await ctx.send("https://www.publi24.ro/anunturi/matrimoniale/")
    
@bot.command()
async def misiune_info(ctx):
    await ctx.send("Rate: ")
    await ctx.send("Comun: %s" % (quests.Rarities.COMUN))
    await ctx.send("Epic: %s" % (quests.Rarities.EPIC))
    await ctx.send("Legendar: %s" % (quests.Rarities.LEGENDAR))
    await ctx.send("Imposibil %s" % (quests.Rarities.IMPOSIBIL))
    

@bot.command()
async def misiune(ctx):
    # TODO: Show current QUESTs
    # TODO: Start timers, s
    # TODO: 
    #await ctx.send("Misiunea curenta este: %s" % quests.getCurrentQuests())
    

bot.run('<TOKEN>')