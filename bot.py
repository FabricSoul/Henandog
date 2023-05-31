import discord
from discord.ext import commands
import asyncio
import datetime
import config
import time
import random
import json
import requests
import logging
import coloredlogs

intents = discord.Intents.all()
intents.message_content = True
intents.members = True  # enable member intents
intents.guilds = True
last_triggered_member = {}
last_triggered = {keyword: 0 for keyword in config.keywords}

logger = logging.getLogger('my_logger')
coloredlogs.install(level='INFO', logger=logger, fmt='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logger.setLevel(logging.INFO)

client = commands.Bot(command_prefix='$', intents=intents)

replying = False

@client.event
async def on_ready():
    logger.info(f'Logged in as {client.user.name} ({client.user.id})')

async def handle_message(message):
    chance = random.randint(0,100)
    if chance <= 5 and message.author.id in config.reply_member_id:
        if message.author.id not in last_triggered_member or time.time() - last_triggered_member[message.author.id] >= 300:
            logger.info(f"reply to {message.author}")
            await asyncio.sleep(random.randint(10, 20))
            image = discord.File(config.kill_sck)
            if (message.channel.id not in config.not_reply_in_channel):
                await message.reply(file=image) 
            last_triggered_member[message.author.id] = time.time()
    if any(keyword in message.content for keyword in config.keywords):
        for keyword, reply in config.keywords.items():
            chance = random.randint(0,100)
            now = time.time()
            if keyword in message.content and chance <= 30 and now - last_triggered[keyword] >= 300:
                logger.info(f"reply to {message.author}, trigger {keyword}")
                await asyncio.sleep(random.randint(10, 30))
                if reply.startswith('./images'):
                    image = discord.File(reply)
                    await message.reply(file=image)
                else:
                    await message.reply(reply)
                last_triggered[keyword] = now
                break  # break from the loop once a keyword has been responded to
            elif keyword in message.content and now - last_triggered[keyword] < 300:
                logger.info(f"not reply to {message.author}, trigger {keyword}, cooldown {now - last_triggered[keyword]}")


@client.event
async def on_message(message):
    global replying
    if config.reply_message and message.author != client.user and not replying:
        replying = True
        await handle_message(message)
        replying = False
    await client.process_commands(message)

@client.command()
async def timeout(ctx, user: discord.Member):
    '''Timeout a user for 5 minutes'''
    logger.info(f'Timeout command initiated for {user}')
    await vote_action(ctx, user, user.timeout, f'投票禁言{user.mention}', f"{user.mention}被禁言", f"禁言{user.mention}失败", datetime.timedelta(minutes=config.timeout_time), "Timeout vote passed")

@client.command()
async def kick(ctx, user: discord.Member):
    '''Kick a user from the server'''
    logger.info(f'Kick command initiated for {user}')
    await vote_action(ctx, user, user.kick, f'投票踢出{user.mention}', f"{user.mention}被踢出", f"踢出{user.mention}失败", None, "Kick vote passed")

async def vote_action(ctx, user, action, initiate_text, success_text, fail_text, timeout_duration, reason):
    timeout_votes = []
    vote_yes = []
    vote_no = []
    timeout_embed = discord.Embed(title='公众裁决⚖️', description=f'{initiate_text}\n点击 👍 同意, 👎 反对', color=0x00FFFF)
    timeout_msg = await ctx.send(embed=timeout_embed)
    embed = timeout_msg.embeds[0]
    await timeout_msg.add_reaction("👍")
    await timeout_msg.add_reaction("👎")
    def check(reaction, user):
        return str(reaction.emoji) in ["👍", "👎"]
    def result(text, timedout: bool):
        result_yes = '\n'.join([f"{user.mention} " for user in vote_yes])
        result_no = '\n'.join([f"{user.mention} " for user in vote_no])
        result_text = f"投票结果:\n{text}\n \n {len(vote_yes)}票同意: \n{result_yes} \n \n {len(vote_no)}票反对: \n{result_no}\n"
        if timedout:
            result_text += f"禁言将在 <t:{int(time.time()+(config.timeout_time*60))}:t> 结束"
        embed.description = result_text
    while len(timeout_votes) < config.vote_threshold:
        try:
            reaction, user_vote = await client.wait_for('reaction_add', timeout=config.wait_time, check=check)
        except asyncio.TimeoutError:
            result(fail_text, False)
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
        await action(timeout_duration, reason=reason) if timeout_duration else await action()
        result(success_text, True)
        await timeout_msg.edit(embed=embed)
    else:
        result(fail_text, False)
        await timeout_msg.edit(embed=embed)

@client.command()
async def search(ctx, *, question):
    '''Search on google'''
    if ctx.channel.id in config.ALLOWED_SEARCH_IN_CHANNELS:
        search_results = google_search(question)
        if search_results: 
            await ctx.send(f"**{search_results[0]['title']}**\n{search_results[0]['snippet']}\nRead more: {search_results[0]['link']}")
        else:
            await ctx.send("抱歉，没有找到相关结果")
    else:
        await ctx.send("这个频道不允许使用搜索功能\n请在 https://discord.com/channels/1091392183510241300/1112603636581797919 使用搜索功能")

def google_search(query):
    search_url = f"https://www.googleapis.com/customsearch/v1?key={config.GOOGLE_API_KEY}&cx={config.GOOGLE_CX_ID}&q={query}"
    response = requests.get(search_url)
    response.raise_for_status()
    search_results = json.loads(response.text)
    return search_results.get('items', [])

client.run(config.TOKEN)
