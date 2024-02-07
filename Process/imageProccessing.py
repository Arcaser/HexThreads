from PIL import Image
from io import BytesIO
import base64

class ImageProcessing:
    def __init__(self):
        pass

    def image2string(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                # Read the image file as bytes
                image_bytes = image_file.read()
                # Encode the image bytes as base64
                base64_string = base64.b64encode(image_bytes).decode("utf-8")
                return base64_string
        except FileNotFoundError:
            print(f"Error: File '{image_path}' not found.")
            return None
        
    def string2image(self, base64_string):
        try:
            # Decode the base64 string to bytes
            image_bytes = base64.b64decode(base64_string)
            # Create a PIL Image object from the bytes
            image = Image.open(BytesIO(image_bytes))
            return image
        except Exception as e:
            print(f"Error decoding image: {e}")
            return None

# Example usage
image_processor = ImageProcessing()
image_path = "test.jpg"
image_string = image_processor.image2string(image_path)
if image_string is not None:
    print("Base64 String:", image_string)
    image = image_processor.string2image(image_string)
    if image is not None:
        image.show()