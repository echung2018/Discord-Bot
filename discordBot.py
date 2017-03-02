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
    if message.content.startswith('!cat'):
        dir = 'Data\Images\Cats'
        filename = random.choice(os.listdir(dir))
        await client.send_file(message.channel,'Data\Images\Cats\\' + filename)
        print('working')
        
    elif message.content.startswith('!youtube '):
        query = message.content[len('!youtube '):]
        searchLink = 'https://www.youtube.com/results?search_query=' + query.replace(' ', '+')
        html_content = urllib.request.urlopen(searchLink).read()

        link = re.findall(r'/watch\?v=\w+"', html_content.decode())
        
    
        await client.send_message(message.channel,  'https://www.youtube.com' + link[0][:-1])
'''
	elif message.content.startswith('!xkcd'):
		query = message.content[len('!xkcd '):]
		val += 1
		if(query == null):
			html_content = urllib.request.urlopen('https://www.xkcd.com').read()
			ass = re.search(r'Permanent link to this comic: https://xkcd\.com/+/', html_content.decode())
			currxkcd = int(ass.group(1))
			xkcdNumb = int(random.random()*currxkcd)
			link = "https://xkcd.com/%s" % (xkcdNumb)
			html_content = urllib.request.urlopen('link').read()
			titties = re.search(r'Image URL (for hotlinking/embedding): +png', html_content.decode())
			pictureLink = titties.group(1) + "png"
			urllib.request.urlretrieve(pictureLink, "Data\Cache\xkcd" + xkcdNumb + ".png")

'''     
client.run('MjU1NzI3MDQxMTg4NDYyNTky.CynueQ.G_p98nuLKEhuYXMipx2n1ZYYPwU')











