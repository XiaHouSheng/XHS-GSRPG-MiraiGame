import requests
from bs4 import BeautifulSoup
import os
import json
data = [
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3564/detail?bbs_presentation_style=no_header",
        "name": "八重神子",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/15/6276411/2a54cd4008e8bc398f3f8bdc08225048_2883595654384922672.jpg?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3387/detail?bbs_presentation_style=no_header",
        "name": "云堇",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/01/05/16314655/6f4bbe7d060f72a0c84e868887ac7a32_4711867403945994990.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3386/detail?bbs_presentation_style=no_header",
        "name": "申鹤",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/01/05/16314655/e2dfeee83654c0a6a7436b7c120c105a_6628180966971160404.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3276/detail?bbs_presentation_style=no_header",
        "name": "荒泷一斗",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/12/14/16314655/567d0cf114a7f799d650df6e4c7cc0e2_8422200515118882596.jpg?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3275/detail?bbs_presentation_style=no_header",
        "name": "五郎",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/12/14/16314655/1535aaa6189d4262445c0a66ead22eb9_8396030312270652951.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2040/detail?bbs_presentation_style=no_header",
        "name": "优菈",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/525f808e85fb7a13c37debaf3c7d1463_4010662131576296773.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1360/detail?bbs_presentation_style=no_header",
        "name": "阿贝多",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/01009cc20f9a4ebf4ece5e96fdecad1a_3067405046796818316.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2606/detail?bbs_presentation_style=no_header",
        "name": "托马",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/11/02/16314655/f4b404cae89b96327a5b87500f7833c9_6577116317420146203.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1627/detail?bbs_presentation_style=no_header",
        "name": "胡桃",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/8980427ee3cecce2a46400d2c0af6d20_4290442929626456243.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1220/detail?bbs_presentation_style=no_header",
        "name": "达达利亚",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/c0a4fcefc01b018856439e023dd4dc7a_6675006735371357498.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2404/detail?bbs_presentation_style=no_header",
        "name": "雷电将军",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/09/01/16314655/4f2125e44d2b9e15611877eda1794ec7_7083452076426995696.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2403/detail?bbs_presentation_style=no_header",
        "name": "珊瑚宫心海",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/09/21/75379475/5f6f5d0c81155aea5c939ba08249e5d5_6649173224604660824.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2415/detail?bbs_presentation_style=no_header",
        "name": "埃洛伊",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/11/05/10875381/65886603cf7f0bdbaa82a165898237a3_1473519897376013260.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2124/detail?bbs_presentation_style=no_header",
        "name": "宵宫",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/10/75276545/43014af35ae9c4cdf19a8323aa04a0a9_2108182380466335233.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2123/detail?bbs_presentation_style=no_header",
        "name": "神里绫华",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/21/75276545/eaef31b81b190dc676413b099c540526_6543346382757797116.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2142/detail?bbs_presentation_style=no_header",
        "name": "枫原万叶",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/2566b97ea262980d9bcd7db6a116bfd4_6795571745044574054.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/57/detail?bbs_presentation_style=no_header",
        "name": "温迪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/3008da32b80ba05f243bc2c858b534b5_540461000064419548.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1058/detail?bbs_presentation_style=no_header",
        "name": "刻晴",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/666155bbd60391341253e4b1daace9d4_2687379046030308520.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1057/detail?bbs_presentation_style=no_header",
        "name": "莫娜",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/16/6276411/d7d8e4a15f70e31a16edaa6d7389437f_2242463119371173498.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/55/detail?bbs_presentation_style=no_header",
        "name": "可莉",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/06/21/283462834/d2972c634d9d81979774b22b49d1ab01_887661176891008491.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/59/detail?bbs_presentation_style=no_header",
        "name": "琴",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/16/6276411/a7608c6a588467440f7685a22ab6547c_3946325001679449884.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/75/detail?bbs_presentation_style=no_header",
        "name": "迪卢克",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/8ae58465155b31a21319522383027436_4999468226785017726.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1056/detail?bbs_presentation_style=no_header",
        "name": "七七",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/a08d22cf34d2836519a80a8537fe12c8_7861266877849414180.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1498/detail?bbs_presentation_style=no_header",
        "name": "魈",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/a02533e3ac055344982bcfd04865ae72_6103227973780149519.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1290/detail?bbs_presentation_style=no_header",
        "name": "钟离",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/6682780141a9e7788da99c71b1cfd5c3_6751062493374563471.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1433/detail?bbs_presentation_style=no_header",
        "name": "甘雨",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/8b9946e573bf7aff9801c580707a23e1_3026364173026253689.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/53/detail?bbs_presentation_style=no_header",
        "name": "旅行者",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/11/24/183046623/10b36827c0b4429a54e1d04ff75b673d_7756629149373307293.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2125/detail?bbs_presentation_style=no_header",
        "name": "早柚",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/10/75276545/4f50355892c08017346ea3ab80071b9c_1725343112540399387.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2402/detail?bbs_presentation_style=no_header",
        "name": "九条裟罗",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/09/01/16314655/5284b4f47bf6d9e9451d79ad5066d744_9148992125502860596.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/78/detail?bbs_presentation_style=no_header",
        "name": "凝光",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/e4e41cdfac3bdc225f0b847f2cc2cd72_5640782607282153058.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/382/detail?bbs_presentation_style=no_header",
        "name": "菲谢尔",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/18a67c8802d7184db1449693908fe6cf_7858478886557060389.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/105/detail?bbs_presentation_style=no_header",
        "name": "班尼特",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/498b43ef0d21c4e2c1d7a1dea0deea3f_2145838239611168396.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/92/detail?bbs_presentation_style=no_header",
        "name": "丽莎",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/014d59ec5b78c3499b90f45fc80c00a4_5392359609224242061.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/241/detail?bbs_presentation_style=no_header",
        "name": "行秋",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/cd48b60376438c60dbaaa8a85e6a480b_2048377578381627282.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1221/detail?bbs_presentation_style=no_header",
        "name": "迪奥娜",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/759f0ebba20d33f606c2ecc025b9b586_6011368354846344391.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/54/detail?bbs_presentation_style=no_header",
        "name": "安柏",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/16/6276411/138132721f21bf60c53a8935a8fb0107_8908120754759624960.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/644/detail?bbs_presentation_style=no_header",
        "name": "重云",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/0bd80f58871b97281be47fcd6e2d7487_1302151446666002486.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/56/detail?bbs_presentation_style=no_header",
        "name": "雷泽",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/24edfa5586de73329a2b2c5c5d4262a3_3505783202009716970.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/61/detail?bbs_presentation_style=no_header",
        "name": "芭芭拉",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/7f1ac500bafa0526438e4e5b95165991_9116453886373904076.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1744/detail?bbs_presentation_style=no_header",
        "name": "罗莎莉亚",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/16/6276411/bdec34acae15315368017c1dbc29e106_1767613545250694082.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/112/detail?bbs_presentation_style=no_header",
        "name": "香菱",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/83a69074378a0837ca65d33e9052d729_6648871595979928785.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/76/detail?bbs_presentation_style=no_header",
        "name": "凯亚",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/60d8b985eef1e6e0e959410893a75dc0_6659933186171988912.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/79/detail?bbs_presentation_style=no_header",
        "name": "北斗",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/0f7406a1ea1b7fb827d7abe14bfe83e8_3108123811393147392.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/111/detail?bbs_presentation_style=no_header",
        "name": "诺艾尔",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/5cd5b91e504b2466197796cb26fcb7be_508847912159113655.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1055/detail?bbs_presentation_style=no_header",
        "name": "砂糖",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/b30efaf1e19725ddda490a2028b17464_6998283335917930867.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1291/detail?bbs_presentation_style=no_header",
        "name": "辛焱",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/a4b09e58a0d52ea0808b4cef5725ac93_6743022430414510479.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1795/detail?bbs_presentation_style=no_header",
        "name": "烟绯",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/23/75276545/b8952d8a5d2d266126ce370c4eb78438_4209492093986588378.png?x-oss-process=image/quality,q_75/resize,s_120"
    }
]

