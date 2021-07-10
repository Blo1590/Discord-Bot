import discord
import json
import random
from discord.embeds import Embed
from discord.ext import commands
from discord import client
from discord import message
from discord.ext.commands.core import bot_has_permissions, has_permissions

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Waiting to serve"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        commandnotfoundembed = discord.Embed(title='**Command not Found!**',
                                             description=f'Try looking at the ".help" command for a list of all commands!',
                                             color=0x000000)
        await ctx.send(embed=commandnotfoundembed)

@client.event 
async def on_member_join(member):
    mybed = discord.Embed(title = "Welcome",description = f"Welcome to Lunar {member.mention}! ", color = 0x00ff00)
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.send(embed=mybed) 
    await member.add_roles(role)

@client.command()
async def info(ctx):
    infoEmbed = discord.Embed(title="Blo Bot Info:",
                              description="Information and descrtiption about Blo Bot, a bot developed by Blo#7727",
                              colour = 0x00ff00)
    infEmbed.add_field(name="Brief description of Blo Bot:",
                        value="The bot is a simply moderation, and fun bot.", inline=False)
    infEmbed.add_field(name="Library used:",
                        value="The bot was developed with discord.py",
                        inline=False)
    infEmbed.add_field(name="Help Command:",
                        value=".help",                   
                        inline=False)
    infEmbed.add_field(name="Bot owner:",
                        value="Blo#7727",
                        inline=False)
    infEmbed.set_footer(
        text="Bot created by Blo#7727")
    infEmbed.set_thumbnail(
        url = "https://cdn.shopify.com/s/files/1/1798/6083/products/the-grey-wind-fox-by-amy-lay-8013_1024x1024.jpg?v=1571609605")
    await ctx.send(embed=infoEmbed)

@client.command(aliases= ["sv-info"])
async def serverinfo(ctx):
    header = f'Server Information: {ctx.guild.name}'
    svembed = discord.Embed(title=header, description='Discord Server information by: Blo Bot', color= 0x00ff00)
    svembed.add_field(name='Name:', value=f'{ctx.guild.name}')
    svembed.add_field(name='ID:', value=f'{ctx.guild.id}')
    svembed.add_field(name='Region:', value=f'{ctx.guild.region}')
    svembed.add_field(name='Owner:', value=f'{ctx.guild.owner.display_name}')
    svembed.add_field(name='Shard ID:', value=f'{ctx.guild.shard_id}')
    svembed.add_field(name='Created on:', value=ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    svembed.add_field(name='Number of Members:', value=f'{len(ctx.guild.members)}')
    svembed.set_thumbnail(url=ctx.guild.icon_url)
    svembed.set_footer(text='Bot made by Blo#7727')
    await ctx.send(embed=embedman)

@client.command(aliases=["u-info"])
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]
 
    bruh = discord.Embed(colour=member.color, timestamp=ctx.message.created_at, )

    bruh.set_author(name=f"User Info - {member}")
    bruh.set_thumbnail(url=member.avatar_url)
    bruh.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    bruh.add_field(name="User ID:", value=member.id)
    bruh.add_field(name="Member name:", value=member.display_name)
    bruh.add_field(name='Boosted:', value= str(bool(member.premium_since)))

    bruh.add_field(name="Account Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    bruh.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    bruh.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    bruh.add_field(name="Top role:", value=member.top_role.mention)

    bruh.add_field(name="Is he a bot?", value=member.bot)

    await ctx.send(embed=bruh)

@client.command(aliases=["servermembers", "users"])
async def members(ctx):
    await ctx.send(f"The server has {len(ctx.guild.members)} members!")

@client.command(aliases=["inv"])
async def invite(ctx):
    inviteEmbed = discord.Embed(title="Blo Bot invite",
                                description="[Click here](https://discord.com/api/oauth2/authorize?client_id=847725829839388672&permissions=8&scope=bot) to invite the bot",
                                color=0x00ff00)
    inviteEmbed.set_thumbnail(
        url="https://pbs.twimg.com/profile_images/1242861639814139905/aiMugf_T_400x400.jpg")
    await ctx.send(embed=inviteEmbed)

@client.command(aliases=["h"])
async def help(ctx,*,sector="0"):
    if str(sector) == "1":
        Blohelp1 = discord.Embed(title="Help 1: **Commands**", color=0x00ff00)
       
        Blohelp1.add_field(name=".ping" ,
                             value=f' Returns the bots latency')
        Blohelp1.add_field(name=".member" ,
                             value=f' Shows the member count of the server')
        Blohelp1.add_field(name="serverinfo" ,
                             value=f' Shows the server info')
        Blohelp1.add_field(name=".invite" ,
                             value=f' Gets the invite link of the bot')
        Blohelp1.add_field(name=".userinfo",
                              value=f"Shows the user info")
        Blohelp1.set_thumbnail(url = "https://i.pinimg.com/564x/84/bf/14/84bf140018f412dad340cf4d91ce6c6d.jpg")
        
        Blohelp1.set_footer(text="Blo Bot created by Blo#7727")
        await ctx.send(embed=Blohelp1)
    if str(sector) == "2":
        Blohelp2 = discord.Embed(title="Help 2: **Moderation**", color=0x00ff00)

        Blohelp2.add_field(name=".ban" ,
                               value="Bans the member")
        Blohelp2.add_field(name=f".unban"  ,
                               value="Unbans the member")
        Blohelp2.add_field(name=".kick" ,
                               value="Kicks the member" )
        Blohelp2.add_field(name=".mute" ,
                               value="Mutes the member")
        Blohelp2.add_field(name=".unmute" ,
                               value="Unmutes the member")
        Blohelp2.add_field(name=f".clear [value]", 
        value="Clears the given amount of messages")
        Blohelp2.set_thumbnail(url = "https://i.pinimg.com/564x/84/bf/14/84bf140018f412dad340cf4d91ce6c6d.jpg")  
        Blohelp2.set_footer(text="Blo Bot created by Blo#7727")
        await ctx.send(embed=Blohelp2)
    if str(sector) == "3":
        Blohelp3 = discord.Embed(title="Help 3: **Fun Commands**", color=0x00ff00)

        Blohelp3.add_field(name=".howgay" , 
                           value="See if user is a faggot, or halal?")
        Blohelp3.add_field(name=".kill" ,
                           value="Kills that annoying bitch")
        Blohelp3.set_thumbnail(url = "https://i.pinimg.com/564x/84/bf/14/84bf140018f412dad340cf4d91ce6c6d.jpg")  
        Blohelp3.set_footer(text="Blo Bot created by Blo#7727")
        await ctx.send(embed=Blohelp3)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency *1000)}ms')

