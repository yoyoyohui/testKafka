#!/usr/bin/python
# -*- coding: GBK -*-
import json
import time
from sqlalchemy import false, true, null
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

msg_dict = {
    "cache_time": 1625053011,
    "code": 0,
    "data": {
        "activity_collection": {},
        "control": {},
        "destination_type": 2,
        "destination_url": "order_checkout.html",
        "goods": {
            "allowed_region": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32",
            "app_client_only": 0,
            "app_new": 0,
            "bottom_notice": {
                "notice": "",
                "notice_type": 0,
                "priority": 1
            },
            "brand_id": 357642,
            "carousel_rec": 1,
            "cat_id": 19271,
            "cat_id_1": 2933,
            "cat_id_2": 2946,
            "cat_id_3": 19268,
            "cat_id_4": 19271,
            "check_quantity": 1,
            "cost_province_codes": "5,9,19,20,21,28,29",
            "cost_template_id": 197766148002016,
            "country": "",
            "customer_num": 2,
            "decoration": [
                {
                    "contents": [
                        {
                            "height": 1409,
                            "img_url": "https://img.pddpic.com/mms-material-img/2020-12-12/9e136db8-d94e-408d-b793-62ba3749d4b8.jpeg.a.jpeg",
                            "width": 790
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1858762885,
                    "key": "DecImage",
                    "priority": 0,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 745,
                            "img_url": "https://img.pddpic.com/mms-material-img/2020-12-12/98ac4636-80d3-4e92-badc-deb69897d2d4.jpeg.a.jpeg",
                            "width": 802
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1858762886,
                    "key": "DecImage",
                    "priority": 1,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 430,
                            "img_url": "https://img.pddpic.com/mms-material-img/2020-12-12/34694d8c-6434-4543-8c7f-26e495d4ac7e.jpeg.a.jpeg",
                            "width": 781
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1858762887,
                    "key": "DecImage",
                    "priority": 2,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/a8e9f34a58b879ae1624fbe8a24654d0.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153151,
                    "key": "DecImage",
                    "priority": 3,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 579,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/6210342c5e2e428533256608482270c6.jpeg",
                            "width": 1200
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153152,
                    "key": "DecImage",
                    "priority": 4,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/ac949161d4a0c35e29ee36bded7e0aa1.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153153,
                    "key": "DecImage",
                    "priority": 5,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 661,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/b1de81c31c7e95cdf9e16baabb1eac57.jpeg",
                            "width": 1200
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153154,
                    "key": "DecImage",
                    "priority": 6,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/a0665836b4198f71af9eb64ad71dad02.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153155,
                    "key": "DecImage",
                    "priority": 7,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/f7e2debfa6fd176c4897de0affb48e8f.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153156,
                    "key": "DecImage",
                    "priority": 8,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/9b9af7c34a4395448cbaaec482e6e2e1.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153157,
                    "key": "DecImage",
                    "priority": 9,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/fe613429789cd6832916c187a2f7b256.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153158,
                    "key": "DecImage",
                    "priority": 10,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 502,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/bbcd15ad6832e5b5bda81b078137db8b.jpeg",
                            "width": 1199
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153159,
                    "key": "DecImage",
                    "priority": 11,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/3778a0ad0641f4aa33e50908245e9b57.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153160,
                    "key": "DecImage",
                    "priority": 12,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/f81d97041fddd580781e658be2f73414.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153161,
                    "key": "DecImage",
                    "priority": 13,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/0e8e4b3739eba86462b611d28ba4afb0.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153162,
                    "key": "DecImage",
                    "priority": 14,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/8c65e7a8931fb46e2a1f94a10f472d85.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153163,
                    "key": "DecImage",
                    "priority": 15,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/ccc9101ca8b1d0135d13154c0d21ad98.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153164,
                    "key": "DecImage",
                    "priority": 16,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 478,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/6e786e5ae64c40738bf2d16ddfc3fd74.jpeg",
                            "width": 1200
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153165,
                    "key": "DecImage",
                    "priority": 17,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/5b88355e381e69f3b42ec40a15ef15ae.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153166,
                    "key": "DecImage",
                    "priority": 18,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 470,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/f863668a695c6e75e1dc194ad61f3100.jpeg",
                            "width": 1199
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153167,
                    "key": "DecImage",
                    "priority": 19,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/ac9f4706d159e27dea962fc24122e5d5.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153168,
                    "key": "DecImage",
                    "priority": 20,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/ae36c3c149ee54bd545cbffc96cc2707.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153169,
                    "key": "DecImage",
                    "priority": 21,
                    "type": "image"
                },
                {
                    "contents": [
                        {
                            "height": 1500,
                            "img_url": "https://t16img.yangkeduo.com/garner-api/bcdcb97512bb4d28b49a3b56a01a0695.jpeg",
                            "width": 1172
                        }
                    ],
                    "enable_share": 1,
                    "floor_id": 1847153170,
                    "key": "DecImage",
                    "priority": 22,
                    "type": "image"
                }
            ],
            "default_province_id": 1,
            "event_type": 0,
            "gallery": [
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 960,
                    "id": 488193774364,
                    "priority": 33,
                    "type": 6,
                    "url": "https://video3.pddpic.com/i1/2020-12-21/42e7acc72347f106ae8f0e261d0d8dd9.mp4",
                    "width": 720
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 488193774363,
                    "priority": 32,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/bcdcb97512bb4d28b49a3b56a01a0695.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 488193774362,
                    "priority": 31,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/ae36c3c149ee54bd545cbffc96cc2707.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 488193774361,
                    "priority": 30,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/ac9f4706d159e27dea962fc24122e5d5.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 470,
                    "id": 488193774360,
                    "priority": 29,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/f863668a695c6e75e1dc194ad61f3100.jpeg",
                    "width": 1199
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 488193774359,
                    "priority": 28,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/5b88355e381e69f3b42ec40a15ef15ae.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 478,
                    "id": 488193774358,
                    "priority": 27,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/6e786e5ae64c40738bf2d16ddfc3fd74.jpeg",
                    "width": 1200
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 488193774357,
                    "priority": 26,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/ccc9101ca8b1d0135d13154c0d21ad98.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376081,
                    "priority": 25,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/8c65e7a8931fb46e2a1f94a10f472d85.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376080,
                    "priority": 24,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/0e8e4b3739eba86462b611d28ba4afb0.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376079,
                    "priority": 23,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/f81d97041fddd580781e658be2f73414.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376078,
                    "priority": 22,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/3778a0ad0641f4aa33e50908245e9b57.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 502,
                    "id": 487571376077,
                    "priority": 21,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/bbcd15ad6832e5b5bda81b078137db8b.jpeg",
                    "width": 1199
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376076,
                    "priority": 20,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/fe613429789cd6832916c187a2f7b256.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376075,
                    "priority": 19,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/9b9af7c34a4395448cbaaec482e6e2e1.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376074,
                    "priority": 18,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/f7e2debfa6fd176c4897de0affb48e8f.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376073,
                    "priority": 17,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/a0665836b4198f71af9eb64ad71dad02.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 661,
                    "id": 487571376072,
                    "priority": 16,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/b1de81c31c7e95cdf9e16baabb1eac57.jpeg",
                    "width": 1200
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376071,
                    "priority": 15,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/ac949161d4a0c35e29ee36bded7e0aa1.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 579,
                    "id": 487571376070,
                    "priority": 14,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/6210342c5e2e428533256608482270c6.jpeg",
                    "width": 1200
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376069,
                    "priority": 13,
                    "type": 2,
                    "url": "https://t16img.yangkeduo.com/garner-api/a8e9f34a58b879ae1624fbe8a24654d0.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 430,
                    "id": 487571376068,
                    "priority": 12,
                    "type": 2,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-12/34694d8c-6434-4543-8c7f-26e495d4ac7e.jpeg.a.jpeg",
                    "width": 781
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 745,
                    "id": 487571376067,
                    "priority": 11,
                    "type": 2,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-12/98ac4636-80d3-4e92-badc-deb69897d2d4.jpeg.a.jpeg",
                    "width": 802
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1409,
                    "id": 487571376066,
                    "priority": 10,
                    "type": 2,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-12/9e136db8-d94e-408d-b793-62ba3749d4b8.jpeg.a.jpeg",
                    "width": 790
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376065,
                    "priority": 9,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/ebbfd571-4abb-4c74-b653-8b13d281396f.jpeg.a.jpeg",
                    "width": 800
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1500,
                    "id": 487571376064,
                    "priority": 8,
                    "type": 1,
                    "url": "https://t16img.yangkeduo.com/garner-api/8b1e06e4bf80de249bff3c09718bbf88.jpeg",
                    "width": 1500
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 1172,
                    "id": 487571376063,
                    "priority": 7,
                    "type": 1,
                    "url": "https://t16img.yangkeduo.com/garner-api/8e7b864d948db01bdf1efedbf3275c40.jpeg",
                    "width": 1172
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376062,
                    "priority": 6,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/0f991c59-6ecc-4600-86ff-4230d2882a70.jpeg.a.jpeg",
                    "width": 800
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 790,
                    "id": 487571376061,
                    "priority": 5,
                    "type": 1,
                    "url": "https://t16img.yangkeduo.com/garner-api/e2912b07a30c67eb12f1139ffd2e1a5d.jpeg",
                    "width": 790
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 962,
                    "id": 487571376060,
                    "priority": 4,
                    "type": 1,
                    "url": "https://t16img.yangkeduo.com/garner-api/46b83df64598dd5d6eeaa8349be1f2d3.jpeg",
                    "width": 962
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376059,
                    "priority": 3,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/ce13ead0-af0e-4c5d-a332-39d0cb2e4bae.jpeg.a.jpeg",
                    "width": 800
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376058,
                    "priority": 2,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/6d5c7bdb-1772-4785-8076-abc5ef93f9aa.jpeg.a.jpeg",
                    "width": 800
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376057,
                    "priority": 1,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/f2e96659-5eca-408d-b961-9f1683a106f8.jpeg.a.jpeg",
                    "width": 800
                },
                {
                    "enable_share": 1,
                    "goods_id": 210668807838,
                    "height": 800,
                    "id": 487571376056,
                    "priority": 0,
                    "type": 1,
                    "url": "https://img.pddpic.com/mms-material-img/2020-12-21/d7139c42-6fca-4334-af73-90d51767b296.jpeg.a.jpeg",
                    "width": 800
                }
            ],
            "goods_id": 210668807838,
            "goods_name": "手机自拍杆全自动多功能三脚架苹果安卓通用360度拍照直播支架",
            "goods_property": [
                {
                    "key": "品牌",
                    "ref_pid": 310,
                    "reference_id": 357642,
                    "values": [
                        "施索"
                    ]
                },
                {
                    "key": "杆身材质",
                    "ref_pid": 1845,
                    "reference_id": 0,
                    "values": [
                        "铝合金"
                    ]
                },
                {
                    "key": "控制方式",
                    "ref_pid": 474,
                    "reference_id": 0,
                    "values": [
                        "蓝牙遥控"
                    ]
                }
            ],
            "goods_property_type": 0,
            "goods_type": 1,
            "gpv": 2,
            "group": [
                {
                    "buy_limit": 999999,
                    "customer_num": 1,
                    "duration": 86400,
                    "end_time": 2082729600,
                    "goods_id": 210668807838,
                    "group_id": 47303167800,
                    "id": 47303167800,
                    "is_open": 1,
                    "order_limit": 999999,
                    "price": 0,
                    "regular_limit": 0,
                    "regular_limit_duration": 0,
                    "start_time": 1451577600
                },
                {
                    "buy_limit": 999999,
                    "customer_num": 2,
                    "duration": 86400,
                    "end_time": 2082729600,
                    "goods_id": 210668807838,
                    "group_id": 47303167801,
                    "id": 47303167801,
                    "is_open": 1,
                    "order_limit": 999999,
                    "price": 0,
                    "regular_limit": 0,
                    "regular_limit_duration": 0,
                    "start_time": 1451577600
                }
            ],
            "has_activity": 1,
            "has_cost": 0,
            "has_promotion": 1,
            "hd_thumb_url": "http://t00img.yangkeduo.com/goods/images/2020-12-21/e335700a91af5519bff0300d6a4b8b9d.jpeg",
            "image_url": "http://t00img.yangkeduo.com/goods/images/2020-12-21/ba0f1d1d7c35038806b382f687534fe6.jpeg",
            "images": [],
            "is_app": 0,
            "is_app_flow": 1,
            "is_cold_goods": 0,
            "is_hidden": 0,
            "is_mall_dsr": 1,
            "is_mall_rec": 1,
            "is_onsale": 1,
            "is_pre_sale": 0,
            "is_sku_onsale": 1,
            "mall_id": 999151840,
            "market_price": 19900,
            "new_options": [
                70,
                54,
                7,
                9,
                13,
                31
            ],
            "off_sale_type": -1,
            "open_in_festival": 0,
            "options": [
                54,
                7,
                9,
                13,
                31
            ],
            "oversea_type": 0,
            "pre_sale_time": 0,
            "preview_share_link": "mall_quality_assurance.html?_t_timestamp=comm_share_landing&goods_id=210668807838",
            "property_card_click": 0,
            "quantity": 1000,
            "rv": 1,
            "rv_image": 1,
            "second_hand": 0,
            "select_sku_id": 773906701948,
            "service_promise_version": 0,
            "share_desc": "【退货包运费】手机自拍杆全自动多功能三脚架苹果安卓通用360度拍照直播支架",
            "share_link": "goods2.html?goods_id=210668807838&page_from=23&pxq_secret_key=PCKIQ3SV52U2SJSN4JIC6JQ4RP2VZIKH6ONJLSYOQLRB5ZMTOW3A",
            "share_title": "77.9元 手机自拍杆全自动多功能三脚架苹果安卓通用360度拍照直播支架 拼多多",
            "shipment_limit_second": 86400,
            "short_name": "手机自拍杆全自动多功能三脚架苹果安卓通用360度拍照直播支架",
            "show_history_group": 1,
            "show_rec": 1,
            "show_rec_title": 1,
            "side_sale_tip_amount": 100000,
            "side_sales_tip": "已拼10万+件",
            "skip_goods": "0",
            "sku_type": 0,
            "sold_quantity": 100000,
            "spu_id": 0,
            "status": 1,
            "tag": 10,
            "tag_icon": [
                {
                    "height": 51,
                    "id": 10,
                    "url": "https://funimg.pddpic.com/2020-12-02/640fd63d-132e-49df-8b84-84b159c5521d.png.slim.png",
                    "width": 144
                }
            ],
            "thumb_url": "http://t00img.yangkeduo.com/goods/images/2020-12-21/ba0f1d1d7c35038806b382f687534fe6.jpeg",
            "vas_template_id": {},
            "warehouse": "",
            "we_chat_only": 0
        },
        "mall_entrance": {
            "mall_data": {
                "dsr": {
                    "desc_rank_percent": 75,
                    "desc_rank_status": 1,
                    "desc_score": 4.68,
                    "desc_status": 1,
                    "hide_rank_info": 0,
                    "is_show_mall_star": true,
                    "logistics_rank_percent": 75,
                    "logistics_rank_status": 1,
                    "logistics_score": 4.68,
                    "logistics_status": 1,
                    "mall_rating_text_list": [
                        {
                            "mall_rating_key": {
                                "color": "#58595B",
                                "font": 13,
                                "txt": "描述相符"
                            },
                            "mall_rating_value": {
                                "back_color": "#FCE5E5",
                                "color": "#E02E24",
                                "font": 11,
                                "txt": "高"
                            }
                        },
                        {
                            "mall_rating_key": {
                                "color": "#58595B",
                                "font": 13,
                                "txt": "物流服务"
                            },
                            "mall_rating_value": {
                                "back_color": "#FCE5E5",
                                "color": "#E02E24",
                                "font": 11,
                                "txt": "高"
                            }
                        },
                        {
                            "mall_rating_key": {
                                "color": "#58595B",
                                "font": 13,
                                "txt": "服务态度"
                            },
                            "mall_rating_value": {
                                "back_color": "#FCE5E5",
                                "color": "#E02E24",
                                "font": 11,
                                "txt": "高"
                            }
                        }
                    ],
                    "mall_star": 5,
                    "service_rank_percent": 75,
                    "service_rank_status": 1,
                    "service_score": 4.68,
                    "service_status": 1
                },
                "extras": {
                    "2": false,
                    "3": true,
                    "5": 1
                },
                "goods_num": 15,
                "goods_num_desc": "商品数量: 15",
                "is_flag_ship": true,
                "is_guide_mall": false,
                "logo_list": [
                    {
                        "logo_height": 48,
                        "logo_type": 1,
                        "logo_url": "http://t00img.yangkeduo.com/goods/images/2018-12-29/90e6990661ea5c56ac6613bfabc76795.png",
                        "logo_width": 90
                    }
                ],
                "mall_id": "999151840",
                "mall_logo": "http://t16img.yangkeduo.com/pdd_ims/img_check/v2/2D6EE4FFFFFF0320200112174741261/8a79b87f0ace4870b6434371f55ac3b1.png",
                "mall_logo_list": [
                    {
                        "logo_height": 48,
                        "logo_type": 1,
                        "logo_url": "http://t00img.yangkeduo.com/goods/images/2018-12-29/90e6990661ea5c56ac6613bfabc76795.png",
                        "logo_width": 90
                    },
                    {
                        "logo_height": 48,
                        "logo_type": 3,
                        "logo_url": "https://t16img.yangkeduo.com/mms_static/2019-12-04/ea0eaa26-203d-487b-9d7e-9c920c0b8d51.gif",
                        "logo_width": 174
                    }
                ],
                "mall_name": "施索数码电器官方旗舰店",
                "mall_page_head_show_tag_volist": [],
                "mall_service_tag": "客服",
                "mall_show_type": 0,
                "mall_transfer_type": 0,
                "merchant_type": 3,
                "msn": "4e3a4njygwpunk3jzex7awe2wa_axbuy",
                "pdd_route": "mall_page.html?mall_id=999151840&msn=4e3a4njygwpunk3jzex7awe2wa_axbuy&mall_info=%7B%22mall_name%22%3A%22%E6%96%BD%E7%B4%A2%E6%95%B0%E7%A0%81%E7%94%B5%E5%99%A8%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%22%7D&has_decoration=1",
                "pdd_route_name": "进店逛逛",
                "sales_tip": "已拼: 10万+件"
            }
        },
        "neighbor_group": {
            "neighbor_data": {
                "combine_group": {
                    "combine_group_button_desc": "去拼单",
                    "combine_group_desc": "这些人刚刚拼单成功，可参与拼单",
                    "combine_group_list": [
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1536364191447850468",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/44531751e975803888acfeabe789fd188dae07a4-1569733366?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "有你真好",
                                    "uin": "KXFYBVDPHAASAZT3MFZTKHAK3E_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1534618743788281941",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q004NWEwbmVmWGpONDJKeHdNWHFRZ0ZRSzJXaDQxQnYyZz09djA0-1621844103?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "こ浅沫记忆ζ",
                                    "uin": "5KPH5Q4IOFGO53UOBCL6ZN5H6Q_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1536064838707993996",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0dZRk9TM1owZWgyMzRCTTZiUjNWUFc0NFFlM1hzTGdHdz09djA0-1572269676?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "乾豪装饰万建华",
                                    "uin": "MWX4R5NBVSE4752ZETONIG7ANA_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1532016090409662837",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q1BzMWdaUDNZaFBXSXk2aVZodFQrK3lLYm5PRlZZTjluZz09djA0-1621334452?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "阳光老奶",
                                    "uin": "FDTDAGMFFJTZ4TFD7WURA6HLBM_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1526618652048260128",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0lDL280ckpFakxxb0ZsV3NUQ1Y5VXdvYzNydWlYdjRVQT09djA0-1607328393?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "春华秋月",
                                    "uin": "NAEHXCGJNM2N6SEMARK2CPTQPI_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0Zta0hMU09VRldtdXdicWFleDF5amhFQXdjWDIwVjlidz09djA0-1595142143?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "张明霞",
                                    "uin": "WYMUL2TUZ6SEMGQOR6EXBCLI4Y_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0VGL3g3eWJRbVBNNTcwb2dwR1hsejVZOHQxQzNINFovdz09djA0-1623685968?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "[表情]",
                                    "uin": "2YM246G6WWNWCZB3C7AS2COGJE_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0hUdzdyT0F6R25CS1V1dE9JcytUZ1dkOEh0dG9rdkJDQT09djA0-1624103596?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "追梦",
                                    "uin": "FWUDUFGIVR7DYREA22J7A4XJ64_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1524015356406673282",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0EwQUVVaEJQem9sdEdFdmt0dnhFenRhdDB0ZElrWmRRZz09djA0-1528777084?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "李长海",
                                    "uin": "PPXZAPE5J6GRIFQK3HBFWVZCO4_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0ZUVWl6akRYU3VLMTErN2FGemVFaEVJNHVGSFh5UW4zdz09djA0-1603983207?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "霜漫月",
                                    "uin": "YVLUIWR6ZRWUXD5H4IGYNFMRHA_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1526636454185850695",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0VKLzNnUG1mNkJxTGhBTGNNeEhRWVZaeVkyeVpxcENadz09djA0-1567726092?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "金燕子",
                                    "uin": "6F2CPZORRWCUGJTHOGPENTY4SQ_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0VpQ1lHWTF3UDN0R0dWOFJkaTJ6TUZmT0RlWDk2WXZrUT09djA0-1624090420?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "英子",
                                    "uin": "7A5HHRUCHIRKCMLJSVMDEPYCGU_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1530515259792150549",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0V3R09mZWdxZ0JMNVBjMTlGeXFFd2oyblVramQ2b2syZz09djA0-1591269134?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "墨屿",
                                    "uin": "FAYTRVTCUQ3PRPRUI34RCI7WR4_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0c3THJ1bWVWSGQyb1Z5MjFJeDFvZDg5OFh6aUJCUVNWQT09djA0-1623665184?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "微笑闪亮未来",
                                    "uin": "MG4LGBD6V5NEQZOZV266S3HGHM_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1531372268073783763",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0U3bkFvMWRmM3gvd3pnc2RwL2dFVk1vcmdBWlBBODgzQT09djA0-1583472640?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "道道",
                                    "uin": "S3AQB5S27H6T5QIQPNNNKLDXIE_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0d5MWlGa2JLY0RJQWtuL3YwMko2NmtEVVlKRk1aWFJCUT09djA0-1617887117?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "168",
                                    "uin": "C3BZV2HUWLABS2CZ3OZFKD3UCU_GEXDA"
                                }
                            ]
                        },
                        {
                            "button_desc": "去拼单",
                            "group_order_id": "1533153338522251950",
                            "group_type": 1,
                            "is_self_group": false,
                            "member_info_list": [
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0VsZktlQ1VCTWRncG1IM0tHaVZkTjQxVTU0UGZ5Tit6dz09djA0-1623065326?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "、叮当猪 ??",
                                    "uin": "TZU6SO4UWVDL7FT6MM2KSFEXKA_GEXDA"
                                },
                                {
                                    "avatar": "https://avatar2.pddpic.com/a/Q0hEbjBrdjVPQXRtT29sOUo5d3IvN1JoY1UzbGs1ajVhUT09djA0-1573710061?imageMogr2/thumbnail/100x",
                                    "is_friend": false,
                                    "nickname": "tao 涛  tao",
                                    "uin": "PBT32EGOS2OAKMIUAUBUROGCMY_GEXDA"
                                }
                            ]
                        }
                    ],
                    "combine_group_popup_footer": "仅显示10个可参与的拼单",
                    "combine_group_popup_title": "可参与的拼单",
                    "group_total": 10,
                    "recommend_group": {
                        "button_desc": "去拼单",
                        "group_order_id": "1536364191447850468",
                        "group_type": 1,
                        "is_self_group": false,
                        "member_info_list": [
                            {
                                "avatar": "https://avatar2.pddpic.com/a/44531751e975803888acfeabe789fd188dae07a4-1569733366?imageMogr2/thumbnail/100x",
                                "is_friend": false,
                                "nickname": "有你真好",
                                "uin": "KXFYBVDPHAASAZT3MFZTKHAK3E_GEXDA"
                            }
                        ]
                    },
                    "user_combine_group_button_desc": ""
                }
            },
            "neighbor_status": 1
        },
        "pre_render_url": "csr/comm_mall_home_pre_render.html",
        "price": {
            "browser_price_style": 0,
            "line_price": 19900,
            "max_group_price": 7790,
            "max_normal_price": 8000,
            "max_on_sale_group_price": 7790,
            "max_on_sale_normal_price": 8000,
            "min_group_price": 7790,
            "min_normal_price": 8000,
            "min_on_sale_group_price": 7790,
            "min_on_sale_normal_price": 8000,
            "old_max_group_price": 7790,
            "old_max_on_sale_group_price": 7790,
            "old_min_group_price": 7790,
            "old_min_on_sale_group_price": 7790,
            "price_style": 0,
            "unselect_normal_save_price": 210
        },
        "promotion": {
            "events": {
                "promotion_price_info": {
                    "contains_treasure_coupon": false,
                    "copy_writing": {
                        "activity_copy_writing": "",
                        "copy_writing_without_price_start_from": "",
                        "sku_copy_writings": []
                    },
                    "fb_send_amount": 0,
                    "promo_display_items": [],
                    "promo_display_items_with_suffix": []
                },
                "promotion_yellow_label": null
            },
            "promotion_events": {}
        },
        "review": {
            "review_data": {
                "exps": {
                    "goods_detail": {
                        "bucket": 6,
                        "strategy_name": "V3.17.5",
                        "timestamp": 1625053010807
                    },
                    "goods_detail_perfect_pic": {
                        "bucket": 8,
                        "strategy_name": "V2.8",
                        "timestamp": 1625053010803
                    },
                    "label_info": {
                        "bucket": 5,
                        "strategy_name": "V3.16.6",
                        "timestamp": 1625053010807
                    }
                },
                "labels": [
                    {
                        "id": "2f2f443f3861b67ed69168d434775962",
                        "label_merge_outer_count": 3,
                        "name": "正品",
                        "num": 3,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "正品(3)",
                        "view": {
                            "back_color": "#DAF8CD",
                            "click_back_color": "#C2E6B2",
                            "click_text_color": "#2C6813",
                            "iconfont": 59421,
                            "label_type": 1,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#25B513"
                        }
                    },
                    {
                        "id": "ef7bc5da221112376d9961c198834f9f",
                        "label_merge_outer_count": 30,
                        "name": "质量很好",
                        "num": 30,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "质量很好(30)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "956f2804a0b0cd33c63522a36b88b9bb",
                        "label_merge_outer_count": 28,
                        "name": "很漂亮",
                        "num": 28,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "很漂亮(28)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "74f3cfe3c661f485eb953afb0ba8eb8e",
                        "label_merge_outer_count": 19,
                        "name": "实用",
                        "num": 19,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "实用(19)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "e6af86c791888abbc3cd7b7ad1cdba32",
                        "label_merge_outer_count": 18,
                        "name": "方便",
                        "num": 18,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "方便(18)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "0ad8c17dc30f2e42283d0fa81163d64c",
                        "label_merge_outer_count": 12,
                        "name": "物流很快",
                        "num": 12,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "物流很快(12)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "ed0dd179e0b520093f70e6be4a0749f6",
                        "label_merge_outer_count": 10,
                        "name": "物美价廉",
                        "num": 10,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "物美价廉(10)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "fdf56c6da5046de3a1d0f9d284aaf02b",
                        "label_merge_outer_count": 10,
                        "name": "服务态度很好",
                        "num": 10,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "服务态度很好(10)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    },
                    {
                        "id": "67c89882456a289b75d5d8dc51c60d21",
                        "label_merge_outer_count": 6,
                        "name": "手感很好",
                        "num": 6,
                        "outer_positive_count": 0,
                        "positive": 1,
                        "text": "手感很好(6)",
                        "view": {
                            "back_color": "#FDEFEE",
                            "click_back_color": "#F7D7D5",
                            "click_text_color": "#7C7372",
                            "label_type": 0,
                            "select_back_color": "#E02E24",
                            "select_text_color": "#FFFFFF",
                            "text_color": "#58595B"
                        }
                    }
                ],
                "mall_review_entrance_info": {
                    "exps": {
                        "mall_functional_label": {
                            "bucket": 2,
                            "strategy_name": "V3.3.4",
                            "timestamp": 1625053010803
                        }
                    },
                    "label_list": [
                        {
                            "cluster_id": 0,
                            "id": "ef7bc5da221112376d9961c198834f9f",
                            "name": "质量很好",
                            "num": 495,
                            "positive": 1,
                            "text": "质量很好(495)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 22,
                            "id": "29558f23481b8b082df282157e9a055e",
                            "name": "好用",
                            "num": 246,
                            "positive": 1,
                            "text": "好用(246)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 4,
                            "id": "c056d33ed628cbb968c38fc16ae94081",
                            "name": "价格很实惠",
                            "num": 235,
                            "positive": 1,
                            "text": "价格很实惠(235)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 6,
                            "id": "5d34117946dd16c14e6b5519ffb2fe83",
                            "name": "外观好看",
                            "num": 177,
                            "positive": 1,
                            "text": "外观好看(177)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 8,
                            "id": "0a8ae14057a6a82b64ce3fd89650256b",
                            "name": "客服态度很好",
                            "num": 103,
                            "positive": 1,
                            "text": "客服态度很好(103)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 1736,
                            "id": "e9f2782f92aa4289b94791519bd19ac6",
                            "name": "自拍杆太好",
                            "num": 74,
                            "positive": 1,
                            "text": "自拍杆太好(74)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 276,
                            "id": "09d237b5a64d7fe6837bc0cf12e80294",
                            "name": "功能强大",
                            "num": 72,
                            "positive": 1,
                            "text": "功能强大(72)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 18,
                            "id": "4649892d1418d26d44666670e325db03",
                            "name": "补光效果不错",
                            "num": 70,
                            "positive": 1,
                            "text": "补光效果不错(70)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 68,
                            "id": "fab1ce04503da7f3b642b61549e9f041",
                            "name": "性价比高",
                            "num": 57,
                            "positive": 1,
                            "text": "性价比高(57)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 174,
                            "id": "67ef5dc235561e4ad0e3f18d40598599",
                            "name": "使用很方便",
                            "num": 52,
                            "positive": 1,
                            "text": "使用很方便(52)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 48,
                            "id": "3eb1f317c1143856b5c7d9a6a97674c4",
                            "name": "手感非常好",
                            "num": 45,
                            "positive": 1,
                            "text": "手感非常好(45)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        },
                        {
                            "cluster_id": 746,
                            "id": "c148749b2a2422ee9d1f7dfcbdadc8f1",
                            "name": "反应灵敏",
                            "num": 43,
                            "positive": 1,
                            "text": "反应灵敏(43)",
                            "view": {
                                "back_color": "#FDEFEE",
                                "click_back_color": "#F7D7D5",
                                "click_text_color": "#7C7372",
                                "label_type": 0,
                                "select_back_color": "#E02E24",
                                "select_text_color": "#FFFFFF",
                                "text_color": "#58595B"
                            }
                        }
                    ],
                    "title_text": "该商品所属店铺评价"
                },
                "merchant_qa_list": [
                    {
                        "avatar": "https://avatar2.pddpic.com/a/Q0lCR1ppVnNFcFBSOXRXb01MajVrWGlydVVGOVVJNTJDUT09djA0-1607869919?imageMogr2/thumbnail/10x/blur/50x50",
                        "cat_cnt_text": "664人同问",
                        "question": "发什么快递？",
                        "version": "N"
                    },
                    {
                        "avatar": "https://avatar2.pddpic.com/a/Q0N6eUk3a0I5bFlxalJlR0NxU0hMRzN6WkYyVFNnM1VYZz09djA0-1618461211?imageMogr2/thumbnail/10x/blur/50x50",
                        "cat_cnt_text": "3人同问",
                        "question": "这个三角架最长是多少厘米啊？",
                        "version": "N"
                    }
                ],
                "merchant_qa_list_lego_url": "lego_goods_detail_coupon_price_popup_goods_detail_qa_list_popup.html?lego_type=v8&lego_minversion=5.39.0&lego_ssr_api=/api/goods_detail_coupon_price_popup/get_config/goods_detail_qa_list_popup&goods_id=210668807838&mall_id=${mallId}&oc_trace_mark=&oc_trace_mark_extra=",
                "merchant_qa_list_url": "comm_goods_qa.html?goods_id=210668807838&mall_id=999151840&oc_trace_mark=&oc_trace_mark_extra=",
                "merchant_qa_num_text": "商品答疑(4)",
                "merchant_qa_title_text": "商品答疑",
                "merge_review_with_outer_review": 1,
                "new_merchant_qa_pattern_gray": false,
                "new_outer_review_gray": true,
                "outer_positive_review_num_text": "",
                "pgc_info_list": [
                    {
                        "avatar": "https://avatar2.pddpic.com/a/Q0s3ZXNSbzdYcytSVjd3WVBJeDNZK01iYWczZEQvRHlCUT09djA0-1531476964?imageMogr2/thumbnail/100x",
                        "content": "用过才来评价，外观好看，方便，实用，质量很好，物流很快，正品，手感很好，会推荐朋友购买，服务态度很好！",
                        "detail_url": "comm_goods_experience.html?goods_id=210668807838&pgc_id=114306913591728&channel=0",
                        "expert_icon_url": "https://pinduoduoimg.yangkeduo.com/transaction_process/2020-04-09/4bbac4c0-9ceb-44c6-a3ac-00215028d850.png",
                        "expert_status": 3,
                        "favor_count": 0,
                        "favor_list": [],
                        "hit_mall_interact_gray": false,
                        "id": "114306913591728",
                        "is_favor_from_pxq": 0,
                        "is_favored": false,
                        "nick_name": "中国人寿费继江",
                        "pgc_detail_title_text": "行家心得",
                        "pgc_module_text": "行家心得(3)",
                        "picture_list": [
                            {
                                "height": 1236,
                                "type": 0,
                                "url": "https://review.pddpic.com/review3/review/2021-05-27/363dc9f2-4dfc-49ad-a431-7b0dd329fc9c.jpeg",
                                "width": 1236
                            },
                            {
                                "height": 1080,
                                "type": 0,
                                "url": "https://review.pddpic.com/review3/review/2021-05-27/24b3a3ed-1504-4c2b-b922-9313630ac095.jpeg",
                                "width": 1080
                            },
                            {
                                "height": 1236,
                                "type": 0,
                                "url": "https://review.pddpic.com/review3/review/2021-05-27/e352f4f2-796d-4660-80aa-f7d22584faa8.jpeg",
                                "width": 1236
                            },
                            {
                                "height": 1080,
                                "type": 0,
                                "url": "https://review.pddpic.com/review3/review/2021-05-27/a204cd36-e246-4ff5-aabb-b89137c53852.jpeg",
                                "width": 1080
                            }
                        ],
                        "review_id": "357623013975975582",
                        "show_expert_info": true,
                        "show_pgc_detail_text": "查看全部",
                        "title": "行家",
                        "video_list": []
                    }
                ],
                "review_info_list": [
                    {
                        "anonymous": 0,
                        "avatar": "https://avatar2.pddpic.com/a/Q0c2WG5vamZobGdUMnRoV051N2dzenZPVVQxVXMxWnJ2Zz09djA0-1599792237?imageMogr2/thumbnail/100x",
                        "comment": "做工质量非常好，款式设计上超有科技感，视频拍出来感觉特别好，很平稳，防抖效果不错，一体的收纳方便，携带出去也很方便，三脚架固定的很稳，有个小遥控器，连接蓝牙就可以控制手机拍照",
                        "is_my_review": false,
                        "name": "花落十年",
                        "order_num_text": "",
                        "pxq_friend_tag": false,
                        "review_id": 331481387093452400,
                        "specs": "[{\"spec_key\":\"颜色\",\"spec_value\":\"热情红+可充电遥控+稳固三脚架\"}]",
                        "time": 1609640242
                    },
                    {
                        "anonymous": 0,
                        "avatar": "https://avatar2.pddpic.com/a/Q0Y2amNIYm4vTHBkLzJ4QTk0Mnp1QTNDNTNuWWN0Y0c1dz09djA0-1617621130?imageMogr2/thumbnail/100x",
                        "comment": "这个自拍杆太棒了！[点赞][点赞][点赞]结实耐用美观大方！遥控器可以充电，真是一分钱，一分货啊！物有所值！点赞！老板服务态度好，物流很快。",
                        "is_my_review": false,
                        "name": "东北风",
                        "order_num_text": "",
                        "pxq_friend_tag": false,
                        "review_id": 353213314801002100,
                        "specs": "[{\"spec_key\":\"颜色\",\"spec_value\":\"热情红+可充电遥控+稳固三脚架\"}]",
                        "time": 1620002833
                    }
                ],
                "review_merge_outer_num": 0,
                "review_merge_outer_num_text": "",
                "review_num": 200,
                "review_num_text": "商品评价(200)"
            }
        },
        "section_list": [
            {
                "section_id": "sku_preview_section"
            },
            {
                "section_id": "price_section"
            },
            {
                "section_id": "info_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "group_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "comment_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "pgc_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "mall_comment_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "mall_qa_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "mall_info_section"
            },
            {
                "section_id": "mall_goods_rec_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "goods_rec_list_section"
            },
            {
                "section_id": "space_section"
            },
            {
                "section_id": "goods_property_section"
            },
            {
                "section_id": "video_section"
            },
            {
                "section_id": "illustration_section"
            },
            {
                "section_id": "decoration_section"
            },
            {
                "section_id": "usage_price_desc_section"
            }
        ],
        "server_time": 1625053010,
        "service_promise": [
            {
                "desc": "订单发货后90天内如果申请退货退款或换货，拼多多将补贴退货运费",
                "detail_hidden": 0,
                "dialog_type": "退货包运费",
                "id": 3,
                "navigation": 0,
                "navigation_url": "",
                "show_tip": "收货后如不满意，可以免费退货",
                "top": 1,
                "top_type": 1,
                "type": "退货包运费",
                "type_color": "#58595B"
            },
            {
                "desc": "若未在24小时内发货，消费者将会收到至少3元无门槛代金券",
                "detail_hidden": 0,
                "dialog_type": "24小时发货",
                "id": 43,
                "navigation": 0,
                "navigation_url": "",
                "top": 0,
                "top_type": 0,
                "type": "24小时发货",
                "type_color": "#58595B"
            },
            {
                "desc": "所有商品包邮（偏远地区除外）",
                "detail_hidden": 0,
                "dialog_type": "全场包邮",
                "id": 1,
                "navigation": 0,
                "navigation_url": "",
                "top": 0,
                "top_type": 0,
                "type": "全场包邮",
                "type_color": "#58595B"
            },
            {
                "desc": "满足相应条件时，消费者可申请“7天无理由退货”",
                "detail_hidden": 0,
                "dialog_type": "7天无理由退货",
                "id": 2,
                "navigation": 0,
                "navigation_url": "",
                "top": 0,
                "top_type": 0,
                "type": "7天无理由退货",
                "type_color": "#58595B"
            },
            {
                "desc": "若收到商品是假冒品牌，可获得十倍现金券赔偿",
                "detail_hidden": 0,
                "dialog_type": "假一赔十",
                "id": 15,
                "navigation": 0,
                "navigation_url": "",
                "top": 0,
                "top_type": 0,
                "type": "假一赔十",
                "type_color": "#58595B"
            },
            {
                "desc": "拼单成功6小时内，待发货状态下，提交退款申请将立即退款",
                "detail_hidden": 0,
                "dialog_type": "极速退款",
                "id": 24,
                "navigation": 0,
                "navigation_url": "",
                "top": 0,
                "top_type": 0,
                "type": "极速退款",
                "type_color": "#58595B"
            }
        ],
        "sku": [
            {
                "attribute": "{\"mg\":null,\"lampInstallInfo\":null,\"ticketRuleId\":null,\"tenBillionSpikeGlobalLowPrice\":null,\"vegetableRuleId\":null,\"skuPreSaleTime\":null,\"hotLiveGroup\":null,\"vegetableHasAllowance\":null,\"vegetableSupplierPrice\":null,\"vegetableStorePercent\":null,\"vegetableIsZeroGoods\":null,\"vegetableSkuGroup\":null,\"vegetableRegularLimitNumber\":null,\"vegetableArchived\":null,\"vegetableSkuOptions\":null}",
                "default_quantity": 100,
                "end_time": 0,
                "goods_id": 210668807838,
                "group_price": 7790,
                "init_quantity": 0,
                "is_onsale": 1,
                "limit_quantity": 999999,
                "market_price": 0,
                "normal_price": 8000,
                "normal_save_price": 210,
                "old_group_price": 7790,
                "preview_priority": 0,
                "price": 0,
                "quantity": 1000,
                "sku_id": 773906701948,
                "sold_quantity": 0,
                "spec": "5777153851",
                "specs": [
                    {
                        "spec_key": "颜色",
                        "spec_key_id": 27205,
                        "spec_value": "热情红+可充电遥控+稳固三脚架",
                        "spec_value_id": 5777153851
                    }
                ],
                "start_time": 0,
                "static_limit_quantity": 999999,
                "thumb_url": "https://img.pddpic.com/mms-material-img/2020-12-21/0f991c59-6ecc-4600-86ff-4230d2882a70.jpeg.a.jpeg",
                "weight": 0
            },
            {
                "attribute": "{\"mg\":null,\"lampInstallInfo\":null,\"ticketRuleId\":null,\"tenBillionSpikeGlobalLowPrice\":null,\"vegetableRuleId\":null,\"skuPreSaleTime\":null,\"hotLiveGroup\":null,\"vegetableHasAllowance\":null,\"vegetableSupplierPrice\":null,\"vegetableStorePercent\":null,\"vegetableIsZeroGoods\":null,\"vegetableSkuGroup\":null,\"vegetableRegularLimitNumber\":null,\"vegetableArchived\":null,\"vegetableSkuOptions\":null}",
                "default_quantity": 100,
                "end_time": 0,
                "goods_id": 210668807838,
                "group_price": 7790,
                "init_quantity": 0,
                "is_onsale": 1,
                "limit_quantity": 999999,
                "market_price": 0,
                "normal_price": 8000,
                "normal_save_price": 210,
                "old_group_price": 7790,
                "preview_priority": 1,
                "price": 0,
                "quantity": 1000,
                "sku_id": 773906701949,
                "sold_quantity": 0,
                "spec": "5777187057",
                "specs": [
                    {
                        "spec_key": "颜色",
                        "spec_key_id": 27205,
                        "spec_value": "象牙白+可充电遥控+稳固三脚架",
                        "spec_value_id": 5777187057
                    }
                ],
                "start_time": 0,
                "static_limit_quantity": 999999,
                "thumb_url": "https://img.pddpic.com/mms-material-img/2020-12-21/11da23ae-9dce-4eb9-a452-848c9ef8bd65.jpeg.a.jpeg",
                "weight": 0
            },
            {
                "attribute": "{\"mg\":null,\"lampInstallInfo\":null,\"ticketRuleId\":null,\"tenBillionSpikeGlobalLowPrice\":null,\"vegetableRuleId\":null,\"skuPreSaleTime\":null,\"hotLiveGroup\":null,\"vegetableHasAllowance\":null,\"vegetableSupplierPrice\":null,\"vegetableStorePercent\":null,\"vegetableIsZeroGoods\":null,\"vegetableSkuGroup\":null,\"vegetableRegularLimitNumber\":null,\"vegetableArchived\":null,\"vegetableSkuOptions\":null}",
                "default_quantity": 100,
                "end_time": 0,
                "goods_id": 210668807838,
                "group_price": 7790,
                "hot_sale": 1,
                "init_quantity": 0,
                "is_onsale": 1,
                "limit_quantity": 999999,
                "market_price": 0,
                "normal_price": 8000,
                "normal_save_price": 210,
                "old_group_price": 7790,
                "preview_priority": 2,
                "price": 0,
                "quantity": 1000,
                "sku_id": 773906701950,
                "sold_quantity": 0,
                "spec": "5777154900",
                "specs": [
                    {
                        "spec_key": "颜色",
                        "spec_key_id": 27205,
                        "spec_value": "女神粉+可充电遥控+稳固三脚架",
                        "spec_value_id": 5777154900
                    }
                ],
                "start_time": 0,
                "static_limit_quantity": 999999,
                "thumb_url": "https://img.pddpic.com/mms-material-img/2020-12-21/900b85e7-5e9e-4112-b79c-35f7cd56d3a9.jpeg.a.jpeg",
                "weight": 0
            }
        ],
        "ui": {
            "bottom_buying_section": {
                "type": "normal"
            },
            "bubble_section": {
                "show_bubble": 1
            },
            "live_section": {
                "float_from_type": 1,
                "float_info": {
                    "if_goods_show": "false",
                    "show_info": "{\"nonReturnEnum\":null,\"liveExpIdList\":null,\"show_id\":\"20210622_88106923_02\",\"status\":1,\"play_url_list\":[{\"play_url\":\"http://liveplay04.pddpic.com/live/17283_production_sprite_20210622_88106923_02.flv?txSecret=abd3df505cff53c3343f95385a38b76e&txTime=60dd7092&pub_type=bd-pddobs\",\"resolution\":\"default\",\"video_format\":0,\"width\":540,\"height\":960,\"play_in_info\":true}],\"h265_url_list\":[],\"if_h265\":false,\"if_soft_h265\":false,\"low_latency\":false,\"rtc_play\":false,\"h264_rtc_list\":[],\"h265_rtc_list\":[],\"room_id\":\"88106923\",\"image\":\"https://video-snapshot.pddpic.com/kiwi-live-image/202d8b6dcf737ea596ca45f3eecb2c78.jpeg\",\"link_url\":\"live_room.html?ext=%7B%22feed_scene_id%22%3A320%7D&room_id=88106923&play_url=http%3A%2F%2Fliveplay04.pddpic.com%2Flive%2F17283_production_sprite_20210622_88106923_02.flv%3FtxSecret%3Dabd3df505cff53c3343f95385a38b76e%26txTime%3D60dd7092%26pub_type%3Dbd-pddobs&biz_type=0&scene_id=50&if_soft_h265=false&skip_ddjb=false&from_float_window=1&if_h265=false&use_hub=1&_live_goods_id=210668807838&_live_refer=10015&page_from=1&mall_id=999151840&container_hub_type=hub%2Fzb_promotions_scene%2Fweak&head_ids=live_room.html%3Fext%3D%257B%2522feed_scene_id%2522%253A320%257D%26room_id%3D88106923%26play_url%3Dhttp%253A%252F%252Fliveplay04.pddpic.com%252Flive%252F17283_production_sprite_20210622_88106923_02.flv%253FtxSecret%253Dabd3df505cff53c3343f95385a38b76e%2526txTime%253D60dd7092%2526pub_type%253Dbd-pddobs%26biz_type%3D0%26scene_id%3D50%26if_soft_h265%3Dfalse%26skip_ddjb%3Dfalse%26from_float_window%3D1%26if_h265%3Dfalse%26use_hub%3D1%26_live_goods_id%3D210668807838%26_live_refer%3D10015%26page_from%3D1%26mall_id%3D999151840%26container_hub_type%3Dhub%252Fzb_promotions_scene%252Fweak%26hub_type%3Dhub%252Fzb_promotions_scene%252Fweak%26net%3D1%26location_required%3D0%26low_latency%3Dfalse&hub_type=hub%2Fzb_promotions_scene%2Fweak&net=1&location_required=0&low_latency=false\",\"h5_link_url\":\"ddplteec.html?mall_id=999151840&page_from=1&skip_ddjb=false&_live_goods_id=210668807838\",\"anchor_type\":0,\"response_time_stamp\":null,\"authorize_toast\":null,\"living_mall_id\":999151840,\"mall_id\":999151840,\"goods_id\":210668807838,\"float_window_bkg_image\":null}",
                    "type": "0"
                },
                "live_type": 1,
                "on_live": 1
            },
            "more_pop_navi_button": {
                "navi_list": [
                    {
                        "icon_id": "59787",
                        "text": "常见问题",
                        "url": "questions.html"
                    },
                    {
                        "icon_id": "59786",
                        "text": "意见反馈",
                        "url": "personal_feedback.html"
                    },
                    {
                        "icon_id": "59788",
                        "text": "举报商品",
                        "url": "comm_goods_complaint.html?goods_id=210668807838"
                    }
                ]
            },
            "price_explain_section": {
                "pulldown_title": "点击查看商品价格说明"
            },
            "sku_section": {
                "consult_promotion_price": 1,
                "view_style": 0,
                "view_style_v2": 0
            },
            "title_section": {
                "channel_icon": {
                    "height": 51,
                    "id": 10,
                    "url": "https://funimg.pddpic.com/2020-12-02/640fd63d-132e-49df-8b84-84b159c5521d.png.slim.png",
                    "width": 144
                },
                "channel_icon_bef": [
                    {
                        "height": 51,
                        "id": 10,
                        "url": "https://funimg.pddpic.com/2020-12-02/640fd63d-132e-49df-8b84-84b159c5521d.png.slim.png",
                        "width": 144
                    }
                ],
                "green_icon": {
                    "desc": "订单发货后90天内如果申请退货退款或换货，拼多多将补贴退货运费",
                    "id": 3,
                    "show_tip": "收货后如不满意，可以免费退货",
                    "type": "退货包运费"
                }
            }
        }
    },
    "msg": "成功"
}

while 1:
    for i in range(10):
        msg = json.dumps(msg_dict)
        msg = msg.encode()
        producer.send('pdd_kafka', msg, partition=0)
        time.sleep(2)
        producer.flush()
        producer.close()


