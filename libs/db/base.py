import logging
db_logger = logging.getLogger("db_logger")


class DbBase(object):

    def __init__(self):
        self.db = object
        self.cursor = object

    def connect(self):
        pass

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as error:
            db_logger.error(f"fail to select, error:{error}", exc_info=True)

        return result

    def get_all(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
        except Exception as error:
            db_logger.error(f"fail to select, error:{error}", exc_info=True)

        return result

    def get_all_obj(self, sql, table_name, *args):
        result_list = []
        field_list = []
        if len(args) > 0:
            for item in args:
                field_list.append(item)
        else:
            field_sql = "select COLUMN_NAME from information_schema.COLUMNS where tabl_name=%s and table_schema=%s" % (
                table_name, self.dbName
            )
            fields = self.get_all(field_sql)
            for item in fields:
                field_list.append(item[0])

        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[field_list[count]] = x
                count += 1
            result_list.append(obj)
        return result_list

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()

        except Exception as error:
            db_logger.error(f"fail to select, error:{error}", exc_info=True)
            self.db.rollback()

        return count
