import os
import shutil

# Define the directories to search for files
downloads_folder = os.path.join(os.path.expanduser('~'), "Downloads")
# desktop_folder = os.path.join(os.path.expanduser('~'), "Desktop")

# Define the folder names for organizing files
folders = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv', '.json'],
    'Images': ['.jpg', '.jpeg', '.gif', '.png', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.webm'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Code': ['.py', '.java', '.cpp', '.html', '.css', '.js'],
    'Other': []
}

# Function to create folders on the Desktop if they don't exist
def create_folders():
    for folder in folders:
        path = os.path.join(downloads_folder, folder)
        if not os.path.exists(path):
            os.makedirs(path)

# Function to organize files by extension
def organize_files():
    # Create necessary folders
    create_folders()
    
    # List files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)

        # Check which folder the file belongs to
        moved = False
        for folder, extensions in folders.items():
            if extension.lower() in extensions:
                destination_folder = os.path.join(downloads_folder, folder)
                destination_path = os.path.join(destination_folder, filename)

                # Move the file
                shutil.move(file_path, destination_path)
                print(f'Moved {filename} to {folder} folder.')
                moved = True
                break

        # If the file doesn't match any common extension, move it to "Other"
        if not moved:
            destination_folder = os.path.join(downloads_folder, 'Other')
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(file_path, destination_path)
            print(f'Moved {filename} to Other folder.')

if __name__ == "__main__":
    organize_files()