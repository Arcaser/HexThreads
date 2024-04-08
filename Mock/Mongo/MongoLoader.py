from pymongo import MongoClient
from colorthief import ColorThief
from Process import imageProccessing

class loader:

    def __init__(self, uri, db):
        self.client = MongoClient(uri)
        self.db = self.client[db]
        
    
`   #takes an image file, extracts 10 colors from it, 
    def insert_cloth(self,id,image):

        #create the image2string object
        image2string = imageProccessing.ImageProcessing()

        #create the colortheif object and process the image of the clothing
        color_thief = ColorThief(image)
        # get the dominant color
        dominant_color = color_thief.get_color(quality=1)
        # build a color palette
        palette = color_thief.get_palette(color_count=10)

        #turn the image into a string so it can be stored in the database
        imageString = image2string(image)

        #insert the clothing into the database
        self.db.clothes.insert_one({"_id": id, "imageString": imageString, "dominant_color": dominant_color, "palette": palette})

    def insert_store(self,id,clothes):
        self.db.stores.insert_one({"_id": id, "clothes": clothes})
        for i,cloth in clothes:
            self.insert_cloth(i,cloth)
            i+=1