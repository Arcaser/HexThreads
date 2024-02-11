import pymongo
#pymngo is a python driver for MongoDB, which allows Python applications
# to interact with MongoDB
# TODO: to install pymongo type pip install pymongo in terminal or control panel

from PIL import Image 
from io import BytesIO

class ImageProcessing:
    # The ImageProcessing class now connects to a MongoDB database specified by the connection_string, db_name, and collection_name.
    def __init__(self, connection_String, db_name, collection_name):
        self.client=pymongo.MongoClient(connection_String)
        self.db=self.client[db_name]
        self.collection=self.db[collection_name]

    def upload_image(self, image_path, image_name):
    # The upload_image method uploads an image file to MongoDB by reading the image bytes and inserting them into the database as a binary field.
        try:
            with open(image_path, "rb") as image_file:
                image_bytes = image_file.read()
                # Insert the image bytes into MongoDB
                image_data= {
                    "name": image_name,
                    "image": image_bytes
                }
                result=self.collection.insert_one(image_data)
                print(f"Image '{image_name}' uploaded successfully with ObjectId: {result.inserted_id}")
        except FileNotFoundError:
            print(f"Error: File '{image_path}' not found.")

    def get_image(self, image_name):
    # The get_image method retrieves an image from MongoDB by its name and returns a PIL Image object.
        try: 
            # Find the image in MongoDB by name
            image_data= self.collection.find_one({"name": image_name})
            if image_data:
                # Create a PIL Image object from the image bytes
                image_bytes=image_data["image"]
                image=Image.open(BytesIO(image_bytes))
                return image
            else: 
                print(f"Error: Image '{image_name}' not found in the database.")
                return None
        except Exception as e:
            print(f"Error retrieving image: {e}")
            return None
    
    def close_connection(self):
    # The close_connection method closes the MongoDB client connection when done.
        self.client.close()
        print("MongoDB connection closed.")
        
# Example usage:
if __name__ == "__main__":
    # Initialize ImageProcessing object with MongoDB connection details
    connection_string = "mongodb://localhost:27017/"
    db_name = "image_db"
    collection_name = "images"
    image_processor = ImageProcessing(connection_string, db_name, collection_name)

    # Upload image to MongoDB
    image_path = "path/to/your/image.jpg"
    image_name = "example_image"
    image_processor.upload_image(image_path, image_name)

    # Get image from MongoDB
    retrieved_image = image_processor.get_image(image_name)
    if retrieved_image:
        retrieved_image.show()

    # Close MongoDB connection
    image_processor.close_connection()

        
    
    
