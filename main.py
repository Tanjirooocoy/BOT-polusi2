# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import os
import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='>', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    # random local meme image
@bot.command()
async def mem(ctx):
    with open('mem/mem1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


# Event ketika bot sudah siap
@bot.event
async def on_ready():
    print('Bot telah siap!')

# Command untuk melakukan perkalian
@bot.command()
async def perkalian(ctx, angka1: int, angka2: int):
    hasil = angka1 * angka2
    await ctx.send(f'Hasil dari {angka1} * {angka2} adalah {hasil}')


# Event yang dipanggil ketika bot siap
@bot.event
async def on_ready():
    print('Bot is ready.')

# Command untuk memberikan informasi tentang polusi
@bot.command()
async def info(ctx):
    info_message = ("Polusi udara, air, dan tanah merupakan masalah lingkungan serius yang berdampak buruk pada kesehatan manusia dan lingkungan."
                    "Beberapa penyebab polusi termasuk emisi kendaraan bermotor, limbah industri, dan penggunaan bahan bakar fosil."
                    "Untuk mengurangi polusi, kita dapat mengambil langkah-langkah seperti mengurangi penggunaan kendaraan pribadi, "
                    "menggunakan energi terbarukan, dan memperbaiki infrastruktur sanitasi.")
    await ctx.send(info_message)

# Command untuk memberikan saran mengurangi polusi
@bot.command()
async def saran(ctx):
    saran_message = ("Berikut adalah beberapa saran untuk mengurangi polusi:\n"
                     "1. Gunakan transportasi umum, bersepeda, atau berjalan kaki jika memungkinkan.\n"
                     "2. Kurangi penggunaan listrik dengan mematikan peralatan saat tidak digunakan.\n"
                     "3. Daur ulang dan daur ulang sampah untuk mengurangi limbah.\n"
                     "4. Dukung upaya perlindungan lingkungan dan regulasi yang membatasi emisi polutan.")
    await ctx.send(saran_message)

# Command untuk memberikan informasi tentang dampak polusi
@bot.command()
async def dampak(ctx):
    dampak_message = ("Polusi dapat memiliki dampak yang luas, termasuk:\n"
                      "- Gangguan kesehatan seperti gangguan pernapasan, iritasi mata, dan penyakit kronis.\n"
                      "- Kerusakan lingkungan seperti pencemaran air, kerusakan hutan, dan kerusakan ekosistem.")
    await ctx.send(dampak_message)

# Command untuk menginspirasi tindakan lingkungan
@bot.command()
async def tindakan(ctx):
    tindakan_message = ("Anda dapat membantu mencegah polusi dengan mengambil tindakan seperti:\n"
                        "- Menggunakan energi terbarukan seperti panel surya atau turbin angin.\n"
                        "- Menanam pohon dan mengikuti program penanaman pohon lokal.\n"
                        "- Bergabung dengan kelompok lingkungan atau kampanye kesadaran lingkungan.")
    await ctx.send(tindakan_message)
