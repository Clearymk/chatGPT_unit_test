import time
import pymysql


class DataBase(object):
    def __init__(self, database="lite_app"):
        self.count = 0
        try:
            self.mysql = pymysql.connect(host='10.19.124.172',
                                         port=10255,
                                         user='root',
                                         password='catlab1a509',
                                         database=database)
        except Exception:
            time.sleep(2)
            self.__init__()

    def insert_task(self, class_name, class_path):
        insert_sql = "insert into " \
                     "lite_app.unit_test(class_name, class_path) " \
                     "values (%s, %s)"

        cursor = self.mysql.cursor()
        cursor.execute(insert_sql, (class_name, class_path))
        cursor.close()
        self.mysql.commit()

    def query_task(self):
        query_sql = "select * from lite_app.unit_test where flag = 0"
        cursor = self.mysql.cursor()
        cursor.execute(query_sql)
        return cursor.fetchall()

    def update_task(self, flag, class_name):
        update_sql = "update lite_app.unit_test set flag= %s where class_name= %s"
        cursor = self.mysql.cursor()
        cursor.execute(update_sql, (flag, class_name))
        cursor.close()
        self.mysql.commit()
