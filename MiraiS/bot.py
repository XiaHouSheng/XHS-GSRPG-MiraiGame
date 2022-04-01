import asyncio
import websockets
import requests
import json
import Message

class bot:
    def __init__(self):
        session = json.loads(requests.post(url="http://127.0.0.1:5700/verify", json={"verifyKey": "mzxclhml10"}).text)[
            "session"]
        requests.get("http://127.0.0.1:5700/bind", json={"sessionKey": session, "qq": 213303398})
        self._taskes = {}

    async def OnMsg(self,func):
        async with websockets.connect("ws://localhost:5701/message?verifyKey=mzxclhml10&qq=213303398") as websocket:
            self.session = json.loads(await websocket.recv())["data"]["session"]
            while True:
                recv_text = await websocket.recv()
                MessageObj = Message.Messgae(data=recv_text)
                print(MessageObj.__str__())
                if MessageObj.messageType=="GroupMessage":
                    await func["GroupMsg"](MessageObj)
                elif MessageObj.messageType=="FriendMessage":
                    await func["FriendMsg"](MessageObj)


    async def OnEvent(self):
        async with websockets.connect("ws://localhost:5701/event?verifyKey=mzxclhml10&qq=213303398") as websocket:
            self.session = json.loads(await websocket.recv())["data"]["session"]
            while True:
                recv_text = await websocket.recv()
                #Event~~~

    def register(self,text):
        def wrapper(func):
            self._taskes[text]=func
        return wrapper

    def runServer(self):
        asyncio.get_event_loop().run_until_complete(self.OnMsg(self._taskes))


bot = bot()


@bot.register("GroupMsg")
async def onMsg(data):
    pass

@bot.register("FriendMsg")
async def onMsg(data):
    pass

bot.runServer()
