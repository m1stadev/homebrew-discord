#!/usr/bin/env python3

from discord.ext import commands
import discord
import requests
import sys

client = commands.Bot(command_prefix='hb!', help_command=None)
client_id = 'CLIENT_ID'

def bot_token(token):
    try:
        token_file = open(token, "r+")
        return token_file.read()
    except FileNotFoundError:
        sys.exit("No bot token found in token.txt. Make sure you've created the file and put your token into it, or else this bot will not work.")

def list_to_str(lst):
    list_str = ''
    for x in lst:
        list_str += f'{x}, '

    return list_str[:-2]

@client.event
async def on_ready():
    print('Bot is now online.')
    await client.change_presence(activity=discord.Game(name=f'Prefix: {client.command_prefix} | In {len(client.guilds)} servers'))

@client.event
async def on_guild_join(guild):
    await client.change_presence(activity=discord.Game(name=f'Prefix: {client.command_prefix} | In {len(client.guilds)} servers'))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Game(name=f'Prefix: {client.command_prefix} | In {len(client.guilds)} servers'))

@client.command()
@commands.guild_only()
async def search(ctx, package):
    api_info = requests.get('https://formulae.brew.sh/api/formula.json')
    data = api_info.json()
    for i in range(0, len(data)):
        if data[i]['name'] == package.lower() or data[i]['full_name'] == package.lower():
            package_location = i
            break

        elif package.lower() in data[i]['aliases']:
            package_location = i
            break

        package_location = False

    if not package_location:
        embed = discord.Embed(color=0xf7b64f, title='**Error 404:** Package Not Found')
        embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)
        return

    if len(list_to_str(data[package_location]["dependencies"])) == 0:
        dependencies = 'None'
    else:
        dependencies = list_to_str(data[package_location]["dependencies"])

    embed = discord.Embed(color=0xf7b64f, title='\U0001F37A Homebrew Search', description=f'```Name: {data[package_location]["name"]}\nDescription: {data[package_location]["desc"]}\nVersion: {data[package_location]["versions"]["stable"]}\nHomepage: {data[package_location]["homepage"]}\nDependencies: {dependencies}```')
    embed.set_footer(text=f'{ctx.message.author.name}', icon_url=ctx.message.author.avatar_url_as(static_format='png'))
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def invite(ctx):
    embed = discord.Embed(color=0xf7b64f, title='Invite', description=f'Invite me to your server using [this](https://discord.com/oauth2/authorize?client_id={client_id}&scope=bot&permissions=3072) link!')
    embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url_as(static_format='png'))
    await ctx.send(embed=embed)

@client.command()
@commands.guild_only()
async def help(ctx):
    embed = discord.Embed(color=0xf7b64f, title='Commands')
    embed.add_field(name=f'`{client.command_prefix}help`', value='Show this message.', inline=True)
    embed.add_field(name=f'`{client.command_prefix}invite`', value='Get the invite link for this bot.', inline=True)
    embed.add_field(name=f'`{client.command_prefix}search <package>`', value='Search for a package.', inline=True)
    embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url_as(static_format='png'))
    await ctx.send(embed=embed)

try:
    client.run(bot_token('token.txt'))
except discord.LoginFailure:
    sys.exit('Token invalid, make sure your token is the only thing in token.txt')