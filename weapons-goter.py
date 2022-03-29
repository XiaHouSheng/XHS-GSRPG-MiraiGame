import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import os
import json
import threading

data = [
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3611/detail?bbs_presentation_style=no_header",
        "name": "证誓之明瞳",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/13/75833613/47899a33ddd3f573f55c76df4a7802d2_3094185401289107894.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3563/detail?bbs_presentation_style=no_header",
        "name": "神乐之真意",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/02/13/75833613/97f9c91d1d85b8975969b043e8ff673b_1750342366655799865.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3398/detail?bbs_presentation_style=no_header",
        "name": "息灾",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2022/01/04/75833613/bc53d31707c6d8c7637162871f59ba4e_4605074879267649188.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3274/detail?bbs_presentation_style=no_header",
        "name": "赤角石溃杵",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/11/09/75833613/e09b109aa42cd33d9ff41947909cc770_6764220131208611964.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3170/detail?bbs_presentation_style=no_header",
        "name": "辰砂之纺锤",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/11/09/75833613/14439ff89d1a6919bae74e00d9dc3292_6045879981383934302.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2039/detail?bbs_presentation_style=no_header",
        "name": "松籁响起之时",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/05/12/75833613/9601bc8290aa991fe52c42b81f57a6d2_6288984929976131281.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2129/detail?bbs_presentation_style=no_header",
        "name": "苍古自由之誓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/06/07/75833613/074f153b0401c04bee7434370ef352ee_5371774056196814778.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1682/detail?bbs_presentation_style=no_header",
        "name": "终末嗟叹之诗",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/03/15/75833613/7543084fd200a934c835c5f4e3c43561_1445795416639899431.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1612/detail?bbs_presentation_style=no_header",
        "name": "护摩之杖",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/02/02/75833613/61dfa80da5cbd313dea70b12f48c7048_1985763051506243400.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3077/detail?bbs_presentation_style=no_header",
        "name": "断浪长鳍",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/10/10/75833613/e39e9e7de2b4c8d7e4f82d2a5d78b00a_4188699791331957077.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/3076/detail?bbs_presentation_style=no_header",
        "name": "曚云之月",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/10/11/75833613/dbd17d93d77cb60ccc2cf17327ff95c2_5638231530432896456.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2905/detail?bbs_presentation_style=no_header",
        "name": "冬极白星",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/10/10/75833613/a85b5466576b356e2c9183fadc5ee458_5892604898832964943.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2904/detail?bbs_presentation_style=no_header",
        "name": "恶王丸",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/10/11/75833613/4b661765eb32bfe396348b4bc2faa260_3864520739493627825.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2807/detail?bbs_presentation_style=no_header",
        "name": "不灭月华",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/09/21/75833613/a5bda9f4243ace37da9dd3099f040962_8540832573923720873.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2639/detail?bbs_presentation_style=no_header",
        "name": "掠食者",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/30/75833613/ef3893709fb8e9becbc9376e211552c6_3729425257940998281.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2604/detail?bbs_presentation_style=no_header",
        "name": "「渔获」",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/29/75833613/3af34aa78f6dc38d9daa62fbadf6a712_8204522985688809699.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2603/detail?bbs_presentation_style=no_header",
        "name": "衔珠海皇",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/29/75833613/da92ce666f6f5a37c283b29c2f2eb592_1653541597481079247.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2602/detail?bbs_presentation_style=no_header",
        "name": "薙草之稻光",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/08/29/75833613/8b0a05031b78c76f506045a2a990c411_8186351970748341837.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2555/detail?bbs_presentation_style=no_header",
        "name": "飞雷之弦振",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/19/75833613/c4b968aa853f3180828836d3b856f35d_8616479233096643678.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2289/detail?bbs_presentation_style=no_header",
        "name": "雾切之回光",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/18/75833613/a3eb5b2dbfaed0dc91f39038db3919b2_3947809028567339166.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2302/detail?bbs_presentation_style=no_header",
        "name": "桂木斩长正",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/19/75833613/a7b03317a161f04f66cd839c5ac391c1_1029134430971906843.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2288/detail?bbs_presentation_style=no_header",
        "name": "白辰之环",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/19/75833613/9fd23f11d945191ce94a6f902559e1a2_1227521075884277892.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2310/detail?bbs_presentation_style=no_header",
        "name": "喜多院十文字",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/20/75833613/7783dfe92cfe7e589471ba204ec37f6d_932589671452620706.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2307/detail?bbs_presentation_style=no_header",
        "name": "天目影打刀",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/10/21/75833613/ed49afc0e189b8292bba65e91d19fecf_4776350835348014308.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2287/detail?bbs_presentation_style=no_header",
        "name": "破魔之弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/07/19/75833613/dda4a567d9ae43dc385e1fd3b7b5fed8_657560530658326338.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1298/detail?bbs_presentation_style=no_header",
        "name": "降临之剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/03/75833613/8dddea52e964ac7a53d2c80282f23a4b_2487031582911632276.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/215/detail?bbs_presentation_style=no_header",
        "name": "天空之刃",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/445ee7341d31462920858367cadc6fc1_3531531098390151221.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/218/detail?bbs_presentation_style=no_header",
        "name": "狼的末路",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/22b30db150bfea372b73678157955047_3499980040949492760.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/219/detail?bbs_presentation_style=no_header",
        "name": "阿莫斯之弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/dd995508d235c7cf568836241ccff7cc_9208158740180284853.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/227/detail?bbs_presentation_style=no_header",
        "name": "天空之卷",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/24/75833613/d16313992a8ba86e6ba4a84977b59ca4_8815818653896805010.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/291/detail?bbs_presentation_style=no_header",
        "name": "天空之傲",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/26/75833613/93684c0ffeb85fa7388967a178260f1a_8512604404883559254.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/293/detail?bbs_presentation_style=no_header",
        "name": "风鹰剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/26/75833613/935c2d06ae29f29e51b902d131782b18_2882215894293509229.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/296/detail?bbs_presentation_style=no_header",
        "name": "和璞鸢",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/04/01/75833613/cda9841711c3d126c81a531a02e94953_1861909156499226758.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/297/detail?bbs_presentation_style=no_header",
        "name": "四风原典",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/26/75833613/6804c9a9c7e8444a9e9d41523bc9da04_4817566713925112072.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/323/detail?bbs_presentation_style=no_header",
        "name": "天空之翼",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/29/75833613/05f12093a755817ad3c51f53db1039a4_5002287290900373405.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1077/detail?bbs_presentation_style=no_header",
        "name": "天空之脊",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/09/17/75833613/fe7b0e7f80a4e1c9876d27b89cbc93ec_8576774571833165082.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1222/detail?bbs_presentation_style=no_header",
        "name": "尘世之锁",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/11/03/75833613/229ae0b51f2043284bbb77b08c393efd_4990343147407068786.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1288/detail?bbs_presentation_style=no_header",
        "name": "无工之剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/11/03/75833613/d4ecd5c1f63d73c86a17ad3b382ab95c_6771529426315730357.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1289/detail?bbs_presentation_style=no_header",
        "name": "贯虹之槊",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/11/03/75833613/7b10471712c6fd13d69289320b6823df_4067250632358740826.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1356/detail?bbs_presentation_style=no_header",
        "name": "斫峰之刃",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/23/75833613/16d127e84bb154ad5b18322f8cce9cf2_7289288347603811546.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1497/detail?bbs_presentation_style=no_header",
        "name": "磐岩结绿",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/02/02/75833613/bfa02af5665193d9b8153107d5484e57_8272816573994913980.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/141/detail?bbs_presentation_style=no_header",
        "name": "匣里龙吟",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/157123aec9296f06c27def671ac923b1_3170648805240315119.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/144/detail?bbs_presentation_style=no_header",
        "name": "试作古华",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/8f971bf97933800f22eeb1d1afeec757_5656486488252227606.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/171/detail?bbs_presentation_style=no_header",
        "name": "匣里灭辰",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/b753959a45fc9989e39dd945e8769e4a_6217077251181025856.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/172/detail?bbs_presentation_style=no_header",
        "name": "黑岩刺枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/b4e0f6c437598a77e7660997daf5260a_7404028432687991788.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/174/detail?bbs_presentation_style=no_header",
        "name": "西风大剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/60cca5eecb54f5df17e9aadae0f20116_5349417019139180282.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/175/detail?bbs_presentation_style=no_header",
        "name": "铁蜂刺",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/3aab2b1b2703f755d88330ed161568b1_8216113915867690243.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/176/detail?bbs_presentation_style=no_header",
        "name": "绝弦",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/2ea701466be00898d0ada7d09a2f849c_4135463535146683034.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/177/detail?bbs_presentation_style=no_header",
        "name": "祭礼弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/303b9b8c0b5b7a8b3a9ce4aab816e5d1_5279618247464402934.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/178/detail?bbs_presentation_style=no_header",
        "name": "宗室长弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/5e126c30f3d95cdf7c9d173527e82919_3096417559484041900.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/180/detail?bbs_presentation_style=no_header",
        "name": "雨裁",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/21/75833613/d1004336c0b48f25a7d3546b57bce070_1026700881516126262.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/181/detail?bbs_presentation_style=no_header",
        "name": "弓藏",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/21/75833613/baa762ef9f5c22d30bc249a2ae0dfaea_4031849230616127867.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/185/detail?bbs_presentation_style=no_header",
        "name": "西风秘典",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/d5fd5471553ba8ef97c9a8a1dd967470_2181206993669361058.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/192/detail?bbs_presentation_style=no_header",
        "name": "流浪乐章",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/e827b8eb972d3ac0f42569fe6d5e291b_1329731327757714701.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/193/detail?bbs_presentation_style=no_header",
        "name": "黑岩绯玉",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/58b3373fb5bb57023c89c60d5ede5956_1330376353772326494.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/194/detail?bbs_presentation_style=no_header",
        "name": "宗室秘法录",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/098ee6b954cc8b44400d6ed3c601f107_5142741724020145957.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/195/detail?bbs_presentation_style=no_header",
        "name": "西风猎弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/04/03/75833613/e0761fb637cb5fd3971f4195bbb1b58c_2054410022054716358.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/197/detail?bbs_presentation_style=no_header",
        "name": "祭礼残章",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/fadc9fb70048164753b72345362c0c21_7122974106862334603.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/198/detail?bbs_presentation_style=no_header",
        "name": "万国诸海图谱",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/bb5d973a357ab939cc3c6c193000cfca_8857068874429107380.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/199/detail?bbs_presentation_style=no_header",
        "name": "宗室长剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/22/75833613/de675880f3e60488abec363d5579a502_3227188272282171556.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/206/detail?bbs_presentation_style=no_header",
        "name": "宗室大剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/21ba2927f014300431edad9fc7d519d1_1243866720697859716.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/207/detail?bbs_presentation_style=no_header",
        "name": "笛剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/cf572b27ab0c4934984f05af1307888e_8870622140313865255.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/208/detail?bbs_presentation_style=no_header",
        "name": "西风剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/0b4101418da4c458e2df1ee94953c21f_743806312164207500.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/214/detail?bbs_presentation_style=no_header",
        "name": "钟剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/17fa7c1aaf90e8ee33985e9bede2c57a_8855621887112870500.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/217/detail?bbs_presentation_style=no_header",
        "name": "匣里日月",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/23/75833613/ac439934d1093ab4f9eaac59784f3a0c_3374221950943383956.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/226/detail?bbs_presentation_style=no_header",
        "name": "试作斩岩",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/24/75833613/7916a14d5e0ecaea8a37db5505c01f2e_1831722239667693958.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/239/detail?bbs_presentation_style=no_header",
        "name": "祭礼剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/25/75833613/f9c145f07db2787008c50e7c292a46a2_3901382013212830483.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/240/detail?bbs_presentation_style=no_header",
        "name": "试作澹月",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/24/75833613/6d9776dea64400a58adb4eaf824c1618_8563998658668279437.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/289/detail?bbs_presentation_style=no_header",
        "name": "黑岩长剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/25/75833613/d293b11207ee53181851b43e1d190d7a_1880864215301475464.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/290/detail?bbs_presentation_style=no_header",
        "name": "白影剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/26/75833613/de66a13513908e11123998c9783c6ff7_8816102898562581639.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/319/detail?bbs_presentation_style=no_header",
        "name": "试作金珀",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/27/75833613/043803dbf1729027d76feaa7c24aa67b_1248549900106447863.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/321/detail?bbs_presentation_style=no_header",
        "name": "流月针",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/28/75833613/5c5a76b799e189de9257fe0bad6ab347_9004313317699341160.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/391/detail?bbs_presentation_style=no_header",
        "name": "钢轮弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/04/07/75833613/43246d1471d5297f9e53845ad86d2918_3500168414101532920.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/393/detail?bbs_presentation_style=no_header",
        "name": "试作星镰",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/04/08/75833613/388378b90036d2b75302bb7b67bae64f_7385946179060436684.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/418/detail?bbs_presentation_style=no_header",
        "name": "祭礼大剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/04/11/75833613/642e8c429133fad5355e6d24c0abdb15_8391048341219333900.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/690/detail?bbs_presentation_style=no_header",
        "name": "昭心",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/76373921/dafe7f5cdecac90aec82b1a4ba04ff25_8710250991471280781.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/694/detail?bbs_presentation_style=no_header",
        "name": "黑岩战弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/23/76373921/da4fe7434ec5f0ed5f95cfb9da7a844b_1105425832417481917.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/704/detail?bbs_presentation_style=no_header",
        "name": "黑岩斩刀",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/23/76373921/572b49753770be07dec7065ed8aa9e33_6768616184571698394.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/942/detail?bbs_presentation_style=no_header",
        "name": "黑剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/07/12/76373921/22a34b562052859421a1b0b366093f81_6117536199136265054.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/972/detail?bbs_presentation_style=no_header",
        "name": "决斗之枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/07/13/76373921/bfb97f07e9bc595b008fed2337c7289d_8534797406018130646.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/994/detail?bbs_presentation_style=no_header",
        "name": "苍翠猎弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/07/15/76373921/3de256e8fa28b73278f4c47542b993ff_2093138080143171739.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/995/detail?bbs_presentation_style=no_header",
        "name": "螭骨剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/07/15/76373921/e353e82e5f9a0fc316857d77424fb5c3_3817557115959705341.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1079/detail?bbs_presentation_style=no_header",
        "name": "西风长枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/09/18/75833613/6140a0079a81382e3c44a02a9e84126e_3640803810731897553.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1287/detail?bbs_presentation_style=no_header",
        "name": "宗室猎枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/11/03/75833613/5f0ecdf6675c087059ef9bdcf34f8bb7_8359121231390835579.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1361/detail?bbs_presentation_style=no_header",
        "name": "腐殖之剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/03/75833613/7286ac5c1b6bc93fec0e01c5572ae334_2877649227856685290.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1362/detail?bbs_presentation_style=no_header",
        "name": "雪葬的星银",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/03/75833613/1d809e4dc4cb46d286de580f7d37b84b_2295500733774520474.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1363/detail?bbs_presentation_style=no_header",
        "name": "龙脊长枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/03/75833613/a9505cecd5f3c45d8b857ccff349b35d_8684082608956278787.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1377/detail?bbs_presentation_style=no_header",
        "name": "忍冬之果",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/12/16/75833613/ac42040366e47673837f75b3e7fc1263_8560032881788677555.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1610/detail?bbs_presentation_style=no_header",
        "name": "千岩长枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/02/02/75833613/ea70a04d4aa0df1574e7f3d807551883_6915284450779257640.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1611/detail?bbs_presentation_style=no_header",
        "name": "千岩古剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/02/02/75833613/a457b731ddc05ea27498c1dbab1ad4e9_5817136873215016548.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1683/detail?bbs_presentation_style=no_header",
        "name": "暗巷闪光",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/03/14/75833613/d52c7281587da776ac970159cdd7ab03_5264232383122989255.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1684/detail?bbs_presentation_style=no_header",
        "name": "暗巷猎手",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/03/14/75833613/b52a9211755f000cdddc50aff4fee0e1_2236067199592681632.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1685/detail?bbs_presentation_style=no_header",
        "name": "暗巷的酒与诗",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/03/14/75833613/d09ffbaecf1d7d2719cabd73e34e1640_2955780732199887083.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1705/detail?bbs_presentation_style=no_header",
        "name": "风花之颂",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/03/15/75833613/bb170b4ece7137095f468122bf81e029_6798112072367620156.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2127/detail?bbs_presentation_style=no_header",
        "name": "幽夜华尔兹",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/06/07/75833613/20fae82e8d237efc703cebebe371a32a_7003112924895248286.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/2141/detail?bbs_presentation_style=no_header",
        "name": "嘟嘟可故事集",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2021/06/07/75833613/51be197c4c22bf78d9ce43a7ef93b79e_1541289858348302192.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/128/detail?bbs_presentation_style=no_header",
        "name": "飞天御剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/2f7a7658839225d2180ff05943ffddc1_8130712469611269098.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/129/detail?bbs_presentation_style=no_header",
        "name": "铁影阔剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/9f92bc7c1b1c9f667d8b36a2890dba3c_4966013475177272313.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/130/detail?bbs_presentation_style=no_header",
        "name": "沐浴龙血的剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/6612743f57016119d5d86d65b0bb3c78_6863185488096462582.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/131/detail?bbs_presentation_style=no_header",
        "name": "以理服人",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/059f200b99d098fd1791a5b6df57fb15_2429287944097179245.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/134/detail?bbs_presentation_style=no_header",
        "name": "黑缨枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/abfa4d0c2ac36f7e59d892ad6a929316_7872280644216449533.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/137/detail?bbs_presentation_style=no_header",
        "name": "讨龙英杰谭",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/960be0723a8299db9ccb6a02f74e8e2e_8743657917550828069.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/138/detail?bbs_presentation_style=no_header",
        "name": "弹弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/aac8d2ff61512cad048858d2b40385c4_1738541205265285960.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/139/detail?bbs_presentation_style=no_header",
        "name": "鸦羽弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/3624d7d0a0ef89d91cb1166bac6d5518_603388374697378447.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/161/detail?bbs_presentation_style=no_header",
        "name": "冷刃",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/24bdaea5978d2634d74dad47442d6122_9127538621522062301.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/162/detail?bbs_presentation_style=no_header",
        "name": "魔导绪论",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/c154d6129fabcfd551b6f33b88d06d37_8283966138624579260.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/164/detail?bbs_presentation_style=no_header",
        "name": "黎明神剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/471586149ecedabc50df80a71c1a4e13_7638998658566853121.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/165/detail?bbs_presentation_style=no_header",
        "name": "暗铁剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/21/75833613/fb3ff7f236246073f2f508f1f774a9ab_3182158376215763089.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/167/detail?bbs_presentation_style=no_header",
        "name": "神射手之誓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/8ec0ab79c3a2e30828331e0d53428fec_5600004519324126064.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/220/detail?bbs_presentation_style=no_header",
        "name": "飞天大御剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/24/75833613/e5e54473e2037e6820fbcfc2033be1f8_6519699561249741656.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/683/detail?bbs_presentation_style=no_header",
        "name": "白缨枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/c5f23afc286a3eef8e5ea2e889ca67ff_8576229311507323215.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/684/detail?bbs_presentation_style=no_header",
        "name": "甲级宝珏",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/86bb969cdb644cf54cf0ab62350b2e63_7664010052774139997.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/685/detail?bbs_presentation_style=no_header",
        "name": "异世界行记",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/99f89aff67fb655d40c72b4c9e3c2dbd_3678797272332929121.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/686/detail?bbs_presentation_style=no_header",
        "name": "信使",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/16f64d570b8d5a72000191df60f62601_8526863970829738869.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/687/detail?bbs_presentation_style=no_header",
        "name": "反曲弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/e39707b29fa90b4f113673fba60f9b30_8985143992465766581.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/698/detail?bbs_presentation_style=no_header",
        "name": "吃虎鱼刀",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/24/15363053/b212aac89bb6d20fe174035b9469da21_6112821780306629032.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/708/detail?bbs_presentation_style=no_header",
        "name": "旅行剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/25/15363053/ea426d267c69897cc818c5d5a9e386ea_4399217366335298544.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/709/detail?bbs_presentation_style=no_header",
        "name": "翡玉法球",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/25/15363053/5fc36e1db7461a5086df18b58f0dcb8a_9079456443193854168.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/724/detail?bbs_presentation_style=no_header",
        "name": "钺矛",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/06/21/75833613/2ef0c79a0d05d49f3c7c884520e70ef6_7423804349833045135.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/1076/detail?bbs_presentation_style=no_header",
        "name": "白铁大剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/09/17/75833613/f559f442e3ceeb5d0fe4c9e8916f6036_6793022524921054225.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/126/detail?bbs_presentation_style=no_header",
        "name": "银剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/8abcfb0e788eee0d872a8b5ab36b54c9_3740162289790477109.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/142/detail?bbs_presentation_style=no_header",
        "name": "口袋魔导书",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/877be88d4393febf2eebf0d0842991b1_5203967974566406481.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/143/detail?bbs_presentation_style=no_header",
        "name": "历练的猎弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/bda299007ed693390a7629dec62ad9c8_4027560520984292648.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/158/detail?bbs_presentation_style=no_header",
        "name": "佣兵重剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/478f9e83909a2bf2545d7f70d765b788_5488112487273325804.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/160/detail?bbs_presentation_style=no_header",
        "name": "铁尖枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/6189a5177288ec1a426710bfcb41885b_1406125984012296163.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/118/detail?bbs_presentation_style=no_header",
        "name": "新手长枪",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/20/75833613/b72786043e38c86cfca0605f587f83d5_7801496279198261696.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/123/detail?bbs_presentation_style=no_header",
        "name": "训练大剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/2fc6f5c0c4a8f0547ab17cd06e2d9a14_6235791695356383945.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/124/detail?bbs_presentation_style=no_header",
        "name": "学徒笔记",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/79bdee9646f7cd1f3e757d9f26bd3d68_8508785103108153146.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/125/detail?bbs_presentation_style=no_header",
        "name": "猎弓",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/bf332b2c47143efb3f9c99baf63e72b3_5155894237240012716.png?x-oss-process=image/quality,q_75/resize,s_120"
    },
    {
        "href": "https://bbs.mihoyo.com/ys/obc/content/127/detail?bbs_presentation_style=no_header",
        "name": "无锋剑",
        "pic": "https://uploadstatic.mihoyo.com/ys-obc/2020/03/19/75833613/fee1b4cdc14a3dce1f548a99967d0a4d_3322549636151970165.png?x-oss-process=image/quality,q_75/resize,s_120"
    }
]

