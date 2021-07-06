import json
import re
import time


def detail_goods_app_tidb_parse(goods_info):
    if not goods_info:
        return
    item = {}
    try:
        if not goods_info["goods"].get("goods_id", ""):
            return
        if 'hd_thumb_url' in goods_info["goods"]:
            item['hd_thumb_url'] = goods_info["goods"]['hd_thumb_url']
        else:
            item['hd_thumb_url'] = 0
        item['flag'] = 0
        if 'review_num' in goods_info["review"]["review_data"]:
            item['comment_num'] = goods_info["review"]["review_data"]['review_num']
        else:
            item['comment_num'] = 0
        item['freeshiping'] = 0
        item['send_hour'] = 0
        if "min_group_price" in goods_info["price"]:
            item['price'] = goods_info["price"]["min_group_price"]
        else:
            item['price'] = ""
        if 'mall_name' in goods_info["mall_entrance"]["mall_data"]:
            item['mall_name'] = goods_info["mall_entrance"]["mall_data"]['mall_name']
        else:
            item['mall_name'] = ""
        if 'mall_id' in goods_info["mall_entrance"]["mall_data"]:
            item['mall_id'] = str(goods_info["mall_entrance"]["mall_data"]['mall_id'])  # 更改为 str 格式
        else:
            item['mall_id'] = 0
        if 'brand_id' in goods_info["goods"]:
            item['brand_id'] = goods_info["goods"]['brand_id']
        else:
            item['brand_id'] = 0
        if 'brand_name' in goods_info["goods"]:
            item['brand_name'] = goods_info["goods"]['brand_name']
        else:
            item['brand_name'] = ""
        item['goods_id'] = str(goods_info["goods"].get('goods_id'))  # 更改为 str 格式
        item['goods_name'] = goods_info["goods"].get('goods_name')
        item['is_onsale'] = 1
        # #  sale价格处理-----------------------------------------------------
        if 'side_sales_tip' in goods_info["goods"]:
            item['sales'] = goods_info["goods"]['side_sales_tip']
        else:
            item['sales'] = 0
        if re.findall('\+', item['sales']) == ['+']:
            item['sales'] = re.sub('\+', "", item['sales'])
        if re.findall(r'[\u4e00-\u9fa5]+', item['sales']):
            if re.findall('万', item['sales']) == ["万"]:
                sale = re.sub(r'[\u4E00-\u9FA5]+', "", item['sales'])
                item['sales'] = float(sale) * 10000
        item['sales'] = int(item['sales'])
        # -----------------------------------------------------------------
        if 'cat_id_1' in goods_info["goods"]:
            item['cat1'] = goods_info["goods"]['cat_id_1']
        else:
            item['cat1'] = ""
        if 'cat_id_2' in goods_info["goods"]:
            item['cat2'] = goods_info["goods"]['cat_id_2']
        else:
            item['cat2'] = ""
        if 'cat_id_3' in goods_info["goods"]:
            item['cat3'] = goods_info["goods"]['cat_id_3']
        else:
            item['cat3'] = ""
        if 'cat_id_4' in goods_info["goods"]:
            item['cat4'] = goods_info["goods"]['cat_id_4']
        else:
            item['cat4'] = ""
        cat_list = goods_info["goods"].get('cat_ids')
        if isinstance(cat_list, list):
            for i, tab in enumerate(cat_list):
                key = 'cat{}'.format(i + 1)
                item[key] = tab

        #  时间处理
        online_time = re.search(r"\d{4}-\d{2}-\d{2}", goods_info["goods"].get('hd_thumb_url'))
        if online_time:
            item['online_time'] = int(time.mktime(time.strptime(online_time.group(), "%Y-%m-%d")))
        else:
            item['online_time'] = int(time.time())
        item['last_update_time'] = int(time.time())
        item['create_time'] = int(time.time())

        item['old_price'] = 0
        item['is_live'] = 0

        # 商品属性处理
        # if 'goods_property' in goods_info['goods']:
        #     goods_property = goods_info['goods']['goods_property']
        #     goods_property_list = []
        #     for em in goods_property:
        #         key = em.get('key')
        #         values = em.get('values')[0]
        #         property = str(key + ':' + values)
        #         goods_property_list.append(property)
        #     goods_property_list = ','.join(goods_property_list)
        #     item['goods_property_list'] = goods_property_list
        # else:
        #     item['goods_property_list'] = ''

        # 商品属性处理
        if 'goods_property' in goods_info['goods']:
            goods_property = goods_info['goods']['goods_property']

            item['goods_property_list'] = goods_property
        else:
            item['goods_property_list'] = ''


        # 详情图片url处理
        if 'decoration' in goods_info['goods']:
            decoration_list = goods_info['goods']['decoration']
            detail_img_url = []
            for decoration in decoration_list:
                contents = decoration.get('contents')[0].get('img_url')
                detail_img_url.append(contents)
            item['detail_img_url_list'] = detail_img_url   #列表存入新列表
        else:
            item['detail_img_url_list'] = ''



        # 商店商品数量
        if 'goods_num' in goods_info['mall_entrance']['mall_data']:
            goods_num = goods_info['mall_entrance']['mall_data']['goods_num']
            item['goods_num'] = goods_num
        else:
            item['goods_num'] = ''

        # 商店商品拼单数量
        if 'sales_tip' in goods_info['mall_entrance']['mall_data']:
            sales_num = goods_info['mall_entrance']['mall_data']['sales_tip']
            rule = re.compile(r"已拼: (.*?)件", re.S)
            result = rule.findall(sales_num)
            item['sales_num'] = result[0]
        else:
            item['sales_num'] = ''

        # 商店评分
        if 'service_score' in goods_info['mall_entrance']['mall_data']['dsr']:
            service_score = goods_info['mall_entrance']['mall_data']['dsr']['service_score']
            item['service_score'] = service_score
        else:
            item['service_score'] = ''


        return item
    except Exception as e:
        print(e)