"""
list=document.getElementsByClassName("collection-avatar")[0].children
a=[]
for(var i=0;i<list.length;i++){
    item=list[i]
    a[i]={"href":item.href,"name":item.innerText,"pic":item.children[0].dataset['src']}
}
console.log(a)
"""


def  getMemberValue(url):
    testUrl = "https://bbs.mihoyo.com/ys/obc/content/3564/detail?bbs_presentation_style=no_header"
    a = requests.get(testUrl)
    a.encoding = "utf-8"
    soup = BeautifulSoup(a.text, "lxml")
    li = soup.find_all("li", {"class": "obc-tmpl__switch-item"})
    starttds = [i for i in next(li[7].children).children][-1].find_all("td")
    start = [{starttds[i].getText(): starttds[i + 1].getText()} for i in range(len(starttds)) if i % 2 == 0]
    endtds = [i for i in next(li[0].children).children][-1].find_all("td")
    end = [{endtds[i].getText(): endtds[i + 1].getText()} for i in range(len(endtds)) if i % 2 == 0]
    D_value = {"ATK": int(start[2]["攻击力"].split("（")[0]) - int(end[4]["攻击力"].split("（")[0]),
               "AFK": int(start[1]["防御力"]) - int(end[6]["防御力"]), "HP": int(start[0]["生命值"]) - int(end[2]["生命值"])}
    S_value = {"ATK": int(end[4]["攻击力"].split("（")[0]), "AFK": int(end[6]["防御力"]), "HP": int(end[2]["生命值"])}
    star=sum(1 for _ in soup.find_all("div",{"class":"obc-tmp-character__box--stars"})[0].children)
    return [D_value, S_value,star]

if __name__ == '__main__':
    for i in data:
        name = str(i["name"])
        pic = i["pic"]
        url = i["href"]
        path="./data/resources/image/character/" + name + ".png"
        if not os.path.exists(path):
            with open(path, "wb") as image:
                image.write(requests.get(pic).content)
                image.close()
        with open("./data/resources/information/character/" + name + ".json","w") as file:
            value=getMemberValue(url)
            result={"name":name,"pic":path,"D-value":value[0],"S-value":value[1],"star":value[2]}
            file.write(json.dumps(result))
            file.close()
        print(name+" 数据同步成功！")

