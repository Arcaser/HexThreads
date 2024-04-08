from pymongo import MongoClient
from colorthief import ColorThief
from io import BytesIO
from datetime import datetime


class MongoDBConnector:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    #add clothes store takes binary
    def add_clothes_store(self, store_name, image_binary):
        # Use BytesIO to create a stream from the binary data
        image_stream = BytesIO(image_binary)
        
        color_thief = ColorThief(image_stream)
        
        dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=6, quality=1)  # Adjust color_count as needed
        
        # Insert document into MongoDB
        collection = self.db['clothes_stores']
        document = {
            "store_name": store_name,
            "image": image_binary,
            "palette": palette,
            "dominant_color": dominant_color,
            "date": datetime.now()  # Stores the current date and time
        }
        collection.insert_one(document)
        return True
    
    def get_colors(self, rgb, store):
        # Construct the query based on whether a store name is provided
        if store == "NoStore":
            query = {"palette": {"$elemMatch": {"$eq": list(rgb)}}}
        else:
            query = {"store_name": store, "palette": {"$elemMatch": {"$eq": list(rgb)}}}

        # Execute the query
        results = self.db['clothes_stores'].find(query)

        # Collect the results
        matching_documents = list(results)
        
        # Return the matching documents
        return matching_documents