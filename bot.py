# bot.py
import os
import random 
import discord
import requests, uuid, json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')




client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messagefiltered = message.content.replace('!t', '')
    body = [{"text": messagefiltered}]

    subscription_key = os.getenv('KEY_VAR_NAME')
    endpoint = os.getenv('ENDPOINT_VAR_NAME')

    path = '/translate?api-version=3.0'
    params = '&to=en'
    constructed_url = endpoint + path + params

    headers2 = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4()),
    'Ocp-Apim-Subscription-Region': 'westeurope'
    }
   
    if "!t" in message.content:
        request = requests.post(constructed_url, headers=headers2, json=body)
        responseinitial = request.json()
        #response = json.dumps(responseinitial, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': '))
        #responseformed = json.loads(responseinitial)
        finalmsg = responseinitial[0]['translations'][0]['text']
        finalmsgfrom = responseinitial[0]['detectedLanguage']['language']
        await message.channel.send(finalmsg + "\n\nTranslated from '" + finalmsgfrom + "'" + "\nwith love by masterbrotranslator")

client.run(TOKEN)

