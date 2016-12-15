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
        
    
        await client.send_message(message.channel,  'https://www.youtube.com' + link[0][:-1])
        
    elif message.content.startswith('!image '):
        query = message.content[len('!image '):]
        searchLink = 'https://www.google.com/search?q=%s&safe=off&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiLxpGi2vTQAhUFHGMKHVllCfIQ_AUICSgC&biw=1920&bih=901' % query.replace(' ', '+')

        html_content = urllib.request.urlopen(searchLink).read()

        #link = re.findall(r'href="/imgres\?imgurl=\w+&', html_content.decode())
        print(html_content)
'''
def decodeURL(str):
	returnedString = str
    returnedString.replace('%21', '!')
    returnedString.replace('%22', '"')
    returnedString.replace('%23', '#')
    returnedString.replace('%24', '$')
    returnedString.replace('%25', '%')
    returnedString.replace('%26', '&')
    returnedString.replace('%27', '\'')
    returnedString.replace('%28', '(')
    returnedString.replace('%29', ')')
    returnedString.replace(r'%2A', '*')
    returnedString.replace(r'%2B', '+')
    returnedString.replace(r'%2C', '.')
    returnedString.replace(r'%2D', '-')
    returnedString.replace(r'%2E', '.')
    returnedString.replace(r'%2F', '/')
    returnedString.replace(r'%3A', ':')
    returnedString.replace(r'%3B', ';')
    returnedString.replace(r'%3C', '<')
    returnedString.replace(r'%3D', '=')
    returnedString.replace(r'%3E', '>')
    returnedString.replace(r'%3F', '?')

	return returnedString
'''
        
client.run('MjU1NzI3MDQxMTg4NDYyNTky.CynueQ.G_p98nuLKEhuYXMipx2n1ZYYPwU')

