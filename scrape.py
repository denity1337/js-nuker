import discord
from discord.ext import commands
import time
import os

os.system(f"cls & mode 85,20")

token = input(f"Enter your bots token: ")
time.sleep(1)
print(f"Connected")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='bot', intents=intents)
os.system(f"cls & mode 85,20 & title [Claqz nuker] - Loading")


@bot.event
async def on_ready():
    os.system(f"cls & title [Claqz Nuker] - {bot.user}")
    print(f'[SUCCESFUL] - Logged in as {bot.user}.')
    guild = input("Enter Guild Id To Scrape: ")
    await bot.wait_until_ready()
    guildOBJ = bot.get_guild(int(guild))
    members = await guildOBJ.chunk()

    try:
            os.remove("members.txt")
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"Scraped {membercount} Members")
            m.close()

    time.sleep(2)
    print(f"Run the main file to start the nuker.")


bot.run(token)