from PIL import Image  # python -m pip install Pillow
import os

downloadsFolder = "C:/Users/Username/Desktop/compressTest" 

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(filename) 
        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            file_path = os.path.join(downloadsFolder, filename) 
            picture = Image.open(file_path)
            compressed_path = os.path.join(downloadsFolder, f"compressed_{filename}")
            picture.save(compressed_path, optimize=True, quality=60)
            