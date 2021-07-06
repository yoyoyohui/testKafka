import pymysql
import json
data_dict={'hd_thumb_url': 'http://t00img.yangkeduo.com/goods/images/2020-12-21/e335700a91af5519bff0300d6a4b8b9d.jpeg', 'flag': 0, 'comment_num': 200, 'freeshiping': 0, 'send_hour': 0, 'price': 7790, 'mall_name': '施索数码电器官方旗舰店', 'mall_id': '999151840', 'brand_id': 357642, 'brand_name': '', 'goods_id': '210668807838', 'goods_name': '手机自拍杆全自动多功能三脚架苹果安卓通用360度拍照直播支架', 'is_onsale': 1, 'sales': 100000, 'cat1': 2933, 'cat2': 2946, 'cat3': 19268, 'cat4': 19271, 'online_time': 1608480000, 'last_update_time': 1625300555, 'old_price': 0, 'is_live': 0, 'goods_property_list': '品牌:施索,杆身材质:铝合金,控制方式:蓝牙遥控', 'detail_img_url_list': 'https://img.pddpic.com/mms-material-img/2020-12-12/9e136db8-d94e-408d-b793-62ba3749d4b8.jpeg.a.jpeg,https://img.pddpic.com/mms-material-img/2020-12-12/98ac4636-80d3-4e92-badc-deb69897d2d4.jpeg.a.jpeg,https://img.pddpic.com/mms-material-img/2020-12-12/34694d8c-6434-4543-8c7f-26e495d4ac7e.jpeg.a.jpeg,https://t16img.yangkeduo.com/garner-api/a8e9f34a58b879ae1624fbe8a24654d0.jpeg,https://t16img.yangkeduo.com/garner-api/6210342c5e2e428533256608482270c6.jpeg,https://t16img.yangkeduo.com/garner-api/ac949161d4a0c35e29ee36bded7e0aa1.jpeg,https://t16img.yangkeduo.com/garner-api/b1de81c31c7e95cdf9e16baabb1eac57.jpeg,https://t16img.yangkeduo.com/garner-api/a0665836b4198f71af9eb64ad71dad02.jpeg,https://t16img.yangkeduo.com/garner-api/f7e2debfa6fd176c4897de0affb48e8f.jpeg,https://t16img.yangkeduo.com/garner-api/9b9af7c34a4395448cbaaec482e6e2e1.jpeg,https://t16img.yangkeduo.com/garner-api/fe613429789cd6832916c187a2f7b256.jpeg,https://t16img.yangkeduo.com/garner-api/bbcd15ad6832e5b5bda81b078137db8b.jpeg,https://t16img.yangkeduo.com/garner-api/3778a0ad0641f4aa33e50908245e9b57.jpeg,https://t16img.yangkeduo.com/garner-api/f81d97041fddd580781e658be2f73414.jpeg,https://t16img.yangkeduo.com/garner-api/0e8e4b3739eba86462b611d28ba4afb0.jpeg,https://t16img.yangkeduo.com/garner-api/8c65e7a8931fb46e2a1f94a10f472d85.jpeg,https://t16img.yangkeduo.com/garner-api/ccc9101ca8b1d0135d13154c0d21ad98.jpeg,https://t16img.yangkeduo.com/garner-api/6e786e5ae64c40738bf2d16ddfc3fd74.jpeg,https://t16img.yangkeduo.com/garner-api/5b88355e381e69f3b42ec40a15ef15ae.jpeg,https://t16img.yangkeduo.com/garner-api/f863668a695c6e75e1dc194ad61f3100.jpeg,https://t16img.yangkeduo.com/garner-api/ac9f4706d159e27dea962fc24122e5d5.jpeg,https://t16img.yangkeduo.com/garner-api/ae36c3c149ee54bd545cbffc96cc2707.jpeg,https://t16img.yangkeduo.com/garner-api/bcdcb97512bb4d28b49a3b56a01a0695.jpeg', 'goods_num': 15, 'sales_num': '10万+', 'service_score': 4.68}

