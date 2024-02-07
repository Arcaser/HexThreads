from flask import Flask, render_template, request, redirect, url_for
from Mongo.MongoLoader import loader  # Make sure this import matches your file and class name

app = Flask(__name__)

# Use environment variables or another secure method to store and retrieve your credentials
db_uri = "your_mongodb_connection_string"
db_name = "hexThreads"

# Initialize your loader instance correctly
l = loader(db_uri, db_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_cloth_form')
def add_cloth_form():
    return render_template('add_cloth.html')

@app.route('/add_cloth', methods=['GET', 'POST'])
def add_cloth():
    if request.method == 'POST':
        data = request.form
        l.insert_cloth(data['id'], data['store'], data['image'])
        return redirect(url_for('add_cloth_form'))
    else:
        return render_template('add_cloth.html')

if __name__ == "__main__":
    app.run()