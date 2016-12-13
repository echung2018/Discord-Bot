import discord
import asyncio
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!cat'):
        dir = 'Data\Images\Cats'
        filename = random.choice(os.listdir(dir))
        await client.send_file(message.channel,'Data\Images\Cats\\' + filename)

client.run('MjU1NzI3MDQxMTg4NDYyNTky.CynueQ.G_p98nuLKEhuYXMipx2n1ZYYPwU')