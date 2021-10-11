'''
Yo Mama Bot ©2021 Nathan Boehm
Special thanks to yo mama lmao
'''
import discord
import os
import asyncio
import random as rand
from keep_alive import keep_alive
client = discord.Client()

jokes = ["Yo mama so stupid, she thought Nickelback was a refund.", "Yo mama so fat, that when she dies in call of duty the player gets a 5 person kill streak.", "Yo mama so ugly, that one direction went the other direction.", "Yo mama so hairy, that when she gave birth to you, you got carpet burned.", "Yo mama so stupid, that she thought seaweed is something that fish smoke.", "Yo mama so short, that she hang glides on a dorito.", "Yo mama so fat, that when dracula sucked her blood she got diabetes.", "Yo mama so ugly, that Bob the builder said I can't fix that.", "Yo mama so stupid, that she bought tickets to Xbox Live.", "Yo mama so old, that her first christmas was the first christmas.", "Yo mama so ugly, that when she looked down at the window she got arrested for mooning.", "Yo mama so stupid, that when she put two quarters in her ears she thought she was listening to fifty cent.", "Yo mama so old, that when she farts dust comes out.", "Yo mama so fat, that she got arrested for carrying 15 pounds of crack.", "Yo mama so stupid, that she made an appointment with dr. Pepper.", "Yo mama so ugly, that her pillow cries at night.", "Yo mama so fat, that she had to be baptised at sea world.", "Yo mama so stupid, that she thought fruit punch was a gay boxer.", "Yo mama so hairy, that big foot took her pictures.", "Yo mama so ugly, that when she went to a haunted house she got a job application.", "Yo mama so stupid, that she tried to climb Mountain Dew.", "Yo mama so ugly, that she made an onion cry.", "Yo mama so fat, that when she died she broke the stairway to heaven.", "Yo mama so short, that you can see her legs on her driver's license photo.", "Yo mama so poor, that she eats cerial with a fork to save milk.", "Yo mama so ugly, she turned medusa into stone.", "Yo mama so skinny, that when I shook her hand she gave me a paper cut.", "Yo mama so fat, that big chungus chungused on her"]

