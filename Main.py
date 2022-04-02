from MiraiS import bot
from data import DataManger
from MiraiS import Message

bot = bot()
session = bot.session


@bot.register("GroupMsg")
async def onMsg(data):
    pass


@bot.register("FriendMsg")
async def onMsg(data):
    print(data)


bot.runServer()
