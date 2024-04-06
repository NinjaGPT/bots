import discord
import re
import asyncio

channel_A = 1225880618294111111 # monitor this channel '# general'
channel_B = 1225880692206111111 # send answer to this channel  
# answer BOT's Token
TOKEN = 'xxxx'

intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True  # will be ignore in some versions
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # no response self message
    if message.author == client.user:
        return

    # monitor channel A
    if message.channel.id == channel_A:
        ################# QUESTION ONE - 1
        keywords1 = ['change', 'address', 'order']
        if all(keyword in message.content.lower() for keyword in keywords1):
            # send recommended answer to channel B
            channel_b = client.get_channel(channel_B)

            await channel_b.send(f'[ ❓ ] QUESTION:\n {message.author.name} ===> {message.content}')
            await channel_b.send('[ 🤔 ] RECOMMENDED ANSWER:\nplease email support@product.tech for change of address/refund. Thanks!\n' + '-'*144)

        ################# QUESTION TWO - 2
        keywords2 = ['cancel', 'order']

        if all(keyword in message.content.lower() for keyword in keywords2):
            # send recommended answer to channel B
            channel_b = client.get_channel(channel_B)

            await channel_b.send(f'[ ❓ ] QUESTION:\n {message.author.name} ===> {message.content}')
            await channel_b.send('[ 🤔 ] RECOMMENDED ANSWER:\nplease email support@product.tech for change of address/refund. Thanks!\n' + '-'*144)

        ################# QUESTION BACKUP
        #if re.search(r'@username.*xxx.*ooo', message.content):

            #channel_b = client.get_channel(channel_B)
            #await channel_b.send(f'[ ❓ ] QUESTION:\n {message.author.name} ===> {message.content}')
            #await channel_b.send('[ 🤔 ] RECOMMEND ANSWER:\nfuck a piece shit!\n' + '-'*144)



client.run(TOKEN)
