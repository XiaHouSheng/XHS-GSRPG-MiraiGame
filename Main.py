from MiraiS.bot import bot
from data.DataManager import Player
from MiraiS.Message import Message

bot = bot()
session = bot.session


@bot.register("GroupMsg")
async def onMsg(data):
    pass


@bot.register("FriendMsg")
async def onMsg(data):
    print(data)


bot.runServer()
