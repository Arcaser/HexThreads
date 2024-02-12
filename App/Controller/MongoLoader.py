from pymongo import MongoClient
from colorthief import ColorThief
from converter import converter

class loader:

    def __init__(self, uri, db):
        self.client = MongoClient(uri)
        self.db = self.client[db]
        self.name = converter()


    # takes an image file, extracts 10 colors from it
    def insert_cloth(self, id,store, image):
        dominant_color,palette,imageString = self.ProcessImage(image)

        # insert the clothing into the database
        self.db.clothes.insert_one(
            {"_id": id,
             "store":store,
             "imageString": imageString, 
             "dominant_color": dominant_color, 
             "palette": palette
        })


    #will take a list of images and add them into the database
    def insert_store(self, id,store_name, clothes):
        self.db.stores.insert_one({
            "_id": id,
            "name":store_name, 
            "clothes": clothes})
        
        for cloth in enumerate(clothes):
            i = self.generate_unique_id()
            self.insert_cloth(i,store_name, cloth)
    
    #inserts a clothing item that is not tied to a store in the database. used when the users are uploading their own clothing items
    def insert_cloth_nonStore(self,image):
        id = self.generate_unique_id()
        dominant_color,palette,image2string = self.ProcessImage(image)
        self.db.clothes.insert_one(
            {"_id": id,
             "store":"nonStore",
             "imageString": image2string, 
             "dominant_color": dominant_color, 
             "palette": palette
        })

    #takes an image and returns the dominant color and the color palette, as well as the image in string format
    def ProcessImage(self,image):
        print(image)
        image2string = self.name.image2string(image)
        
        color_thief = ColorThief(image)

        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)

        # build a color palette
        palette = color_thief.get_palette(color_count=10)
        return dominant_color,palette,image2string
    

    #creates a unique numerical id for the clothing items. Current adds 1 to the current count of clothing items in the database
    def generate_unique_id(self):
        id = self.db.clothes.count_documents({}) + 1
        print(id)
        return id