import discord
import os
import random
import urllib.request
import re
import asyncio

client = discord.Client()

 
@client.event
async def on_ready():
	print('Up and running')


@client.event
async def on_message(message):
    if message.content.startswith('!cat '):
        dir = 'Data\Images\Cats'
        filename = random.choice(os.listdir(dir))
        await client.send_file(message.channel,'Data\Images\Cats\\' + filename)
        print('working')
        
    elif message.content.startswith('!youtube '):
        query = message.content[len('!youtube '):]
        searchLink = 'https://www.youtube.com/results?search_query=' + query.replace(' ', '+')
        html_content = urllib.request.urlopen(searchLink).read()

        link = re.findall(r'/watch\?v=\w+"', html_content.decode())
        #search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        
        #html_content.close()
        
        
    
        await client.send_message(message.channel,  'www.youtube.com' + link[0][:-1])
        
    elif message.content.startswith('!image '):
        query = message.content[len('!image '):]
        searchLink = 'https://www.google.com/search?q=%s&safe=strict&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLxpGi2vTQAhUFHGMKHVllCfIQ_AUICSgC&biw=1920&bih=901' % query.replace(' ', '+')
        
client.run('MjU1NzI3MDQxMTg4NDYyNTky.CynueQ.G_p98nuLKEhuYXMipx2n1ZYYPwU')
