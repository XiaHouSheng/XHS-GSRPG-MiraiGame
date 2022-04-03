from data.DataManager import Player
import random
import hashlib
import time

def LaiYiFa(qid):
    md5 = hashlib.md5(bytes((str(qid)+str(time.time())+"saltyXiaHouSheng").encode("utf-8")))
    seed = md5.hexdigest()
    random.seed(seed)



def LaiShiFa(qid):
    pass
if __name__ == '__main__':
    LaiYiFa(213303398)