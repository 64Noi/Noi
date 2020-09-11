import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!') 

@bot.event 
async def on_ready():
    print("실행 완료")

@bot.command()
async def 청소(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@bot.event
async def on_message(message):
    message_content = message.content
    bad = message_content.find("시발")
    print(bad)
    if bad >= 0:
        await message.channel.send("고운 말을 사용해주세요.")
        await message.delete()
    await bot.process_commands(message)

bot.run("")
