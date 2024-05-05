from config import db
from math import sqrt

class Clothe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filePath = db.Column(db.String(255), nullable=False)
    palette = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'palette': self.palette,
            'filePath': self.filePath
        }

    def hex_to_rgb(self, hex_code):
        """Convert hex color code to an RGB tuple."""
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    def color_distance(self, rgb1, rgb2):
        return sqrt(sum((c1 - c2) ** 2 for c1, c2 in zip(rgb1, rgb2)))

    def match_color(self, target_hex, tolerance=5):
        target_rgb = self.hex_to_rgb(target_hex)
        palette_array = self.palette.split(",")
        for hex_code in palette_array:
            color_rgb = self.hex_to_rgb(hex_code)
            if self.color_distance(target_rgb, color_rgb) <= tolerance:
                return True
        return False