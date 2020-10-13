import discord
import random
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    powerword=open("./powerwordlist.txt").readlines()
    # 「**」で始まるか調べる
    if message.content.startswith("/pw"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            i = random.randrange(0,len(powerword))
            # メッセージを書きます
            m = powerword[i]
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

    if message.content.startswith("/pwa"):
        if client.user !=message.author:
            s = "\n" + message.content.replace("/pwa ","",1).replace("/pwa　","",1).replace("/pwa","",1)
            with open("./powerwordlist.txt","a") as plist:
                print(s,file=plist,end="")

client.run("NjU0NzE5MjgyOTA2NjYwOTE0.XfJo7w.iikMg8xasoEtitkX5gDwozuGvRs")
