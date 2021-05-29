import discord
import requests
import json
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "quack ")
#def video_search(name):
#request = requests.get("https://youtube.googleapis.com/youtube/v3/search?part=snippet&q=come%20and%20go&key=[AIzaSyA6pkgWekHOwimIOKIhKgdvRNVbpOJb91k]HTTP/1.1
#", params = name)

#query = {'part': 'snippet', 'q': name}

@client.event
async def on_member_join(member):
  ground = client.get_channel(847075713999175690)
  await ground.send("{0} has brought some pizza".format(member))

@client.event
async def on_member_remove(member):
  ground = client.get_channel(847075713999175690)
  await ground.send("{0} has left our party".format(member))#
  

@client.event
async def on_ready():
    print("Quack Quack guys, I am online!")
    ground = client.get_channel(847075713999175690)
    await ground.send("Quack Quack guys, I am online")

@client.command(aliases = ["whats up", "whats up!", "whats up?"])
async def whatsup(ctx):
  await ctx.send("I am Quacked up!, what about you? want some sucky sucky? :)")


@client.command()
async def quote(ctx):
  r = requests.get("https://animechan.vercel.app/api/quotes/anime?title=naruto")
  number = random.randint(0, 10)
  await ctx.send(r.json()[number]["quote"])
  await ctx.send('- ' + r.json()[number]["character"])

@client.command(name = "suck")
async def suck_me(ctx):
  await ctx.send(f'Sucking {ctx.author.name}\'s dick!')

@client.command()
async def sing(ctx):
  await ctx.send("Quack Quack, Quack Quack!")

@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
  responses = ["It is Certain!",
               "It is decidedly so",
               "Without a doubt",
               "Yes, Definitely",
               "You may rely on it",
               "As I see it, yes",
               "Most likely",
               "Outlook good",
               "Yes",
               "Signs point to yes",
               "Reply hazy, try again",
               "Ask again later",
               "better not tell you now",
               "cannot predict now",
               "concentrate and ask again",
               "don't count on it",
               "my reply is no",
               "my sources say no",
               "outlook not so good",
               "very doubtful"
                ]
  await ctx.send(f'{str(ctx.author).split("#")[0]}: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def clear(ctx, number):
  await ctx.channel.purge(limit=(int(number) + 1))

@client.command()
async def kick(ctx, member : discord.member ,* , reason = None):
  await member.kick(reason = reason)
  await ctx.send(f'{ctx.author} kicked {member} away!')

@client.command()
async def ban(ctx, member : discord.member, *, reason = None):
  await member.ban(reason = reason)
  await ctx.send(f'Woah!, {ctx.author} banned {member}')

@client.command()
async def unban(ctx, * , member):
  banned_list = await ctx.guild.bans()
  member_name, member_discriminant = member.split("#")

  for banned in banned_list:
    user = banned.user

    if (user.name, user.discriminant) == (member_name, member_discriminant):
      await ctx.guild.unban(user)
      await ctx.send(f'{user.mention} is unbanned')



client.run(<Token of your bot>)
