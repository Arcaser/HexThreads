from flask import Flask, render_template, request, redirect, url_for
from App.Controller.MongoLoader import loader  
from App.Controller.MongoReader import reader
from App.Controller.upload import Upload


app = Flask(__name__)


# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "mongodb+srv://Arcaser:Gb4Y1PWqhXnwY2jh@hexthreads.mw1ibnw.mongodb.net/?retryWrites=true&w=majority"
db_name = "hexThreads"



# Make a mongo main controller because this is starting to get messy
# Initialize your loader instance correctly
upload = Upload(db_uri, db_name)
read = reader(db_uri, db_name)

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

# Define the upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        print('No file part')
        return redirect(url_for('home'))
    file = request.files['image']
    if file.filename == '':
        print('No selected file')
        return redirect(url_for('home'))
    fileName = file.filename
    valid = upload.allowed_file(fileName)
    if file and valid:

        if upload.upload_file(file):
            print('File uploaded successfully')
            # Redirect or process as needed
        else:
            print('File upload failed')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()

