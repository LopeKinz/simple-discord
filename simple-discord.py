import discord
import json
import os
import colorama

def init():
  async def on_ready(self):
        print('Logged on as', self.user)
      
def start(token):
  intents = discord.Intents.default()
  intents.message_content = True
  client = MyClient(intents=intents)
  client.run(token)
  
#not done yet since its alot to do