def save_mysql(data_dict):
    db = conn_mysql1()  # 连接mysql
    create_db(db)       # 创建数据库

    DB = conn_mysql2()  # 连接mysql

    # 商品表
    init_pdd_goods_table(DB)
    insert_goods_info(DB, data_dict)

    # 属性表
    init_pdd_goods_attribute_table(DB)  # 初始化新表
    insert_goods_attribute(DB, data_dict)

    # 店铺表
    init_pdd_mall_table(DB)
    insert_pdd_mall_table(DB, data_dict)

    # init_pdd_goods_expand_table(DB)
    # insert_goods_expand(DB, data_dict)
    #
    # init_pdd_goods_price_table(DB)
    # insert_goods_price_table(DB, data_dict)

    DB.close()

def conn_mysql1():

    DBHOST = "localhost"
    DBUSER = "root"
    DBPASS = "246759"
    # DBNAME = "people"
    DBPORT = 3306

    try:
        db = pymysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, port=DBPORT)
        print("mysql连接成功")
    except pymysql.Error as e:
        print("mysql连接失败:" + str(e))
    return db


def conn_mysql2():

    DBHOST = "localhost"
    DBUSER = "root"
    DBPASS = "246759"
    DBNAME = "pdd"
    DBPORT = 3306

    try:
        DB = pymysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, port=DBPORT, database=DBNAME)
        print("数据库连接成功")
    except pymysql.Error as e:
        print("数据库连接失败:" + str(e))
    return DB


def create_db(db):
    try:
        cur = db.cursor()
        sql = "create database pdd;"
        cur.execute(sql)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))
    db.close()


# 商品表
def init_pdd_goods_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_goods;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_goods(
                    asin_id VARCHAR(20) PRIMARY key COMMENT '商品id',
                    goods_name VARCHAR(500) COMMENT '商品名',
                    mall_id VARCHAR(30) COMMENT '店铺id',
                    mall_name VARCHAR(200) COMMENT '店铺名',
                    price DECIMAL(10, 2) COMMENT '商品价格',
                    comment_num int(11) COMMENT '评论数',
                    brand_id VARCHAR(30) COMMENT '商品品牌id',
                    brand_name VARCHAR(200) COMMENT '商品品牌名称',
                    cate1 BIGINT(11) default null COMMENT '类别id1',
                    cate2 BIGINT(11) default null COMMENT '类别id2',
                    cate3 BIGINT(11) default null COMMENT '类别id3',
                    cate4 BIGINT(11) default null COMMENT '类别id4',
                    img_url VARCHAR(255) COMMENT '轮拨主图链接',
                    last_update_time VARCHAR(30) COMMENT '最后更新时间'
                    );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


# 商品属性表
def init_pdd_goods_attribute_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_goods_attribute;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_goods_attribute(
                    asin_id VARCHAR(20) COMMENT '商品id',
                    attribute_list VARCHAR(2000) COMMENT '商品属性',
                    detail_img_url_list VARCHAR(2000) COMMENT '图片详情链接',
                    last_update_time VARCHAR(30) COMMENT '最后更新时间',
                    PRIMARY KEY(asin_id)
                    );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


# 商品图片描述表
def init_pdd_goods_expand_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_goods_expand;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_goods_expand(
                    asin_id VARCHAR(20) PRIMARY KEY COMMENT '商品id',
                    img_url_list text COMMENT '商品详情图片'
                    );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


# 商品价格表
def init_pdd_goods_price_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_goods_price;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_goods_price(
                    asin_id VARCHAR(20) COMMENT '商品id',
                    price DECIMAL(10, 2) COMMENT '商品价格',
                    old_price int(11) COMMENT '商品原价',
                    is_onsale int(11) COMMENT '是否打折1or0',
                    sales int(11) COMMENT '打折力度',
                    source_ INT null COMMENT '来源',
                    primary key(asin_id)
                    );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


# 店铺表
def init_pdd_mall_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_mall;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_mall(
                    mall_id VARCHAR(30) PRIMARY KEY COMMENT '店铺id',
                    mall_name VARCHAR(200) not null COMMENT '店铺名',
                    goods_num int(11) COMMENT '店铺商品数量',
                    sales_num VARCHAR(30) COMMENT '商店商品拼单数量',
                    service_score FLOAT COMMENT '商店评分',
                    last_update_time VARCHAR(30) COMMENT '更新时间',
                    create_time VARCHAR(30) COMMENT '抓取日期'
                );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


