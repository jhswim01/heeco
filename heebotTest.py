import discord
import os
import asyncio



heebot = discord.Client()

print('start')

@heebot.event
async def on_message(message):
    print('희동이가 메세지를 받았습니다.')
    if message.content.startswith('희동'):
      await heebot.send_message(message.channel, '멍멍~')
      await heebot.send_message(message.channel, '멍멍~')

@heebot.event
async def on_ready():
  print('희동이 준비완료!')


access_token = os.environ["BOT_TOKEN"]
heebot.run(access_token)
