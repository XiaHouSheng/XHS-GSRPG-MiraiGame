from MiraiS import bot
from data import DataManger
from MiraiS import Message

bot = bot(port="5700", qid=213303398, verifykey="mzxclhml10")
session = bot.session


@bot.register("GroupMsg")
async def onMsg(data):
    pass


@bot.register("FriendMsg")
async def onMsg(data):
    print(data)


bot.runServer()
