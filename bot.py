#from webserver import keep_alive
#^ its a free hosting from replit :)
import os
import discord
from discord.ext import commands, tasks
import urllib.parse, urllib.request, re
import praw
import random
import time
from itertools import cycle
from praw.reddit import Submission
#if you have any questions add me on discord BigYoshi#4496 also dont message me to say that my code is shit.I know it is

# you can find more info about praw here https://pypi.org/project/praw/

reddit = praw.Reddit(client_id = "",
                     client_secret = "",
                     username = "",
                     password = "",
                     user_agent = "")

client = commands.Bot(command_prefix = '&')



@client.event
async def on_ready():
    print('Servers connected to: ')
    for guild in client.guilds:
        print(guild.name,guild.id,guild.owner_id)

#you can make this reddit code 300 times faster but im too fucking lazy to do that
@client.command()
async def r(ctx,*,subred = ""):
    subreddit = reddit.subreddit(subred)
    all_subs = []
    top = subreddit.top(limit = 150)
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    #this is kinda like a whitelist on who can post nsfw stuff with reddit
    if ctx.author.id == 696226723947085904:
        em = discord.Embed(title = name)
        em.set_image(url = url)
        await ctx.send(embed = em) 
    elif not submission.over_18:
        em = discord.Embed(title = name)
        em.set_image(url = url)
        await ctx.send(embed = em)
    else:
        await ctx.send("U hab little penis")
        print("Not whitelisted")


@client.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong", description=f"{round(client.latency *1000)}",color=0x00ff00)
    await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
    await ctx.send (embed=discord.Embed(titel="Rules", description="Follow tos",color=0x00ff00))


@client.command()
async def commands(ctx):
    await ctx.send (embed=discord.Embed(titel="Commands",description="The current commands are &ping, &rules, &kick, &addrole,&remrole, &ban, &r for reddit",color=0x00ff00))
    
@client.command()
async def command(ctx):
    await ctx.send (embed=discord.Embed(titel="Commands",description="The current commands are &ping, &rules, &kick, &addrole,&remrole, &ban, &r for reddit",color=0x00ff00))



@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.kick(reason=reason)

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        await member.ban(reason=reason)

@client.command()
async def addrole(ctx, role: discord.Role, member: discord.Member):
    if ctx.author.guild_permissions.administrator:
      await member.add_roles(role)
      await ctx.send(f"ok dad")

@client.command()
async def remrole(ctx, role: discord.Role, member: discord.Member):
    if ctx.author.guild_permissions.administrator:
      await member.remove_roles(role)

@client.command()
async def yes(ctx):
    await ctx.send (embed=discord.Embed(title="Yes",color=0x00ff00))

#keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)

#if you have any questions add me on discord BigYoshi#4496 also dont message me to say that my code is shit.I know it is