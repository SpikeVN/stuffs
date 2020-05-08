import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print('Khởi động thành công!')
    print('Giữ cho của sổ này mở để bot online!')

@bot.event
async def on_member_join(member):
    print(f'{member} đã tham gia sever của chúng ta!')
    await ctx.send(f'Yeah! {member} joined Hydra!')
    await ctx.send(f'Our sever now have {server.member_count} members!') 

@bot.event
async def on_member_remove(member):
    print(f'{member} has left :(')
    await ctx.send(f'{member} has left :(')

@bot.command()
async def lamtoan(ctx, a, b):
    a:int
    b:int
    await ctx.send('Đáp án là ', a + b,' khi làm cộng')
    await ctx.send('Đáp án là ', a - b,' khi làm trừ')
    await ctx.send('Đáp án là ', a * b,' khi làm nhân')
    await ctx.send('Đáp án là ', a / b,' khi làm chia')    
    
bot.run('Njk3MDc1NzIwMzQ1NzQ3NTc3.XpHOgA.YLncbOyuBrhqwW_5WqeHURcq0RA')
