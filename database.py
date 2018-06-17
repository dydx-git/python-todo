import sqlite3


class Database:
    def save_task(self, task):
        insert_task_query = "INSERT INTO tasks VALUES (?)"
        insert_task_data = (task,)
        self.runQuery(insert_task_query, insert_task_data)

    def load_tasks(self):
        load_tasks_query = "SELECT task FROM tasks"
        my_tasks = self.runQuery(load_tasks_query, receive=True)

        return my_tasks

    @staticmethod
    def runQuery(sql, data=None, receive=False):
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)

        if receive:
            return cursor.fetchall()
        else:
            conn.commit()

        conn.close()

    @staticmethod
    def firstTimeDB():
        create_tables = "CREATE TABLE tasks (task TEXT)"
        Database.runQuery(create_tables)

        default_task_query = "INSERT INTO tasks VALUES (?)"
        default_task_data = ("--- Add Items Here ---",)
        Database.runQuery(default_task_query, default_task_data)
