import discord
from discord.ext import commands
import asyncio
import datetime
import config
import time
import random

intents = discord.Intents.all()
intents.message_content = True
intents.members = True  # enable member intents
intents.guilds = True

# set bot command prefix
client = commands.Bot(command_prefix='$', intents=intents)

@client.command()
async def timeout(ctx, user: discord.Member):

    # initiate a timeout vote
    # create empty lists to store votes
    timeout_votes = []
    vote_yes = []
    vote_no = []

    # send message to initiate vote
    timeout_embed = discord.Embed(
        title='公众裁决⚖️', description=f'投票禁言{user.mention}\n点击 👍 同意, 👎 反对', color=0x00FFFF)

    timeout_msg = await ctx.send(embed=timeout_embed)
    embed = timeout_msg.embeds[0]

    await timeout_msg.add_reaction("👍")
    await timeout_msg.add_reaction("👎")

    # define a check function to validate reactions
    def check(reaction, user):
        return str(reaction.emoji) in ["👍", "👎"]

    def result(text, timedout: bool):
        result_yes = '\n'.join([f"{user.mention} " for user in vote_yes])
        result_no = '\n'.join([f"{user.mention} " for user in vote_no])
        result_text = f"投票结果:\n{text}\n \n {len(vote_yes)}票同意: \n{result_yes} \n \n {len(vote_no)}票反对: \n{result_no}\n"
        if timedout:
            result_text += f"禁言将在 <t:{int(time.time()+(config.timeout_time*60))}:t> 结束"
        embed.description = result_text

    # wait for reactions from members
    while len(timeout_votes) < config.vote_threshold:
        try:
            reaction, user_vote = await client.wait_for('reaction_add', timeout=config.wait_time, check=check)
        except asyncio.TimeoutError:
            result(f"没有足够的票数禁言{user.mention}", False)
            await timeout_msg.edit(embed=embed)
            return

        if str(reaction.emoji) == "👍":
            if user_vote in timeout_votes:
                await ctx.send(content=f"{user_vote.mention}你已经投过票了", ephemeral=True)
                continue
            else:
                timeout_votes.append(user_vote)
                vote_yes.append(user_vote)
        elif str(reaction.emoji) == "👎":
            if user_vote in timeout_votes:
                await ctx.send(content=f"{user_vote.mention}你已经投过票了", ephemeral=True)
                continue
            else:
                timeout_votes.append(user_vote)
                vote_no.append(user_vote)

    if len(vote_yes) > len(vote_no):
        # timeout member
        await user.timeout(datetime.timedelta(minutes=config.timeout_time), reason="Timeout vote passed")
        result(f"{user.mention}被禁言", True)
        await timeout_msg.edit(embed=embed)
    else:
        result(f"禁言{user.mention}失败", False)
        await timeout_msg.edit(embed=embed)

    return

@client.command()
async def kick(ctx, user: discord.Member):

    # initiate a timeout vote
    # create empty lists to store votes
    timeout_votes = []
    vote_yes = []
    vote_no = []

    # send message to initiate vote
    timeout_embed = discord.Embed(
        title='公众裁决⚖️', description=f'投票踢出{user.mention}\n点击 👍 同意, 👎 反对', color=0x00FFFF)

    timeout_msg = await ctx.send(embed=timeout_embed)
    embed = timeout_msg.embeds[0]

    await timeout_msg.add_reaction("👍")
    await timeout_msg.add_reaction("👎")

    # define a check function to validate reactions
    def check(reaction, user):
        return str(reaction.emoji) in ["👍", "👎"]

    def result(text, timedout: bool):
        result_yes = '\n'.join([f"{user.mention} " for user in vote_yes])
        result_no = '\n'.join([f"{user.mention} " for user in vote_no])
        result_text = f"投票结果:\n{text}\n \n {len(vote_yes)}票同意: \n{result_yes} \n \n {len(vote_no)}票反对: \n{result_no}\n"
        if timedout:
            pass
            # result_text += f"禁言将在 <t:{int(time.time()+(config.timeout_time*60))}:t> 结束"
        embed.description = result_text

    # wait for reactions from members
    while len(timeout_votes) < config.vote_threshold:
        try:
            reaction, user_vote = await client.wait_for('reaction_add', timeout=config.wait_time, check=check)
        except asyncio.TimeoutError:
            result(f"没有足够的票数踢出{user.mention}", False)
            await timeout_msg.edit(embed=embed)
            return

        if str(reaction.emoji) == "👍":
            if user_vote in timeout_votes:
                await ctx.send(content=f"{user_vote.mention}你已经投过票了", ephemeral=True)
                continue
            else:
                timeout_votes.append(user_vote)
                vote_yes.append(user_vote)
        elif str(reaction.emoji) == "👎":
            if user_vote in timeout_votes:
                await ctx.send(content=f"{user_vote.mention}你已经投过票了", ephemeral=True)
                continue
            else:
                timeout_votes.append(user_vote)
                vote_no.append(user_vote)

    if len(vote_yes) > len(vote_no):
        # timeout member
        await user.kick()
        result(f"{user.mention}被踢出", True)
        await timeout_msg.edit(embed=embed)
    else:
        result(f"踢出{user.mention}失败", False)
        await timeout_msg.edit(embed=embed)

    return


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    
@client.event
async def on_message(message):
    if config.reply_message and message.author != client.user:
        chance = random.randint(0,100)
        if chance <= 10:
            if message.author.id in config.reply_member_id:
                image = discord.File(config.kill_sck)
                print(f"reply to {message.author}")
                await message.reply(file=image)
        
        if chance <= 90:
            if any(keyword in message.content for keyword in config.keywords):
                for keyword, reply in config.keywords.items():
                    if keyword in message.content:
                        if reply.startswith('./images'):
                            image = discord.File(reply)
                            await message.reply(file=image)
                        else:
                            await message.reply(reply)
    await client.process_commands(message)

client.run(
    config.TOKEN)
