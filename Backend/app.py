import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from colorthief import ColorThief
import base64
from db import MongoDBConnector

# set of supported file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app)

# function that checks whether a file has the supported extensions (png, jpg, jpeg)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "mongodb+srv://Arcaser:Gb4Y1PWqhXnwY2jh@hexthreads.mw1ibnw.mongodb.net/?retryWrites=true&w=majority"
db_name = "hexThreads"

# Make a mongo main controller because this is starting to get messy
db2 = MongoDBConnector(db_uri, db_name)

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

# route that gets the dominant color from the uploaded image
@app.route('/color', methods=['GET', 'POST'])
def get_dominant_color():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part included'}), 400
    image = request.files['file']
    if image.filename == '':
        return jsonify({'message': 'No file selected'}), 404
    if image and allowed_file(image.filename):
        ct = ColorThief(image)
        color = ct.get_color()
        hex_code = '#{:02x}{:02x}{:02x}'.format(*color)
        hex_to_json = json.dumps(hex_code)
        return hex_to_json

# route that gets the palette from the uploaded image
@app.route('/palette/<int:size>', methods=['GET', 'POST'])
def get_palette(size):
    palettes = []
    if 'file' not in request.files:
        return jsonify({'message': 'No file part included'}), 400
    image = request.files['file']
    if image.filename == '':
        return jsonify({'message': 'No file selected'}), 404
    if image and allowed_file(image.filename):
        ct = ColorThief(image)
        if size > 1:
            palette = ct.get_palette(color_count=size)
            for i in palette:
                hex_code = '#{:02x}{:02x}{:02x}'.format(*i)
                palettes.append(hex_code)
                json_palettes = json.dumps(palettes)
            #json_palettes = list(map(lambda x: json.dumps(x), palettes))
            return json_palettes
        else:
            dominant_color = ct.get_color()
            hex_code = '#{:02x}{:02x}{:02x}'.format(*dominant_color)
            palettes.append(hex_code)
            json_dominant_color = json.dumps(palettes)
            return json_dominant_color

# Run the app
if __name__ == "__main__":
    app.run()