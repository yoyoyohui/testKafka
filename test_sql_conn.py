import pymysql

def save_mysql():

    DB = conn_mysql()  # 连接mysql
    init_pdd_goods_table(DB)
    init_pdd_goods_attribute_table(DB)  # 初始化新表
    init_pdd_goods_expand_table(DB)
    init_pdd_goods_cate_table(DB)
    init_pdd_goods_price_table(DB)
    init_pdd_mall_table(DB)


    DB.close()


def conn_mysql():

    DBHOST = "139.159.140.38"
    DBUSER = "root"
    DBPASS = "20A3NBVJnWZtNzxumYOz"
    DBNAME = "pdd"
    DBPORT = 4000

    try:
        DB = pymysql.connect(host=DBHOST, user=DBUSER, passwd=DBPASS, port=DBPORT, database=DBNAME)
        print("数据库连接成功")
    except pymysql.Error as e:
        print("数据库连接失败:" + str(e))
    return DB


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
                    market_price DECIMAL(10, 2) COMMENT '商品原价格',
                    comment_num int(11) COMMENT '评论数',
                    is_live int(11) COMMENT '是否在售1或0',
                    brand_id VARCHAR(30) COMMENT '商品品牌id',
                    brand_name VARCHAR(200) COMMENT '商品品牌名称',
                    cate1 BIGINT(11) COMMENT '类别id1',
                    cate2 BIGINT(11) COMMENT '类别id2',
                    cate3 BIGINT(11) COMMENT '类别id3',
                    cate4 BIGINT(11) COMMENT '类别id4',
                    cate5 BIGINT(11) COMMENT '类别id5',
                    img_url VARCHAR(255) COMMENT '轮拨主图链接',
                    last_update_time datetime COMMENT '抓取时间',
                    add_time datetime COMMENT '抓取日期'
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
                    attribute_list VARCHAR(800) COMMENT '商品属性',
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


# 商品分类表
def init_pdd_goods_cate_table(DB):
    try:
        cur = DB.cursor()
        sql1 = "DROP TABLE IF EXISTS pdd_goods_cate;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_goods_cate(
                    cate_id BIGINT(11) COMMENT '分类id',
                    asin_id VARCHAR(20) COMMENT '商品id',
                    last_update_time datetime COMMENT '抓取时间',
                    date_ date COMMENT '抓取日期',
                    primary key(asin_id, cate_id, date)
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
                    date_ date COMMENT '日期',
                    source_ INT null COMMENT '来源',
                    primary key(asin_id, date_)
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
        sql1 = "DROP TABLE IF EXISTS 51job;"
        cur.execute(sql1)
        sql2 = '''
                CREATE table pdd_mall(
                    mall_id VARCHAR(30) PRIMARY KEY COMMENT '店铺id',
                    mall_name VARCHAR(200) not null COMMENT '店铺名',
                    last_update_time datetime COMMENT '更新时间',
                    add_time datetime COMMENT '抓取时间'
                );
            '''
        cur.execute(sql2)
        print("数据库操作成功")
        cur.close()
    except pymysql.Error as e:
        print("数据库操作失败:" + str(e))


def main():
    save_mysql()

main()