"""
list=document.getElementsByClassName("collection-avatar")[1].children
a=[]
for(var i=0;i<list.length;i++){
    item=list[i]
    a[i]={"href":item.href,"name":item.innerText,"pic":item.children[0].dataset['src']}
}
console.log(a)
"""


def getWepaonValue(url):
    # data-data明摆着数据我没看见。。。
    a = requests.get(url)
    a.encoding = "utf-8"
    soup = BeautifulSoup(a.text, "lxml")
    wep_data = json.loads(unquote(str(soup.find_all("div", {"class": "obc-tmpl"})[0].get("data-data"))))
    start_ATK = int(wep_data[2]["data"]["data"][0]["basic"][0]["value"].replace("：", ": ").split(": ")[1])
    print(wep_data[2]["data"]["data"][0]["basic"][0]["value"])
    end_ATK = int(wep_data[2]["data"]["data"][-1]["basic"][0]["value"].replace("：", ": ").split(": ")[1])
    star = int(wep_data[0]["data"]["rate"])
    type_ = wep_data[0]["data"]["type"]
    D_value = end_ATK - start_ATK
    S_value = start_ATK
    return [D_value, S_value, star, type_]


class myThread(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self.data = data

    def run(self):
        for i in self.data:
            name = str(i["name"])
            pic = i["pic"]
            url = i["href"]
            path = "./data/resources/image/weapon/" + name + ".png"
            if not os.path.exists(path):
                with open(path, "wb") as image:
                    image.write(requests.get(pic).content)
                    image.close()
            with open("./data/resources/information/weapon/" + name + ".json", "w") as file:
                value = getWepaonValue(url)
                result = {"name": name, "pic": path, "D-value": value[0], "S-value": value[1], "star": value[2],
                          "type": value[3]}
                file.write(json.dumps(result))
                file.close()
            print(name + " 数据同步成功！")


if __name__ == '__main__':
    thread_num = 13
    prepare_data = [[] for i in range(thread_num)]
    task_num = int(len(data) / thread_num)
    index = 0
    prepare_data_index = 0
    for i in data:
        if (index + 1) % task_num == 0:
            prepare_data_index += 1
        if (prepare_data_index + 1) > thread_num:
            if index + 1 == len(data):
                prepare_data[0].append(data[-1])
                break
            else:
                a = 0
                while True:
                    if index + 1 == len(data):
                        break
                    index += 1
                    prepare_data[a].append(data[index])
                    a += 1
                prepare_data[0].append(data[-1])
                break
        prepare_data[prepare_data_index].append(i)
        index += 1
    for i in range(thread_num):
        thread = myThread(prepare_data[i])
        thread.start()
