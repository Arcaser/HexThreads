from flask import Flask , url_for, request, redirect , jsonify, render_template
from colorthief import ColorThief
from io import BytesIO
import base64
from db import MongoDBConnector

app = Flask(__name__)


# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "mongodb+srv://Arcaser:Gb4Y1PWqhXnwY2jh@hexthreads.mw1ibnw.mongodb.net/?retryWrites=true&w=majority"
db_name = "hexThreads"



# Make a mongo main controller because this is starting to get messy
db2 = MongoDBConnector(db_uri, db_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image_items' not in request.json:
        return jsonify({"error": "Missing image_items in request"}), 400

    for item in request.json['image_items']:
        store_name = item.get('store')
        image_data = item.get('binary')
        
        # Decode base64 image to binary if necessary
        # Ensure you're receiving the binary data in base64 format from the client
        image_binary = base64.b64decode(image_data)
        
        db2.add_clothes_store(store_name, image_binary)

    return jsonify({"message": "Upload successful"}), 200
    
#colorgrab route with store
@app.route('/colorgrab/<store>/<rgb>', methods=['GET', 'POST'])
def colorgrab(rgb,store):
    if request.method == 'GET':
        return "Please use POST method to send the RGB value"
    else:
        
        results = db2.get_colors(rgb, store)
        return jsonify(results)
    
#colorgrab no store 
@app.route('/colorgrab/<rgb>', methods=['GET', 'POST'])
def colorgrab_nostore(rgb):
    if request.method == 'GET':
        return "Please use POST method to send the RGB value"
    else:
        
        results = MongoDBConnector.get_colors(rgb, "NoStore")
        return jsonify(results)

# Run the app
if __name__ == "__main__":
    app.run()

