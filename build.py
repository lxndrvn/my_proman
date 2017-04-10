from models import *


class Database(object):
    def __init__(self):
        self.db = db

    def connect_to_db(self):
        self.db.connect()

    def drop_table(self):
        self.db.drop_tables([Board, Card], safe=True)

    def create_tables(self):
        self.db.create_tables([Board, Card], safe=True)


if __name__ == "__main__":
    my_proman = Database()
    my_proman.connect_to_db()
    #my_proman.drop_table()
    my_proman.create_tables()

