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
            self.addProject("numCharacter", 0)
            self.addProject("characters", [{'name': '旅行者', 'pic': './data/resources/image/character/旅行者.png',
                                            'level': 1,
                                            'D-value': {'ATK': 313, 'AFK': 525, 'HP': 9565},
                                            'S-value': {'ATK': 50, 'AFK': 44, 'HP': 807},
                                            'star': 5,
                                            'weapons': {'name': '无锋剑',
                                                        'pic': './data/resources/image/weapon/无锋剑.png',
                                                        'D-value': 162,
                                                        'S-value': 23,
                                                        'star': 1,
                                                        'type': '单手剑'},
                                            'sacred-relics': []
                                            }
                                           ])
            self.addProject("items", [{"纠缠之缘": 90}])
            self.addProject("quantityChouKa", 0)
            self.save()

    def addItem(self, what: str, nums: int):
        self.result["items"].append({what: nums})

    def getItems(self, key):
        if key not in self.result:
            return None
        return self.result[key]
