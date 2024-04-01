import discord
# monitor user A's message AND specific keywords in everyone's message, will trigger BOT to send DM to user B
#-----------------------------------
# user A's ID（message sender）
TARGET_USER_ID_A = '904044085025857111'

# user B's ID（DM receiver）
TARGET_USER_ID_B = '1184978820546183111'

# BOT's Token
BOT_TOKEN = 'xxxx'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # ignore BOT self message
        if message.author == self.user:
            return

        # gain user B's handler
        user_b = await self.fetch_user(int(TARGET_USER_ID_B))

        # monitor user A and DM user B
        if message.author.id == int(TARGET_USER_ID_A):
            await user_b.send(f'{message.author.name} 在频道中发言了: {message.content}')

        # when monitor some keywords, DM user B 
        if "@chris" in message.content or "@chris_inc" in message.content:
            await user_b.send(f'USER {message.author.name} just at you: {message.content}')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

client = MyClient(intents=intents)
client.run(BOT_TOKEN)
