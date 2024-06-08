import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='&' , intents=discord.Intents.all())

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('Sae'))
  print('Logged in as {0.user}'.format(client))

@client.command(aliases=['p', 'q'])
async def ping(ctx, arg=None):
  if arg == "pong":
    await ctx.send('hello')

  else:
    await ctx.send(f'Pong: {round(client.latency * 1000)}ms')

keep_alive()
client.run(os.getenv('TOKEN'))
