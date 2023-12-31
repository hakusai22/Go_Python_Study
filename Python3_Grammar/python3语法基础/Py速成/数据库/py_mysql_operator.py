# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/8/15 21:41

import pymysql


class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        """获取连接"""
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                                        user='root', password='12345678',
                                        database='hrs', charset='utf8mb4')
        except pymysql.Error as e:
            print('MysqlStartError: %s' % e)

    def close_conn(self):
        """关闭连接"""
        try:
            if self.conn:
                # 关闭链接
                self.conn.close()
        except pymysql.Error as e:
            print('MysqlStopError: %s' % e)

    def get_one(self):
        """获取一条数据"""
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家',))
        # print(dir(cursor))
        # print(cursor.description)
        # for k in cursor.description:
        #     print(k[0])
        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more(self):
        """获取多条数据"""
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家',))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def get_more_by_page(self, page, page_size):
        ''' 分页查询数据 '''
        offset = (page - 1) * page_size
        # 准备SQL
        sql = 'SELECT * FROM `news` WHERE `types` = %s ORDER BY `created_at` DESC LIMIT %s, %s;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行SQL
        cursor.execute(sql, ('百家', offset, page_size))
        # print(dir(cursor))
        # 拿到结果
        rest = [dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()]
        # 处理数据
        # 关闭cursor/链接
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        ''' 插入数据 '''
        # 受影响的行数
        row_count = 0
        try:
            # 准备SQL
            sql = (
                "INSERT INTO `news`(`title`,`image`, `content`, `types`, `is_valid`) VALUE"
                "(%s, %s, %s, %s, %s);"
            )
            # 获取链接和cursor
            cursor = self.conn.cursor()
            # 执行sql
            # 提交数据到数据库
            cursor.execute(sql, ('标题11', '/static/img/news/01.png', '新闻内容5', '推荐', 1))
            # cursor.execute(sql, ('标题12', '/static/img/news/01.png', '新闻内容6', '推荐', 1, 1))
            # 提交事务
            self.conn.commit()
        except:
            print('Translation Error Rollback')
            # 回滚事务
            self.conn.rollback()
        # 执行最后一条SQL影响的行数
        row_count = cursor.rowcount
        cursor1 = self.conn.cursor()
        cursor1.execute('select `title` from news')
        print(cursor1.fetchall())
        cursor1.close()
        # 关闭cursor和链接
        cursor.close()
        self.close_conn()
        # row_count > 0 表示成功
        return row_count > 0


def main():
    obj = MysqlSearch()
    rest = obj.get_one()
    print(rest['image'])




if __name__ == '__main__':
    main()
