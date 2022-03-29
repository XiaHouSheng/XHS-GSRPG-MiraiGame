"""玩家的数据管理"""
import os
import json


class Data:
    def __init__(self, filename, local_path):
        self.result = {}
        self.__local_path = local_path
        self.filename = filename
        self.data_file_path = self.__local_path + self.filename + ".json"
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, "w") as file:
                data = {}
                file.write(json.dumps(data))
                file.close()
                print("%s.json Create Successfully!" % self.filename)
        else:
            with open(self.data_file_path, "r+") as file:
                self.result = json.load(file)
                file.close()

    def delete(self):
        os.remove(self.data_file_path)
        print("%s.json Delete Successfully!" % self.filename)

    def addProject(self, name, content):
        self.result[name] = content

    def save(self):
        with open(self.data_file_path, "r+") as file:
            file.write(self.result)
            file.close()


class Player(Data):
    def __init__(self, qid, nickname):
        super().__init__(qid, "./player-data/")
        self.nickname = nickname
        if not os.path.exists(self.data_file_path):
            self.addProject("nickname", nickname)
            self.addProject("qid", qid)
            self.addProject("numPet", 0)
            self.addProject("items", [{"纠缠之缘": 10}])
            self.addProject("member", [])
            self.save()

    def addItem(self, what: str, nums: int):
        self.result["items"].append({what: nums})

    def getItems(self):
        return self.result["items"]
