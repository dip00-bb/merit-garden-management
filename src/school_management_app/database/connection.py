# database/connection.py

import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        self.db_path = Path("data/school.db")


        self.db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(
                self.db_path,
                check_same_thread=False
            )
            


            self.connection.row_factory = sqlite3.Row

        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None