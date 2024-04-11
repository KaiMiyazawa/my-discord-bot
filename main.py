import discord

TOKEN = "" # botのアクセストークンを書き込む

bot = discord.Bot(
        intents=discord.Intents.all(),  # 全てのインテンツを利用できるようにする
        activity=discord.Game("Discord Bot入門"),  # "〇〇をプレイ中"の"〇〇"を設定,
)


@bot.event
async def on_ready():
    # 起動すると、実行したターミナルに"Hello!"と表示される
    print("Hello!")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content == 'hello':
        await message.reply("Hello!")

@bot.command(name="ping", description="pingを返します")
async def ping(ctx: discord.ApplicationContext):
	await ctx.respond("pong")

@bot.command(name="greeting", description="挨拶を行います")
async def greeting(ctx: discord.ApplicationContext, user: discord.Option(discord.User, "対象のユーザー")):
    await ctx.respond(f"Hi, {user.mention}!")

@bot.command(name="mon", description="月曜日の日程調整メッセージを代送します")
async def mon(ctx: discord.ApplicationContext):
	await ctx.respond("月曜１限❤️  ２限🧡  昼休み💛  ３限💚  ４限🩵  ５限💜  ６限🤍")

@bot.command(name="tue", description="火曜日の日程調整メッセージを代送します")
async def tue(ctx: discord.ApplicationContext):
	await ctx.respond("火曜１限❤️  ２限🧡  昼休み💛  ３限💚  ４限🩵  ５限💜  ６限🤍")

@bot.command(name="wed", description="水曜日の日程調整メッセージを代送します")
async def wed(ctx: discord.ApplicationContext):
	await ctx.respond("水曜１限❤️  ２限🧡  昼休み💛  ３限💚  ４限🩵  ５限💜  ６限🤍")

@bot.command(name="thu", description="木曜日の日程調整メッセージを代送します")
async def thu(ctx: discord.ApplicationContext):
	await ctx.respond("木曜１限❤️  ２限🧡  昼休み💛  ３限💚  ４限🩵  ５限💜  ６限🤍")

@bot.command(name="fri", description="金曜日の日程調整メッセージを代送します")
async def fri(ctx: discord.ApplicationContext):
	await ctx.respond("金曜１限❤️  ２限🧡  昼休み💛  ３限💚  ４限🩵  ５限💜  ６限🤍")

@bot.command(name="sat", description="土曜日の日程調整メッセージを代送します")
async def sat(ctx: discord.ApplicationContext):
	await ctx.respond("土曜10:00~12:00❤️  12:00~15:00🧡  15:00~18:00💛\n  18:00~20:00💚  20:00~22:00🩵   22:00~24:00💜")

@bot.command(name="sun", description="日曜日の日程調整メッセージを代送します")
async def sun(ctx: discord.ApplicationContext):
	await ctx.respond("日曜10:00~12:00❤️  12:00~15:00🧡  15:00~18:00💛\n  18:00~20:00💚  20:00~22:00🩵   22:00~24:00💜")

bot.run(TOKEN)