def insert_goods_info(DB, data_dict):
    try:
        cur = DB.cursor()  # 在表中插入数据
        asin_id = data_dict['goods_id']
        goods_name = data_dict['goods_name']
        mall_id = data_dict['mall_id']
        mall_name = data_dict['mall_name']
        price = data_dict['price']
        comment_num = data_dict['comment_num']
        brand_id = data_dict['brand_id']
        brand_name = data_dict['brand_name']
        cate1 = data_dict['cat1']
        cate2 = data_dict['cat2']
        cate3 = data_dict['cat3']
        cate4 = data_dict['cat4']
        img_url = data_dict['hd_thumb_url']
        last_update_time = data_dict['last_update_time']
        sql = '''
                    INSERT INTO pdd_goods(asin_id,goods_name,mall_id,mall_name,price,comment_num,brand_id,brand_name,cate1,cate2,cate3,cate4,img_url,last_update_time)
                    VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    '''
        value = (asin_id,goods_name,mall_id,mall_name,price,comment_num,brand_id,brand_name,cate1,cate2,cate3,cate4,img_url,last_update_time)
        cur.execute(sql, value)
        DB.commit()
        cur.close()
    except Exception as e:
        print(e)
        DB.rollback()

def insert_goods_attribute(DB, data_dict):
    try:
        cur = DB.cursor()  # 在表中插入数据
        asin_id = data_dict['goods_id']
        attribute_list = json.dumps(data_dict['goods_property_list'], ensure_ascii=False)
        detail_img_url_list = json.dumps(data_dict['detail_img_url_list'], ensure_ascii=False)
        last_update_time = data_dict['last_update_time']
        sql = '''
                    INSERT INTO pdd_goods_attribute(asin_id, attribute_list, detail_img_url_list, last_update_time)
                    VALUE(%s, %s, %s, %s);
                '''
        value = (asin_id, attribute_list, detail_img_url_list, last_update_time)
        cur.execute(sql, value)
        DB.commit()
        cur.close()
    except Exception as e:
        print(e)
        DB.rollback()

def insert_goods_expand(DB, data_dict):
    try:
        cur = DB.cursor()  # 在表中插入数据

        asin_id = data_dict['goods_id']
        img_url_list = data_dict['detail_img_url_list']
        sql = '''
                    INSERT INTO pdd_goods_expand(asin_id, img_url_list)
                    VALUE(%s, %s);
                '''
        value = (asin_id, img_url_list)
        cur.execute(sql, value)
        DB.commit()
        cur.close()
    except Exception as e:
        print(e)
        DB.rollback()

def insert_goods_price_table(DB, data_dict):
    try:
        cur = DB.cursor()  # 在表中插入数据

        asin_id = data_dict['goods_id']
        price = data_dict['price']
        old_price = data_dict['old_price']
        is_onsale = data_dict['is_onsale']
        sales = data_dict['sales']
        sql = '''
                    INSERT INTO pdd_goods_price(asin_id,price,old_price, is_onsale, sales)
                    VALUE(%s, %s, %s, %s, %s);
                '''
        value = (asin_id, price, old_price, is_onsale, sales)
        cur.execute(sql, value)
        DB.commit()
        cur.close()
    except Exception as e:
        print(e)
        DB.rollback()

def insert_pdd_mall_table(DB, data_dict):
    try:
        cur = DB.cursor()  # 在表中插入数据

        mall_id = data_dict['mall_id']
        mall_name = data_dict['mall_name']
        goods_num = data_dict['goods_num']
        sales_num = data_dict['sales_num']
        service_score = data_dict['service_score']
        last_update_time = data_dict['last_update_time']
        create_time = data_dict['create_time']
        sql = '''
                       INSERT INTO pdd_mall(mall_id, mall_name,goods_num,sales_num,service_score,last_update_time, create_time)
                       VALUE(%s, %s, %s ,%s, %s, %s, %s);
                   '''
        value = (mall_id, mall_name, goods_num, sales_num, service_score, last_update_time,create_time)
        cur.execute(sql, value)
        DB.commit()
        cur.close()
    except Exception as e:
        print(e)
        DB.rollback()

# def main():
#     save_mysql(data_dict)
#
# main()