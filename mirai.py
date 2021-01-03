import discord
import jt
import botconfig

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(botconfig.jtprefix):
        args = message.content.split(" ")[1:]
        for i, arg in enumerate(args):
            args[i] = int(arg)

        if not args or args[0] == "help":
            await message.channel.send(jt.doc)
        else:
            mat = jt.fmt2d(jt.melt(args))
            lines = ["```"]
            for row in mat:
                lines.append(" ".join(row))
            lines.append("```")
            await message.channel.send("\n".join(lines))
                

client.run(botconfig.token)
