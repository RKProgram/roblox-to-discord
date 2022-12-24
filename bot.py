import discord
import socket
import threading
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('127.0.0.1', 6666))

async def recieve(ctx):
    while True:
        try:
            message = socket.recv(1024).decode('ascii')
            await ctx.send(message)

        except Exception as e:
            print(e)

@client.event
async def on_ready():
    print('started')

@client.command(aliases=["listen"])
async def l_isten(ctx):
    await ctx.send("listening")
    thread = threading.Thread(target=asyncio.run, args=(await recieve(ctx),))
    thread.start()

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

client.run("bottoken")
