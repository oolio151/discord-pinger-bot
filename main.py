import discord
from discord.ext import commands, tasks
import time
import os
import sys
client = discord.Client()
bot = commands.Bot(command_prefix="gao ")

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="with david's mom"))
  print("bot online")

@bot.command(
  help="Set person to ping",
  brief="Set person to ping",
  alias="sp"
)
async def setperson(ctx, user: discord.Member):
  global person
  person=user
  if user=="@everyone":
    await ctx.send("Sorry, you cannot register everyone")
    time.sleep(1)
    await ctx.message.delete()
  else:
    await ctx.send("{} is registered".format(user))
  
@bot.command(
  brief="Check target to be pinged",
  help="Check who is set to be pinged"
)  
async def test(ctx):
  try:
    await ctx.send(person)
  except:
    await ctx.send("Error")

@bot.command(
  help="One time ping for troubleshooting and testing",
  brief="One time ping"
)
async def oneping(ctx):
  try:
    await ctx.send(person.mention)
  except:
    await ctx.send("You have not set a person to ping")

@bot.command(
  help="real deal",
  brief="real deal"
)
async def ping(ctx,times):
  try:
    if person.id==549634577044340747:
      await ctx.send("Sorry, this command does not work on this person")
    else:
      for i in range(1,int(times)):
        await ctx.send(person.mention)
        time.sleep(1)
  except:
    await ctx.send("Error")
    
@bot.command()
async def restart(ctx):
  if ctx.author.id == 549634577044340747 or ctx.author.id == 922282746225774604:
    await ctx.send("Restarting Bot")
    os.execv(sys.executable, ['python'] + sys.argv)
  else:
    await ctx.send("You are not authorized to run this command")

bot.run(os.environ['TOKEN'])