@client.event
async def on_ready():
  print("{0.user} so fat.".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers."))

@client.event
async def on_message(message):
  #prevmessages = await message.channel.history(limit=5).flatten()
  messagenopunc = ""
  for char in message.content:
    if char not in '''.,;!?'"''':
      messagenopunc = messagenopunc + char
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds)) + " servers."))
  if message.author == client.user:
    return
  #Yandere Dev be like:
  if message.content.lower().startswith("i think "):
    await message.channel.send("Yo mama thinks " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i wonder "):
    await message.channel.send("Yo mama wonders " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i have "):
    await message.channel.send("Yo mama has " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i need "):
    await message.channel.send("Yo mama needs " + " ".join(message.content.split()[2:]))
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
  elif messagenopunc.lower() == "i love yo mama" or messagenopunc.lower() == "i love yo mama bot" or messagenopunc.lower() == "thanks yo mama bot" or messagenopunc.lower() == "yo mama loves you":
    await message.channel.send(file=discord.File('Yo Mama.gif'))
  elif message.content.lower().startswith("i really love "):
    await message.channel.send("Yo mama really loves " + " ".join(message.content.split()[3:]))
  elif message.content.lower().startswith("i really hate "):
    await message.channel.send("Yo mama really hates " + " ".join(message.content.split()[3:]))
  elif message.content.lower().startswith("i love "):
    await message.channel.send("Yo mama loves " + " ".join(message.content.split()[2:]))
  elif message.content.lower().startswith("i hate "):
    await message.channel.send("Yo mama hates " + " ".join(message.content.split()[2:]))
  elif message.content.lower() == ("i-"):
    await message.channel.send("Yo mama-")
  elif messagenopunc.lower() == "sus" or messagenopunc.lower() == "sussy" or messagenopunc.lower() == "yo mama so sus" or messagenopunc.lower() == "yo mama sus" or messagenopunc.lower() == "yo mama sussy" or messagenopunc.lower() == "yo mama so sussy":
    await message.channel.send(file=discord.File('Sus.mp4'))
  elif messagenopunc.lower() == "yo mama so fat that she grates cheese" or messagenopunc.lower() == "yo mama so fat that she grates cheeze":
    await message.channel.send("What's that you say? My mama is so fat that she grates cheese? How dare you sir!")
  elif message.content.lower().startswith("my mama "):
    await message.channel.send("Indeed.")
  elif message.content.lower() == "yo mama dead" or message.content.lower() == "yo mama dead." or message.content.lower() == "yo mama so dead" or message.content.lower() == "yo mama so dead." or message.content.lower() == "thats why yo mama dead" or message.content.lower() == "thats why yo mama dead." or message.content.lower() == "that's why yo mama dead" or message.content.lower() == "that's why yo mama dead.":
    await message.channel.send("Dead as hell.")
    return
  elif message.content.lower() == "yo mama so stupid she left the voice chat." or message.content.lower() == "yo mama so stupid she left the voice chat" or message.content.lower() == "yo mama so stupid she left the voice chat!":
    voice_state = message.author.voice
    if voice_state != None:
      for x in client.voice_clients:
        if x.guild == message.guild:
          return await x.disconnect()
    if rand.randint(1,10) == 1:
      await message.channel.send(file=discord.File('Yo Mama Moment.mp4'))
    else:
      await message.channel.send("Hell yeah.")
  elif message.content.lower().startswith("yo mama so "):
    if rand.randint(1,10) == 1:
      await message.channel.send(file=discord.File('Yo Mama Moment.mp4'))
    else:
      await message.channel.send("Hell yeah.")
  elif message.content.lower() == "hell yeah" or message.content.lower() == "hell yeah.":
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
  #elif prevmessages[1].author == client.user and (message.content.lower().startswith("fuck off") or message.content.lower().startswith("fuck you") or message.content.lower().startswith("i hate you") or message.content.lower().startswith("you suck") or message.content.lower().startswith("shut up") or message.content.lower().startswith("this bot sucks") or message.content.lower().startswith("this bot was a mistake")):
    #await message.channel.send("Fuck you.")
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
    await message.channel.send(file=discord.File('Fat.png'))
  elif message.content.lower() == "sans":
    await message.channel.send(file=discord.File('Sans.mov'))
  elif client.user in message.mentions:
    await message.channel.send(jokes[rand.randint(0, len(jokes) - 1)])
  elif message.content.lower() == "no mama" or message.content.lower() == "no mama.":
    await message.channel.send(file=discord.File('No Mama.mp4'))
  elif "your biological mother is so morbidly obese when she went to go get her yearly physical done the doctor took her blood and the results concluded that she had a high blood pressure onset type 2 diabetes hypertension and the possibility of heart disease she also suffers from severe depression because she lacks confidence in her physical appearance which enables her to consume even more food making her more obese not to mention but your mother is becoming so monstrous she had a hard time fitting through small spaces and exceeding weight limits on practical applications your mother has an endless cycle of malicious eating habits that only make her health worsen over time" in messagenopunc.lower() or "your biological mother is so morbidly obese when she went to get her yearly physical done the doctor took her blood and the results concluded that she had a high blood pressure onset type 2 diabetes hypertension and the possibility of heart disease she also suffers from severe depression because she lacks confidence in her physical appearance which enables her to consume even more food making her more obese not to mention but your mother is becoming so monstrous she had a hard time fitting through small spaces and exceeding weight limits on practical applications your mother has an endless cycle of malicious eating habits that only make her health worsen over time" in messagenopunc.lower():
    await message.channel.send("By the devil, that is correct.")
  elif message.content.lower() == "i forgor":
    await message.channel.send("Yo mama forgor")
  elif message.content.lower() == "i forgor.":
    await message.channel.send("Yo mama forgor.")
  elif message.content.lower() == "i suck":
    await message.channel.send("Yo mama sucks")
  elif message.content.lower() == "i suck.":
    await message.channel.send("Yo mama sucks.")
  elif messagenopunc.lower() == "dead chat" or messagenopunc.lower() == "dead chat xd" or messagenopunc.lower() == "ded chat" or messagenopunc.lower() == "ded chat xd":
    await message.channel.send("Yo mama's a dead chat.")
  elif messagenopunc.lower() == "unused server" or messagenopunc.lower() == "unused server xd":
    await message.channel.send('''You think you're slick? You think you can avoid me? Think again fucker. I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.''')
  elif message.guild.id == 888219323682930729 and ("kel" in messagenopunc.lower() or "omori" in messagenopunc.lower() or "alcohol" in messagenopunc.lower()): #this is only used for a specific server i'm in
    await message.delete()

keep_alive()
client.run(os.getenv("TOKEN"))