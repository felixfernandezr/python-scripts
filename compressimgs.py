from PIL import Image  # python -m pip install Pillow
import os

downloadsFolder = "C:/Users/felix/Desktop/compressTest"  # Use raw string

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(filename)  # Fixed typo
        if extension.lower() in [".jpg", ".jpeg", ".png"]:  # Check file extensions
            file_path = os.path.join(downloadsFolder, filename)  # Use os.path.join
            picture = Image.open(file_path)
            compressed_path = os.path.join(downloadsFolder, f"compressed_{filename}")
            picture.save(compressed_path, optimize=True, quality=60)
            