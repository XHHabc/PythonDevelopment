from pymysql import Connect


class Database:
    def __init__(self, host, port, user, password, database):
        self.conn = Connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        # 如果表不存在则创建
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(create_table_query)

    def insert_data(self, table_name, data):
        insert_query = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(data))})"
        self.cursor.execute(insert_query, data)

    def select_data(self, table_name, columns="*", condition=None):
        select_query = f"SELECT {columns} FROM {table_name}"
        if condition:
            select_query += f" WHERE {condition}"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def update_data(self, table_name, set_values, condition=None):
        update_query = f"UPDATE {table_name} SET {set_values}"
        if condition:
            update_query += f" WHERE {condition}"
        self.cursor.execute(update_query)

    def delete_data(self, table_name, condition=None):
        delete_query = f"DELETE FROM {table_name}"
        if condition:
            delete_query += f" WHERE {condition}"
        self.cursor.execute(delete_query)

    def commit_changes(self):  # 事务提交
        self.conn.commit()

    def close_connection(self):  # 断开连接
        self.cursor.close()
        self.conn.close()

# if __name__ == '__main__':
#     db = Database('localhost', 3306, 'root', '123456', 'handsData')
    # db.update_data('operate', f"trigger_num1 = {str(22)}", condition="id = 1")
    # db.commit_changes()
    #
    # new_portData = db.select_data('operate', condition="id IN (1,2,3,4)")
    # print(new_portData)
