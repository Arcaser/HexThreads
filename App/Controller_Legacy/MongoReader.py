from pymongo import MongoClient

class reader:

    def __init__(self, uri, db):
        self.client = MongoClient(uri)
        self.db = self.client[db]

    # returns a list of all the clothing items in the database
    def get_all_clothes(self):
        clothes = self.db.clothes.find()
        return clothes

    # returns a list of all the clothing items in the database
    def get_all_stores(self):
        stores = self.db.stores.find()
        return stores

    # returns a list of all the clothing items in the database
    def get_clothes_by_store(self, store):
        clothes = self.db.clothes.find({"store": store})
        return clothes

    # returns a list of all the clothing items in the database
    def get_cloth_by_id(self, id):
        cloth = self.db.clothes.find_one({"_id": id})
        return cloth

    # returns a list of all the clothing items in the database
    def get_store_by_id(self, id):
        store = self.db.stores.find_one({"_id": id})
        return store

    # returns a list of all the clothing items in the database
    def get_clothes_by_color(self, color):
        clothes = self.db.clothes.find({"dominant_color": color})
        return clothes

    # returns a list of all the clothing items in the database
    def get_clothes_by_palette(self, palette):
        clothes = self.db.clothes.find({"palette": palette})
        return clothes