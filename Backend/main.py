import base64
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from colorthief import ColorThief
from config import db, ALLOWED_EXTENSIONS, app
from models import Clothe
import os
from PIL import Image

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
            original_dir = "uploads"
            modified_dir = "modified"
            os.makedirs(original_dir, exist_ok=True)
            os.makedirs(modified_dir, exist_ok=True)
            original_path = os.path.join(original_dir, filename)
            modified_path = os.path.join(modified_dir, filename.replace('.jpg', '.png'))
            file.save(original_path)
            input_image = Image.open(original_path)
            output_image = input_image
            if output_image.mode == 'RGBA':
                output_image = output_image.convert('RGB')
                modified_path = modified_path.replace('.jpg', '.png')
            output_image.save(modified_path)
            with open(modified_path, 'rb') as imageFile:
                paletteList = []
                ct = ColorThief(imageFile)
                palette = ct.get_palette(color_count=6)
                for color in palette:
                    hex_code = '#{:02x}{:02x}{:02x}'.format(*color)
                    paletteList.append(hex_code)
                palette_str = ','.join(paletteList)
            os.remove(modified_path)
            new_clothe = Clothe(filePath=original_path, palette=palette_str)
            db.session.add(new_clothe)
            db.session.commit()
            results.append({'id': new_clothe.id, 'message': 'Upload successful', 'filePath': original_path})
        else:
            results.append({'filename': file.filename, 'message': 'Invalid file type or empty filename'})
    return jsonify(results), 200

@app.route('/palette/<int:size>', methods=['GET', 'POST'])
def get_palette(size):
    palette = []
    if 'file' not in request.files:
        return jsonify({'message': 'No file part included'}), 400
    image = request.files['file']
    if image.filename == '':
        return jsonify({'message': 'No file selected'}), 404
    if image and allowed_file(image.filename):
        ct = ColorThief(image)
        if size <= 1:
            color = ct.get_color()
            hex_code = '#{:02x}{:02x}{:02x}'.format(*color)
            palette.append(hex_code)
            palette_to_json = json.dumps(palette)
            return palette_to_json
        else:
            ct_palettes = ct.get_palette(color_count=size)
            for i in ct_palettes:
                hex_code = '#{:02x}{:02x}{:02x}'.format(*i)
                palette.append(hex_code)
            palette_to_json = json.dumps(palette)
            return palette_to_json

@app.route('/match', methods=['GET', 'POST'])
def match_color():
    data = request.get_json()
    hexcode = data.get('Hex')  # Extract the hex code from the JSON data
    if not hexcode:
        return jsonify({"error": "No hex code provided"}), 400

    clothes = Clothe.query.all()  # Query all clothing items
    matches = []

    # Find all clothes that match the given hex code
    for clothe in clothes:
        if clothe.match_color(hexcode):
            clothe_info = clothe.to_json()
            image_path = os.path.join('uploads', clothe.filePath)

            # Read and encode the image in Base64
            with open(image_path, 'rb') as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
            clothe_info["image_data"] = f"data:image/{get_file_extension(clothe.filePath)};base64,{encoded_string}"

            matches.append(clothe_info)

    return jsonify(matches), 200  # Return the list of matches as JSON

@app.route('/uploads/<path:filename>')
def serve_uploads(filename):
    return send_from_directory('uploads', filename)

@app.route('/clotheexamples/<path:filename>')
def serve_clotheexamples(filename):
    return send_from_directory('../clotheexamples', filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

def get_file_extension(filename):
    """Get the file extension of an image file."""
    return filename.split('.')[-1].lower()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
