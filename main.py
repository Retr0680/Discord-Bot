#     ____       __       ____ 
#    / __ \___  / /______/ __ \
#   / /_/ / _ \/ __/ ___/ / / /
#  / _, _/  __/ /_/ /  / /_/ / 
# /_/ |_|\___/\__/_/   \____/  

# Libraries
import discord
import os
from discord.ext import commands
#import youtube_dl
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = discord.Client()
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print("     ____       __       ____  ")
    print("    / __ \___  / /______/ __ \ ")
    print("   / /_/ / _ \/ __/ ___/ / / / ")
    print("  / _, _/  __/ /_/ /  / /_/ /  ")
    print(" /_/ |_|\___/\__/_/   \____/   ")

    print('Bot is online!'.format(client))
    #print("{0.user} is online!".format(client))

    # Discord Presence
    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))

@client.command()
async def userinfo(ctx: commands.Context, user: discord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `discord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `discord.User` instance.
    # The documentation notes what can be converted, in the case of `discord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 793387363513401346, @Retr0_680 or Retr0_680#1598

    # NOTE: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `discord.User` instance
    # and can do the following:
    user_id = user.id
    username = user.name
    avatar = user.avatar_url
    await ctx.send('User found: {} -- {}\n{}'.format(user_id, username, avatar))

@userinfo.error
async def userinfo_error(ctx: commands.Context, error: commands.CommandError):
    # if the conversion above fails for any reason, it will raise `commands.BadArgument`
    # so we handle this in this error handler:
    if isinstance(error, commands.BadArgument):
        return await ctx.send('Couldn\'t find that user.')

# Dm the any user!
# Custom Converter here
class ChannelOrMemberConverter(commands.Converter):
    async def convert(self, ctx: commands.Context, argument: str):
        # In this example we have made a custom converter.
        # This checks if an input is convertible to a
        # `discord.Member` or `discord.TextChannel` instance from the
        # input the user has given us using the pre-existing converters
        # that the library provides.

        member_converter = commands.MemberConverter()
        try:
            # Try and convert to a Member instance.
            # If this fails, then an exception is raised.
            # Otherwise, we just return the converted member value.
            member = await member_converter.convert(ctx, argument)
        except commands.MemberNotFound:
            pass
        else:
            return member

        # Do the same for TextChannel...
        textchannel_converter = commands.TextChannelConverter()
        try:
            channel = await textchannel_converter.convert(ctx, argument)
        except commands.ChannelNotFound:
            pass
        else:
            return channel

        # If the value could not be converted we can raise an error
        # so our error handlers can deal with it in one place.
        # The error has to be CommandError derived, so BadArgument works fine here.
        raise commands.BadArgument('No Member or TextChannel could be converted from "{}"'.format(argument))

@client.command()
async def notify(ctx: commands.Context, target: ChannelOrMemberConverter,):
    # This command signature utilises the custom converter written above
    # What will happen during command invocation is that the `target` above will be passed to
    # the `argument` parameter of the `ChannelOrMemberConverter.convert` method and 
    # the conversion will go through the process defined there.
    await ctx.send(f' Message has been sent!')
    await target.send('Hello, {}!'.format(target.name))

# MOD-MAIL
@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)

# Greeting to new members
@client.event
async def on_member_join(member):
    guild = client.get_guild(869599646387957780)# server id required here
    channel = guild.get_channel(869600907288018954)# channel id of the server here
    await channel.send(f'{member.mention}, Welcome to {guild.name}!')# message sent in the server
    await member.send(f'{member.mention}, Welcome to {guild.name}!')# Dm to the user

@client.event
async def help(ctx, member):
    await ctx.send(f'{member.mention}, i have sent you a DM!')
    await member.send(f'{member.mention},Write whatever you want to say for help')

keep_alive()
#Token = your bot token
client.run('ODg1OTM5MDE2OTEzMDIzMDY2.YTuVAQ.v7nMgkomVzr-LIXAiEE59J930sA')