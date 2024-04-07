import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from colorthief import ColorThief

# set of supported file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
CORS(app)

# function that checks whether a file has the supported extensions (png, jpg, jpeg)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
        palette = ct.get_palette(color_count=size)
        for i in palette:
            hex_code = '#{:02x}{:02x}{:02x}'.format(*i)
            palettes.append(hex_code)
            json_palettes = json.dumps(palettes)
        #json_palettes = list(map(lambda x: json.dumps(x), palettes))
        return json_palettes

# this is what starts/runs the flask server
if __name__ == '__main__':
    app.run(debug=True)