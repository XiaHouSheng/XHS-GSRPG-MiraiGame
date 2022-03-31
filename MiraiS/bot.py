import asyncio
import websockets
import requests
import json


class bot:
    def __init__(self):
        session = json.loads(requests.post(url="http://127.0.0.1:5700/verify", json={"verifyKey": "mzxclhml10"}).text)[
            "session"]
        requests.get("http://127.0.0.1:5700/bind", json={"sessionKey": session, "qq": 213303398})

    async def OnMsg(self,agrs):
        async with websockets.connect("ws://localhost:5701/message?verifyKey=mzxclhml10&qq=213303398") as websocket:
            self.session=json.loads(await websocket.recv())["data"]["session"]
            while True:
                recv_text = await websocket.recv()
                for i in agrs:
                    await i(recv_text)

    async def OnEvent(self,agrs):
        async with websockets.connect("ws://localhost:5701/event?verifyKey=mzxclhml10&qq=213303398") as websocket:
            self.session = json.loads(await websocket.recv())["data"]["session"]
            while True:
                recv_text = await websocket.recv()
                for i in agrs:
                    await i(recv_text)

    def runServer(self,*args):
        asyncio.get_event_loop().run_until_complete(self.OnMsg(args))



bot = bot()


async def onMsg(data):
    print("message", data)




bot.runServer(onMsg)
