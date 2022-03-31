import json
from io import BytesIO

import requests


class Messgae:
    def __init__(self, data=None, session=None):
        if data:
            result = json.loads(data)
            self.syncID = result["syncId"]
            self.messageType = result["data"]["type"]
            self.contentText = "".join([i["text"] for i in result["data"]["messageChain"] if i["type"] == "Plain"])
            self.images = [Image(i) for i in result["data"]["messageChain"] if i["type"] == "Image"]
            self.voices = [Voice(i) for i in result["data"]["messageChain"] if i["type"] == "Voice"]
            if self.messageType == "GroupMessage":
                self.group = Group(result["group"],session)
                self.sender = Member(result["sender"], True,session)
            else:
                self.group = None
                self.sender = Member(result["sender"], False,session)
        else:
            self.messageChain = []
            self.session = session

    def setText(self, text):
        prepare = {"type": "Plain", "text": text}
        self.messageChain.append(prepare)

    def setVoice(self, voicePath):
        files = {"voice": BytesIO(open(voicePath, "rb").read())}
        data = {"sessionKey": self.session, "type": "group"}
        a = requests.post(url="http://127.0.0.1:5700/uploadVoice", files=files, data=data)
        print(a.text)
        voiceUrl = json.loads(a.text)["url"]
        prepare = {"type": "Voice", "url": voiceUrl}
        self.messageChain.append(prepare)

    def setImage(self, imageType, imagePath):
        files = {"img": BytesIO(open(imagePath, "rb").read())}
        data = {"sessionKey": self.session, "type": imageType}
        a = requests.post(url="http://127.0.0.1:5700/uploadImage", files=files, data=data)
        print(a.text)
        imageUrl = json.loads(a.text)["url"]
        prepare = {"type": "Image", "url": imageUrl}
        self.messageChain.append(prepare)

    def createMessageChain(self):
        return self.messageChain


class Image:
    def __init__(self, data):
        result = json.loads(data)
        self.imageId = result["imageId"]
        self.imageUrl = result["url"]


class Voice:
    def __init__(self, data):
        result = json.loads(data)
        self.voiceId = result["voiceId"]
        self.voiceUrl = result["url"]


class Member:
    def __init__(self, data, isGroup,session):
        result = json.loads(data)
        self.session=session
        self.qid = result["id"]
        self.isGroup=isGroup
        if isGroup:
            self.nickname = result["memberName"]
            self.permission = result["permission"]
            self.joinTimeStamp = result["joinTimeStamp"]
            self.lastSpeckTimeStamp = result["lastSpeckTimeStamp"]
            self.muteTimeRemaining = result["muteTimeRemaining"]
        else:
            self.nickname = result["nickname"]

    def sendMessage(self, messageChain):
        if self.isGroup:
            url = "http://127.0.0.1:5700/sendTempMessage"
        else:
            url = "http://127.0.0.1:5700/sendFriendMessage"
        data = {
            "sessionKey": self.session,
            "target": self.qid,
            "messageChain": messageChain
        }
        requests.post(url, json=data)


class Group:
    def __init__(self, data, session):
        result = json.load(data)
        self.gid = result["id"]
        self.name = result["name"]
        self.permission = result["permission"]
        self.session = session

    def sendMessage(self, messageChain):
        url = "http://127.0.0.1:5700/sendGroupMessage"
        data = {
            "sessionKey": self.session,
            "target": self.gid,
            "messageChain": messageChain
        }
        requests.post(url,json=data)
