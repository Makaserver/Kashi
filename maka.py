import discord
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("마카서버관전")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "[ 유저 ]":
            role = i
            break
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("테스트")
    if message.content.startswith("또뚜"):
        await message.channel.send("DDoDDu#1126")
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)








client.run("NTM4OTkwNzc5MzMxMjQ4MTQ5.XXMLOQ.pyqi18zvQ4ZwU_1Tg2qYJcKufBs")
