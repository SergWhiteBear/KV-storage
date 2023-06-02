import sqlite3


class KeyValueStorage:
    def __init__(self, storage_name, db_file='KV-storage'):
        self.storage_name = storage_name
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.storage_name} (key TEXT PRIMARY KEY, value TEXT)")

    def close_conn(self):
        self.connection.close()

    def __setitem__(self, key, value):
        self.cursor.execute(f"INSERT OR REPLACE INTO {self.storage_name} (key, value) VALUES (?, ?)", (key, value))
        self.connection.commit()

    def __getitem__(self, key):
        self.cursor.execute(f"SELECT value FROM {self.storage_name} WHERE key=?", (key,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            raise KeyError(key)

    def __delitem__(self, key):
        self.cursor.execute(f"DELETE FROM {self.storage_name} WHERE key=?", (key,))
        self.connection.commit()

    def get_all_keys(self):
        self.cursor.execute(f"SELECT key FROM {self.storage_name}")
        return [row[0] for row in self.cursor.fetchall()]

    def search_value(self, value):
        self.cursor.execute(f"SELECT key FROM {self.storage_name} WHERE value=?", (value,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            raise ValueError(value)
