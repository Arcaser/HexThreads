import os
from werkzeug.utils import secure_filename
from App.Controller.MongoLoader import loader
from App.Controller.converter import converter


class Upload:
    path = "App/img"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    def __init__(self, uri, db_name):
        self.loader = loader(uri, db_name)
        self.processor = converter()

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
    
    def upload_file(self, file):
        if file and self.allowed_file(file.filename):
            #sanitize the filename
            filename = secure_filename(file.filename)
            save_path = os.path.join(self.path, filename)
            # Ensure the directory exists
            os.makedirs(self.path, exist_ok=True)
            # Save the file
            file.save(save_path)


            # Process the image and load into MongoDB
            try:
                self.loader.insert_cloth_nonStore(self.loader.generate_unique_id(), file)
                return True
            except Exception as e:
                print(f"An error occurred: {e}")
                
                return False
        return False

    