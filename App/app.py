from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from Mongo.MongoLoader import loader  
from Mongo.MongoReader import reader

app = Flask(__name__)

UPLOAD_FOLDER = 'App\img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "Look at discord"
db_name = "hexThreads"

# Initialize your loader instance correctly
load = loader(db_uri, db_name)
read = reader(db_uri, db_name)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

