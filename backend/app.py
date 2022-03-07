from pymongo import MongoClient

check_icon = ''
exclamation_icon = ''


class Database:
    def __init__(self):
        try:
            client = MongoClient('mongodb://localhost:27017/')
            print(f'[{check_icon}] Connected to MongoDB')
            database = client['lab-automation']
            self.collection = database['electronics']
        except Exception as e:
            print(f'[{exclamation_icon}] Could not connect to server:\n{e}')
            exit()


if __name__ == '__main__':
    Database()
