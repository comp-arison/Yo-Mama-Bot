'''
Yo Mama Bot ©2021 Nathan Boehm
Special thanks to yo mama lmao
'''
import discord
import os
import asyncio
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
  print("{0.user} so fat.".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers."))

@client.event
async def on_message(message):
  prevmessages = await message.channel.history(limit=5).flatten()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers."))
  if message.author == client.user:
    return
  #Yandere Dev be like:
  if message.content.lower().startswith("i think "):
    await message.channel.send("Yo mama thinks " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i wonder "):
    await message.channel.send("Yo mama wonders " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i do "):
    await message.channel.send("Yo mama does " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i am "):
    await message.channel.send("Yo mama is " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i'm ") or message.content.lower().startswith("im "):
    await message.channel.send("Yo mama's " + " ".join(message.content.split()[1:]))
  elif message.content.lower().startswith("i don't ") or message.content.lower().startswith("i dont "):
    await message.channel.send("Yo mama doesn't " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i do "):
    await message.channel.send("Yo mama does " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i really love "):
    await message.channel.send("Yo mama really loves " + " ".join(message.content.split()[3:]))
  elif message.content.lower().startswith("i really hate "):
    await message.channel.send("Yo mama really hates " + " ".join(message.content.split()[3:]))
  elif message.content.lower().startswith("i love "):
    await message.channel.send("Yo mama loves " + " ".join(message.content.split()[3:]))
  elif message.content.lower().startswith("i hate "):
    await message.channel.send("Yo mama hates " + " ".join(message.content.split()[3:]))
  elif message.content.lower() == ("i-"):
    await message.channel.send("Yo mama-")
  elif message.content.lower().startswith("my mama "):
    await message.channel.send("Indeed.")
  elif message.content.lower() == "yo mama so stupid she left the voice chat." or message.content.lower() == "yo mama so stupid she left the voice chat" or message.content.lower() == "yo mama so stupid she left the voice chat!":
    voice_state = message.author.voice
    if voice_state != None:
      for x in client.voice_clients:
        if x.guild == message.guild:
          return await x.disconnect()
    await message.channel.send("Hell yeah.")
  elif message.content.lower().startswith("yo mama "):
    await message.channel.send("Hell yeah.")
  elif message.content.lower() == "yo mama" or message.content.lower() == "yo mama.":
    await message.channel.send(file=discord.File('Yo Mama.mp3'))
    try:
      voice = await message.author.voice.channel.connect()
      voice.play(discord.FFmpegPCMAudio('Yo Mama.mp3'))
      await message.channel.send("If you want me to stop just say:\nYo mama so stupid she left the voice chat.")
      while voice.is_playing():
        await asyncio.sleep(.1)
      await voice.disconnect()
    except:
      pass
  #if the user gets mad at the bot after it says a message, get back at them. I have no idea if this actually works.
  elif prevmessages[1].author == client.user and message.content.lower().startswith("fuck off") or message.content.lower().startswith("fuck you") or message.content.lower().startswith("i hate you") or message.content.lower().startswith("you suck") or message.content.lower().startswith("shut up") or message.content.lower().startswith("this bot sucks") or message.content.lower().startswith("this bot was a mistake"):
    await message.channel.send("Fuck you.")
  elif message.content.lower().startswith("i want "):
    await message.channel.send("Yo mama wants " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("my "):
    await message.channel.send("Yo mama's " + " ".join(message.content.split()[1:]))
  elif message.content.lower() == "i fucked your mom":
    await message.channel.send("Yo mama fucked your mom\n\nwait what")
  elif message.content.lower() == "i fucked ur mom":
    await message.channel.send("Yo mama fucked ur mom\n\nwait what")
  elif message.content.lower() == "i fucked your mom.":
    await message.channel.send("Yo mama fucked your mom\n\nwait what")
  elif message.content.lower() == "i fucked ur mom.":
    await message.channel.send("Yo mama fucked ur mom\n\nwait what")
  elif message.content.lower().startswith("i made "):
    await message.channel.send("Yo mama made " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i need "):
    await message.channel.send("Yo mama needs " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i wear "):
    await message.channel.send("Yo mama wears " + " ".join(message.content.split()[2:]))
  elif message.content.lower() == "fat":
    await message.channel.send(file=discord.File('fat.png'))

keep_alive()
client.run(os.getenv("TOKEN"))