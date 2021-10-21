import sqlite3

class KTHashDb:
    def __init__(self, reset = False):
        self.con = sqlite3.connect('kthash.db')
        self.cur = self.con.cursor()
        if reset is True:
            self.drop_table() 
        self.create_table()
    
    def close(self):
        self.con.close()
    
    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS kthash
        (
            dir_path TEXT,
            file_name TEXT,
            hash TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def drop_table(self):
        sql = """
        DROP TABLE IF EXISTS kthash
        """
        self.cur.execute(sql)
        self.con.commit()

    def query_all(self):
        sql = """
        SELECT * FROM kthash
        """
        return self.cur.execute(sql).fetchall()

    def query_where_hash(self, hash):
        sql = f"""
        SELECT * FROM kthash WHERE hash = '{hash}'
        """
        return self.cur.execute(sql).fetchall()

    def insert(self, hash_data):
        sql = ""
        if type(hash_data) is dict:
            sql = f"""
            INSERT INTO kthash VALUES ('{hash_data["dir_path"]}', '{hash_data["file_name"]}', '{hash_data["hash"]}')
            """
        elif type(hash_data) is list:
            values = ""
            for hash_object in hash_data:
                if type(hash_object) is dict:
                    values += "('{0}', '{1}', '{2}'),".format(
                        hash_object["dir_path"], 
                        hash_object["file_name"], 
                        hash_object["hash"]
                    )

            sql = "INSERT INTO kthash VALUES " + values[0:-1]

        self.cur.execute(sql)
        self.con.commit()