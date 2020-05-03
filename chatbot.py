import discord

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

'''
This is an example showing how to create an export file from
an existing chat bot that can then be used to train other bots.
'''

chatbot = ChatBot('Export Example Bot')

# First, lets train our bot with some data
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

client = discord.Client()

# print in console of bot name
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # if tagged the bot
    id = client.user.id

    if str(id) in message.content:

        # get the question
        resp = str(message.content).split("<@!706304504915820585> ")[1]

        bot_input = chatbot.get_response(resp)

        await message.channel.send(f'{bot_input}')

client.run("")
