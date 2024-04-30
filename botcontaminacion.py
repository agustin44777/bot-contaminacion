import discord
import os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')
manualidades = [
    'Hacer porta macetas con papel',
    'hacer vasos con botellas de vidrio'
]
consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'otro consejo'
]

@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)
    
# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminación es la presencia de un constituyente, impureza o algún otro elemento indeseable que estropea, corrompe, infecta, inutiliza o degrada un material, cuerpo físico, entorno natural, lugar de trabajo, etc"
    await ctx.send(definicion)


todas_imagenes=os.listdir("conta")

@bot.command()
async def contami(ctx):
    img_name=random.choice(todas_imagenes)
    with open(f'conta/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)    

bot.run("codigo del bot")
