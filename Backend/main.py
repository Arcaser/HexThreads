import json
from flask import request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from colorthief import ColorThief
from config import db , ALLOWED_EXTENSIONS ,app
from models import Clothe 
import os
from PIL import Image
from rembg import remove


# Utility function to check file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to HexThreads!', 200

@app.route('/uploadMany', methods=['POST'])
def upload_many_files():
    files = request.files.getlist('file')
    if not files:
        return jsonify({"error": "No files part"}), 400

    results = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            original_dir = "Backend/uploads"
            modified_dir = "Backend/modified"

            os.makedirs(original_dir, exist_ok=True)
            os.makedirs(modified_dir, exist_ok=True)
            
            original_path = os.path.join(original_dir, filename)
            modified_path = os.path.join(modified_dir, filename.replace('.jpg', '.png'))

            file.save(original_path)

            input_image = Image.open(original_path)
            output_image = remove(input_image)

            if output_image.mode == 'RGBA':
                output_image = output_image.convert('RGB')
                modified_path = modified_path.replace('.jpg', '.png')

            output_image.save(modified_path)

            with open(modified_path, 'rb') as imageFile:
                ct = ColorThief(imageFile)
                palette = ct.get_palette(color_count=6)

            os.remove(modified_path)
            palette_str = ','.join([f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}' for color in palette])

            new_clothe = Clothe(filePath=original_path, palette=palette_str)
            db.session.add(new_clothe)
            db.session.commit()

            results.append({'id': new_clothe.id, 'message': 'Upload successful', 'filePath': original_path})
        else:
            results.append({'filename': file.filename, 'message': 'Invalid file type or empty filename'})

    return jsonify(results), 200


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

@app.route('/match', methods=['POST'])
def match_color():
    data = request.get_json() 

    hexcode = data.get('Hex')  # Extract the hex code from the JSON data
    if not hexcode:
        return jsonify({"error": "No hex code provided"}), 400  

    hexcode = hexcode.strip().lower() 

    clothes = Clothe.query.all()  # Query all clothing items
    matches = []

    # Find all clothes that match the given hex code
    for clothe in clothes:
        if clothe.match_color(hexcode):
            matches.append(clothe.to_json())

    return jsonify(matches), 200  # Return the list of matches as JSON


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)