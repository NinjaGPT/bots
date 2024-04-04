
import discord
import asyncio
import sys
from datetime import datetime, timedelta, timezone
from colorama import init, Fore
# BOT msg_collector

TOKEN = 'xxxx'
CHANNEL_ID = 1185274946981732111 # channel
outfile_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.txt'
#msg_count = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        channel = self.get_channel(CHANNEL_ID)

        if not channel:
            print("Channel not found.")
            return

        end_time = datetime.utcnow().replace(tzinfo=timezone.utc)
        start_time = end_time - timedelta(hours=24)
        limit_per_batch = 100

        with open(outfile_name, "w") as file:
            while True:
                messages = [message async for message in channel.history(limit=limit_per_batch, before=end_time)]
                if not messages:
                    break

                for message in messages:
                    if message.created_at < start_time:
                        print(Fore.RED + "#" * 100)
                        print("#"," " * 30, "Reached the start of the target period ")
                        print(Fore.RED + "#" * 100)
                        print("#"," " * 30, " PLEASE [ Ctrl + C ] to EXIT THIS BOT")
                        print("#" * 100)
                        return
                    formatted_date = message.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f'USER {message.author.name} SAID: {message.content}\n')
                    print(f'USER {message.author.name} SAID: {message.content}')
                    #file.write(f'{formatted_date}|{message.author.name}| {message.content}\n')
                    #print(f'{formatted_date}|{message.author.name}| {message.content}')
                    #msg_count += 1
                end_time = messages[-1].created_at
                await asyncio.sleep(1)

        #print(f"Total messages retrieved: {msg_count}")

        await self.close()

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(TOKEN)
