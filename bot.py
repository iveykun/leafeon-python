import os
import time
import discord
from dotenv import load_dotenv
from datetime import datetime, timedelta
from threading import Timer
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
token = ''

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')
	await birthday()  # everytime leafeon logs on it checks for bdays
	
'''
@client.event
async def on_member_join(member):  # sends a welcome DM but those are spammy and I hate them
	await member.create_dm()
	await member.dm_channel.send(f"Morning {member.name}! Welcome to the Rewrite Discord server!")
'''

@client.event
async def on_message(message):
	
	if message.author == client.user:
		return
	elif message.content == '|ping':
		await message.channel.send("Pong!")
	elif message.content == '|help':
		await message.channel.send("ping - good - setbday")
	elif message.content == '|good':
		await message.channel.send("Thank you for your praise!")
	elif ('clever girl' or 'good girl') in message.content.lower():
		await message.channel.send("Homete homete!")
		
	elif message.content.lower() == 'cheer up':
		await message.channel.send("Cheer up baby!")
	elif 'happy birthday' in message.content.lower():
		await message.channel.send(f'Happy Birthday! 🎈🎉')	
	elif '|setbday' in message.content:
		if '```' in message.content:
			return
		#await message.channel.send("What is your birthday in MMDD format? Example: July 4 = 0704")
		date = message.content[-4::]
		bday = str(message.author)

		
		f = open("birthdayFile.txt", 'a+')
		for row in f:
			if message.author in row:
				await message.channel.send(f"Your bday is " + row )
				return
		f.write(date + ' ' + bday)
		f.write("\n")
		f.close()
		print("Added to database:", date, bday)
		await message.channel.send(f"Added to database: " + date + ' ' + bday)
		

async def birthday():
	
	channel = client.get_channel(put own channel number heere)
	fileName = open("birthdayFile.txt", 'r')
	today = time.strftime('%m%d')

	for line in fileName:
		if today in line:
			line = line.split(' ')
			
			line[-1] = line[-1].strip()
			if line[-1] != line[1]:
				bdayperson = line[1]+' '+line[2]
			else:
				bdayperson = line[1]
			await channel.send(f"Happy Birthday to "+ bdayperson + "! 🎈🎉" )
	
client.run(token)
