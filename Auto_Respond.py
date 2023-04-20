import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(".a0", self_bot=True)

token = input('Your Token:\n>  ')
replyMessage = str(input('Your Message:\n>  '))


loop1 = True
while loop1:
    try:
        UserID = int(input('ID of User to Respond to:\n> '))
        loop1= False
    except:
        print('User ID needs to be valid.. duh')


@bot.event
async def on_ready():
    print('\n               Bot Presence Active')
    print(f'             Logged in as {bot.user}')
    print('\nThis Script was bought to you by the Shadow Government')
    print('                 ant0n#2759 wz here')

@bot.event
async def on_message(message):
    if message.author.id == UserID:
        await message.channel.send(replyMessage)
        print(f'\nResponded to {message.author} with {replyMessage}')


bot.run(token, bot=False)
