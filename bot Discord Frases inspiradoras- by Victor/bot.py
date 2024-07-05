import discord
import json
import random

with open("json.json", encoding='utf-8') as json_data:
   dados = json.load(json_data)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logou como {self.user.name}!')

    async def on_message(self, message):
        print(f'Mensagem de {message.author}: {message.content}')
        if message.content == '$eae':
            await message.channel.send(f'Eae {message.author.name}, beleza?')
        elif message.content == '$perguntarquanto':
            await message.channel.send('quanto?')
        elif message.content == '$frase':
            frase_aleatoria = random.choice(dados)
            autor = frase_aleatoria['autor']
            frase = frase_aleatoria['frase']
            await message.channel.send(f'{frase} - {autor}')



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('SUA KEY') ##Não esqueça de alterar sua chave aqui.