@client.command()
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
   await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f"Kicked {member.mention}: {reason}")
   
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}: {reason}")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name = "adios")
    await channel.send(f"Adios {member.mention}")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.name}")
            
@client.command()
@has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(member.guild.roles, name="Muted")
    await member.add_roles(mutedRole)
    await ctx.send(f"Muted {member.mention}: {reason}")
    await member.send(f"Stop {reason}")

@client.command()
@has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild
    mutedRole = discord.utils.get(member.guild.roles, name="Muted")
    if mutedRole == True:
        await member.remove_roles(mutedRole)
        await ctx.send(f"Unmuted {member.mention}")
    else:
        await ctx.send(f"{member} is not muted")
    
@client.command()
async def howgay(ctx, member : discord.Member):
    value = random.randint(0,101)

    if value >= 30:
        nuovoembed = discord.Embed(title=f'{member} is {value}% gay. What a faggot',
                                   description='Go fuck yourself',
                                   color=0x000000)
        nuovoembed.set_image(
            url='https://media.giphy.com/media/cyQXvx6OoSDTjukfLJ/giphy.gif')
        await ctx.send(embed=nuovoembed)
    else:
        altroembed = discord.Embed(title=f'{member} is {value}% gay, he is halal', description='Blo is glad!', color=0x000000)
        altroembed.set_image(url='https://media.giphy.com/media/T4jKbEoJ9jukHWwTVn/giphy.gif')
        await ctx.send(embed=altroembed)

@client.command()
async def kill(ctx, member : discord.Member):
    killembed1 = discord.Embed(title=f'{ctx.author} kills {member}',
                               color=0x000000)
    killembed1.set_image(url='https://media.giphy.com/media/24FH7zModR1i1Qfu8G/giphy.gif')
    killembed1.set_footer(text='*Bot created by Blo#7727*')
    killembed2 = discord.Embed(title=f'{ctx.author} kills {member}',
                               color=0x000000)
    killembed2.set_image(url='https://media.giphy.com/media/xUPGcdlIDdjwxbjrO0/giphy.gif')
    killembed2.set_footer(text='*Bot created by Blo#7727*')
    killembed3 = discord.Embed(title=f'{ctx.author} kills {member}',
                               color=0x000000)
    killembed3.set_image(url='https://media.giphy.com/media/3oz8xy1gPFHsB6NMDm/giphy.gif')
    killembed3.set_footer(text='*Bot created by Blo#7727*')
    killembed4 = discord.Embed(title=f'{ctx.author} kills {member}',
                               description=f'sus',
                               color=0x000000)
    killembed4.set_image(url='https://media.giphy.com/media/UcNaNsFk5jLSytk40R/giphy.gif')
    killembed4.set_footer(text='*Bot created by Blo#7727*')
    kill = [killembed1, killembed2, killembed3, killembed4]
    if member == ctx.author:
        ermbed = discord.Embed(description="Try killing someone else")
        await ctx.send(embed=ermbed)
    else:
        await ctx.send(embed=random.choice(kill))


client.run()
