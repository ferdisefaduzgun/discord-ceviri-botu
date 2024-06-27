import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES
from textblob import TextBlob

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator()

language_names = {key: value.capitalize() for key, value in LANGUAGES.items()}

@bot.event
async def on_ready():
    print(f'Çeviri bot {bot.user} olarak sunucuya başarıyla giriş yaptı!!!!!!')

@bot.command()
async def cevir(ctx, *, text):
    try:
        # Yazım hatalarını düzeltilir.
        corrected_text = str(TextBlob(text).correct())
        
        # Çeviri işleminin yapıldığı kısım.
        translated = translator.translate(corrected_text, dest='tr')
        source_lang = language_names.get(translated.src, 'Bilinmeyen Dil')
        
        # Orijinal metin ve düzeltilmiş metin arasında fark olup olmadığı kontrol edilir.
        if text.lower() != corrected_text.lower():
            await ctx.send(f"Orijinal ({source_lang}): {text}\nDüzeltilmiş: {corrected_text}\nTürkçe: {translated.text}")
        else:
            await ctx.send(f"Orijinal ({source_lang}): {text}\nTürkçe: {translated.text}")
    except Exception as e:
        await ctx.send(f'Çeviri sırasında bir hata oluştu: {e}')


bot.run('TOKENİNİZİ_BURAYA_GİRİN')

