from flask import Flask , url_for, request, redirect , jsonify
from colorthief import ColorThief
from io import BytesIO
import base64
import db

app = Flask(__name__)


# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "mongodb+srv://Arcaser:Gb4Y1PWqhXnwY2jh@hexthreads.mw1ibnw.mongodb.net/?retryWrites=true&w=majority"
db_name = "hexThreads"



# Make a mongo main controller because this is starting to get messy
db = db(db_uri, db_name)

@app.route('/', methods=['GET'])
def home():
    return url_for('index.html')

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
        
        db.add_clothes_store(store_name, image_binary)

    return jsonify({"message": "Upload successful"}), 200
    
#colorgrab route
@app.route('/colorgrab/{store}/{rgb}', methods=['GET', 'POST'])
def colorgrab(rgb,store):
    if request.method == 'GET':
        return "Please use POST method to send the RGB value"
    else:
        
        results = db.get_colors(rgb, store)
        return jsonify(results)
    

if __name__ == "__main__":
    app.run()

