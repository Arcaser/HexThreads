from pymongo import MongoClient

def create_db_collections(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]

    # List existing collections
    existing_collections = db.list_collection_names()

    # Create 'clothes' collection if it doesn't exist
    if 'clothes' not in existing_collections:
        db.create_collection('clothes')
        print("Created 'clothes' collection.")

        # Add any required indexes
        db['clothes'].create_index([("id", 1)], unique=True)
    
    # Create 'stores' collection if it doesn't exist
    if 'stores' not in existing_collections:
        db.create_collection('stores')
        print("Created 'stores' collection.")

        # Add any required indexes
        db['stores'].create_index([("id", 1)], unique=True)

    # Any additional initialization logic can go here
    # For example, setting up validation rules, additional indexes, or seed data

    print("Database initialization complete.")

# Example usage
if __name__ == "__main__":
    URI = "<Your MongoDB URI>"
    DB_NAME = "hexThreads"
    create_db_collections(URI, DB_NAME)
