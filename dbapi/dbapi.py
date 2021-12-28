from random import randint
from pymongo import MongoClient


class DatabaseAPI:
    used_ids = []


    def __init__(self):
        try:
            client = MongoClient("mongodb+srv://shodan:ssyYvLdkXKqMRoph@cluster0.jqvnr.mongodb.net/users?retryWrites=true&w=majority")
            self.db = client["users"]
            self.users = self.db["users"]
            self.oper_queue = self.db["oper_queue"]
            self.moder_queue = self.db["moder_queue"]
            self.waiting_moders = self.db['wmoders']
            self.waiting_operators = self.db['wopers']
            DatabaseAPI.used_ids = [x for x in range(1, len([x for x in self.get_collection(self.users)])+1)]
        except Exception as ex:
            print(ex)


    def upload(self, collection, obj):
        collection.replace_one(obj, obj, True)


    def delete(self, collection, obj):
        collection.delete_one({'_id':obj['_id']})


    def get_collection(self, collection):
        return collection.find()


    def generate_objectid(self) -> int:
        object_id = len(DatabaseAPI.used_ids)+1
        DatabaseAPI.used_ids.append(object_id)
        return object_id
