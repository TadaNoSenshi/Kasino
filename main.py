import discord
import os
import asyncio
import time
import json
import datetime as dt
import random
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(),case_insensitive=True)
slash = SlashCommand(bot, sync_commands=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print("Ich bin bereit!")


async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("!help"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{len(set(bot.users))} Member"))
        await asyncio.sleep(10)

@bot.command()
async def hilfe(ctx):
    embed=discord.Embed(title="Hilfe zum Bot", color=0x10b6e0)
    embed.add_field(name="Allgemein:", value="!bank - Schau dir an wie viel Geld du hast\n!transfer - Zahle Geld auf "
                                             "die Bank ein\n!abheben - Hebe Geld von der Bank ab\n!arbeit - Deine "
                                             "Tägliche Arbeit\n!glück - Gewinnst du, "
                                             "dann lohnt es sich\n!überweisen - schicke einem User Geld\n!clear - "
                                             "Setze den Bank acc. eines Users zurück\n!leaderboard - Sehe die "
                                             "reichesten im Server\n!shop - Schau dir den Shop an\n!shop <nummer> - "
                                             "Kaufe etwas aus dem Shop\n!tasche - sehe deine gekauften "
                                             "gegenstände\n!öffnen <nummer> öffne etwas aus deiner Tasche")
    await ctx.send(embed=embed)

@bot.command()
async def bank(ctx, member: discord.Member = None):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if member == None:
        if not str(ctx.guild.id) in data:
            data[str(ctx.guild.id)] = {}
        if not str(ctx.author.id) in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
            with open("bank.json", "w") as f:
                json.dump(data, f, indent=4)
        bar = data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
        bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
        embed = discord.Embed(title="Bank", description=f"{ctx.author}", color=0x10b6e0)
        embed.add_field(name="Bar:", value=f"{bar} <:moneybag:904819147660218448>", inline=True)
        embed.add_field(name="Bank:", value=f"{bank} <:moneybag:904819147660218448>", inline=True)
        await ctx.send(embed=embed)
    else:
        if not str(ctx.guild.id) in data:
            data[str(ctx.guild.id)] = {}
        if not str(member.id) in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(member.id)] = {}
            data[str(ctx.guild.id)][str(member.id)]['Bar'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Bank'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Kleine Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Normale Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Teure Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Reiche Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Bronze Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Silber Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Gold Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Diamant Kiste'] = 0
            data[str(ctx.guild.id)][str(member.id)]['Platin Kiste'] = 0
            with open("bank.json", "w") as f:
                json.dump(data, f, indent=4)
        bar = data[str(ctx.guild.id)][str(member.id)]['Bar']
        bank = data[str(ctx.guild.id)][str(member.id)]['Bank']
        embed = discord.Embed(title="Bank", description=f"{member}", color=0x10b6e0)
        embed.add_field(name="Bar:", value=f"{bar} <:moneybag:904819147660218448>", inline=True)
        embed.add_field(name="Bank:", value=f"{bank} <:moneybag:904819147660218448>", inline=True)
        await ctx.send(embed=embed)


@bot.command()
async def transfer(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(ctx.author.id)] = {}
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    bar = data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    transfer = bar + bank
    if bar == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld zum transferieren", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bar <= 1:
        embed = discord.Embed(title="Fehler",
                              description="Du hast musst erst wieder ins Plus kommen um Geld zu transferieren",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = transfer
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Transfer Erfolgreich",
                          description=f"Dir wurden {bar} <:moneybag:904819147660218448> gut geschrieben",
                          color=0x10b6e0)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(administrator=True)
async def überweisen(ctx, member: discord.Member = None, arg=None):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(ctx.author.id)] = {}
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if member == None:
        embed = discord.Embed(title="Fehler",
                              description="Du musst einen User angeben an den du das Geld überweisen willst",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    if arg == None:
        embed = discord.Embed(title="Fehler",
                              description="Du musst einen Wert angeben und einen User an den du das Geld überweisen willst",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    if not str(member.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(member.id)] = {}
        data[str(ctx.guild.id)][str(member.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(member.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    bankuser = data[str(ctx.guild.id)][str(member.id)]['Bank']
    if bank <= int(arg):
        embed = discord.Embed(title="Fehler", description="Du hast nicht so viel Geld zum überweisen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld zum überweisen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= 1:
        embed = discord.Embed(title="Fehler",
                              description="Du hast musst erst wieder ins Plus kommen um Geld zu Überweisen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] -= int(arg)
    data[str(ctx.guild.id)][str(member.id)]['Bank'] += int(arg)
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Überweisung erfolgreich",
                          description=f"{ctx.author.mention} hat {member.mention} {arg} <:moneybag:904819147660218448> überwiesen",
                          color=0x10b6e0)
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def arbeit(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(ctx.author.id)] = {}
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    plus = random.randint(20, 63)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += plus
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    bar = data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
    embed = discord.Embed(title="Arbeit", description=f"{ctx.author}", color=0x10b6e0)
    embed.add_field(name="Heute verdient:", value=f"{plus} <:moneybag:904819147660218448>", inline=True)
    embed.add_field(name="Aktuelles Bargeld:", value=f"{bar} <:moneybag:904819147660218448>", inline=True)
    embed.add_field(name="Notiz", value=f"Komm morgen wieder um wieder zu arbeiten", inline=False)
    await ctx.send(embed=embed)


@arbeit.error
async def mine_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Cooldown",
                              description='Oh, du kannst erst wieder in {:.2f} Stunde(n) arbeiten'.format(
                                  error.retry_after / 60 / 60), color=0xff0000)
        await ctx.send(embed=embed)
    else:
        raise error


@bot.command(name="glück")
@commands.cooldown(1, 30, commands.BucketType.user)
async def glueck(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(ctx.author.id)] = {}
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    plus = random.randint(-33, 45)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += plus
    bar = data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    if plus >= 1:
        embed = discord.Embed(title="Glück gehabt", description=f"{ctx.author}", color=0x10b6e0)
        embed.add_field(name="Du gewinnst:", value=f"{plus} <:moneybag:904819147660218448>", inline=True)
        embed.add_field(name="Aktuelles Bargeld:", value=f"{bar} <:moneybag:904819147660218448>", inline=True)
        await ctx.send(embed=embed)
    if plus <= 0:
        embed = discord.Embed(title="Pech gehabt", description=f"{ctx.author}", color=0x10b6e0)
        embed.add_field(name="Du verlierst:", value=f"{plus} <:moneybag:904819147660218448>", inline=True)
        embed.add_field(name="Aktuelles Bargeld:", value=f"{bar} <:moneybag:904819147660218448>", inline=True)
        await ctx.send(embed=embed)


@glueck.error
async def glueck_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Cooldown",
                              description='Oh, du kannst erst wieder in {:.2f} Sekunde(n) spielen'.format(
                                  error.retry_after), color=0xff0000)
        await ctx.send(embed=embed)
    else:
        raise error


@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, member: discord.Member):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    data[str(ctx.guild.id)][str(member.id)] = {}
    data[str(ctx.guild.id)][str(member.id)]['Bar'] = 0
    data[str(ctx.guild.id)][str(member.id)]['Bank'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
    data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Reset Bestätigt", description=f"User: {member}", color=0x10b6e0)
    await ctx.send(embed=embed)


@clear.error
async def clear_error(ctx):
    embed = discord.Embed(title="Fehler", description="Dieser User hat kein Konto :shrug:", color=0xff0000)
    await ctx.send(embed=embed)


@bot.command()
async def leaderboard(ctx, x=10):
    with open('bank.json', 'r') as f:

        data = json.load(f)

    leaderboard = {}
    total = []

    for user in list(data[str(ctx.guild.id)]):
        name = int(user)
        total_amt = data[str(ctx.guild.id)][str(user)]['Bank']
        leaderboard[total_amt] = name
        total.append(total_amt)

    total = sorted(total, reverse=True)

    em = discord.Embed(
        title=f'Top {x} highest leveled members in Server:\n{ctx.guild.name}',
        description='Congratulations to:', color=0xff00c8
    )
    embed = discord.Embed(title=f'Top {x} reichste User in:\n{ctx.guild.name}', color=0x10b6e0)

    index = 1
    for amt in total:
        id_ = leaderboard[amt]
        member = bot.get_user(id_)

        embed.add_field(name=f'{index}: {member}', value=f'╠ {amt} <:moneybag:904819147660218448>', inline=False)
        if index == x:
            break
        else:
            index += 1
    await ctx.send(embed=embed)


@bot.command()
async def abheben(ctx, arg=None):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        data[str(ctx.guild.id)][str(ctx.author.id)] = {}
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] = 0
        data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] = 0
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    bar = data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    if arg == None:
        embed = discord.Embed(title="Fehler", description="Du musst einen Wert angeben den du abheben willst",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld zum abheben", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= 1:
        embed = discord.Embed(title="Fehler", description="Du hast musst erst wieder ins Plus kommen um Geld abzuheben",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    transfer = int(arg)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += transfer
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank'] -= transfer
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Transfer Erfolgreich",
                          description=f"Du hast {transfer} <:moneybag:904819147660218448> abgehoben", color=0x10b6e0)
    await ctx.send(embed=embed)

@bot.group(invoke_without_command=True)
async def shop(ctx):
    embed=discord.Embed(title="Willkommen im Shop", color=0x10b6e0)
    embed.add_field(name="9. Platin Kiste", value="75.000 <:moneybag:904819147660218448>")
    embed.add_field(name="8. Diamant Kiste", value="50.000 <:moneybag:904819147660218448>")
    embed.add_field(name="7. Gold Kiste", value="33.400 <:moneybag:904819147660218448>")
    embed.add_field(name="6. Silber Kiste", value="12.520 <:moneybag:904819147660218448>")
    embed.add_field(name="5. Bronze Kiste", value="2.990 <:moneybag:904819147660218448>")
    embed.add_field(name="4. Reiche Kiste", value="2.500 <:moneybag:904819147660218448>")
    embed.add_field(name="3. Teure Kiste", value="1.300 <:moneybag:904819147660218448>")
    embed.add_field(name="2. Normale Kiste", value="900 <:moneybag:904819147660218448>")
    embed.add_field(name="1. Kleine Kiste", value="500 <:moneybag:904819147660218448>")
    embed.set_footer(text="Nutze !shop <Nummer> zum Kaufen")
    await ctx.send(embed=embed)

@shop.command(name="1")
async def one(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= 499:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {500-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    kosten=500
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 kleine Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** kleine Kiste(n)")
    await ctx.send(embed=embed)


@shop.command(name="2")
async def two(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 899
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Normale Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Normale Kiste(n)")
    await ctx.send(embed=embed)

@shop.command(name="3")
async def three(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 1299
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Teure Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Teure Kiste(n)")
    await ctx.send(embed=embed)

@shop.command(name="4")
async def four(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 2499
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Reiche Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Reiche Kiste(n)")
    await ctx.send(embed=embed)


@shop.command(name="5")
async def five(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 2989
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Bronze Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Bronze Kiste(n)")
    await ctx.send(embed=embed)


@shop.command(name="6")
async def six(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 12519
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Silber Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Silber Kiste(n)")
    await ctx.send(embed=embed)


@shop.command(name="7")
async def seven(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 33399
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Gold Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Gold Kiste(n)")
    await ctx.send(embed=embed)


@shop.command(name="8")
async def eight(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 49999
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Diamant Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Diamant Kiste(n)")
    await ctx.send(embed=embed)

@shop.command(name="9")
async def nine(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    bank = data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    kosten = 54999
    if bank == 0:
        embed = discord.Embed(title="Fehler", description="Du hast kein Geld um was zu kaufen", color=0xff0000)
        await ctx.send(embed=embed)
        return
    if bank <= kosten:
        embed = discord.Embed(title="Fehler", description=f"Dir fehlen {kosten-bank} <:moneybag:904819147660218448> um etwas zu kaufen",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']-=kosten
    data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste']+=1
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    kiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste']
    embed = discord.Embed(title="Kauf Erfolgreich",
                          description=f"Du hast 1 Platin Kiste gekauft", color=0x10b6e0)
    embed.add_field(name="Du hast jetzt:", value=f"**{kiste}** Platin Kiste(n)")
    await ctx.send(embed=embed)


@bot.command()
async def tasche(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Tasche", description="Deine Tasche ist leer", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    bar=data[str(ctx.guild.id)][str(ctx.author.id)]['Bar']
    bank=data[str(ctx.guild.id)][str(ctx.author.id)]['Bank']
    klkiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste']
    nokiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste']
    tekiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste']
    rekiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste']
    brkiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste']
    sikiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste']
    gokiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste']
    dikiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste']
    plkiste=data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste']
    embed=discord.Embed(title="Tasche", color=0x10b6e0)
    if klkiste>=1:
        embed.add_field(name="1. Kleine Kisten:", value=f"```{klkiste} stk.```")
    if nokiste>=1:
        embed.add_field(name="2. Normale Kisten:", value=f"```{nokiste} stk.```")
    if tekiste>=1:
        embed.add_field(name="3. Teure Kisten:", value=f"```{tekiste} stk.```")
    if rekiste>=1:
        embed.add_field(name="4. Reiche Kisten:", value=f"```{rekiste} stk.```")
    if brkiste>=1:
        embed.add_field(name="5. Bronze Kisten:", value=f"```{brkiste} stk.```")
    if sikiste>=1:
        embed.add_field(name="6. Silber Kisten:", value=f"```{sikiste} stk.```")
    if gokiste>=1:
        embed.add_field(name="7. Gold Kisten:", value=f"```{gokiste} stk.```")
    if dikiste>=1:
        embed.add_field(name="8. Diamant Kisten:", value=f"```{dikiste} stk.```")
    if plkiste>=1:
        embed.add_field(name="9. Platin Kisten:", value=f"```{plkiste} stk.```")
    embed.set_footer(text="Um eine Kiste zu öffnen nutze !öffne <Zahl>")
    await ctx.send(embed=embed)


@bot.group(name="öffnen", invoke_without_command=True)
async def oeffnen(ctx):
    embed=discord.Embed(title="Öffnen",description="Nutze !öffnen <nummer> um eine Kiste zu öffnen.", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="1")
async def openone(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine kleine Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    klkiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste']
    if klkiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine kleine Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,5)
    if auswahl==5:
        gewinn=1000
    else:
        gewinn=random.randint(200,500)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Kleine Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)


@oeffnen.command(name="2")
async def opentwo(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Normale Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    nokiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste']
    if nokiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Normale Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,5)
    if auswahl==5:
        gewinn=1500
    else:
        gewinn=random.randint(450,1000)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Normale Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="3")
async def openthree(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Teure Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    tekiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste']
    if tekiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Teure Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,5)
    if auswahl==5:
        gewinn=2350
    else:
        gewinn=random.randint(999,1300)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Teure Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="4")
async def openfour(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Reiche Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    rekiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste']
    if rekiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Reiche Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,5)
    if auswahl==5:
        gewinn=2800
    else:
        gewinn=random.randint(1300,2400)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Reiche Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="5")
async def openfive(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Bronze Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    brkiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste']
    if brkiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Bronze Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,8)
    if auswahl==8:
        gewinn=5000
    else:
        gewinn=random.randint(2000,3000)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bronze Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="6")
async def opensix(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Silber Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    sikiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste']
    if sikiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Silber Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,8)
    if auswahl==8:
        gewinn=18000
    else:
        gewinn=random.randint(8000,13520)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Silber Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="7")
async def openseven(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Gold Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    gokiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste']
    if gokiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Gold Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,9)
    if auswahl==9:
        gewinn=40000
    else:
        gewinn=random.randint(20000,35400)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Gold Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="8")
async def openeight(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Diamant Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    dikiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste']
    if dikiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Diamant Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,10)
    if auswahl==9:
        gewinn=60000
    else:
        gewinn=random.randint(40000,51000)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Diamant Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

@oeffnen.command(name="9")
async def opennine(ctx):
    with open("bank.json", "r") as f:
        data = json.load(f)
    if not str(ctx.guild.id) in data:
        data[str(ctx.guild.id)] = {}
        with open("bank.json", "w") as f:
            json.dump(data, f, indent=4)
    if not str(ctx.author.id) in data[str(ctx.guild.id)]:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Platin Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    plkiste = data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste']
    if plkiste<1:
        embed = discord.Embed(title="Öffnen", description="Du hast keine Platin Kiste", color=0x10b6e0)
        await ctx.send(embed=embed)
        return
    auswahl=random.randint(1,15)
    if auswahl==15:
        gewinn=100000
    else:
        gewinn=random.randint(50000,85000)
    data[str(ctx.guild.id)][str(ctx.author.id)]['Platin Kiste'] -= 1
    data[str(ctx.guild.id)][str(ctx.author.id)]['Bar'] += gewinn
    with open("bank.json", "w") as f:
        json.dump(data, f, indent=4)
    embed = discord.Embed(title="Glückwunsch", description=f"Du hast {gewinn} <:moneybag:904819147660218448> bekommen", color=0x10b6e0)
    await ctx.send(embed=embed)

bot.run("TOKEN")
