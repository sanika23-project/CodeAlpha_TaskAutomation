
import os
import shutil
from pathlib import Path

# Get project directory
base_folder = Path(__file__).resolve().parent

# Define folders
source_folder = base_folder / "source_images"
destination_folder = base_folder / "organized_images"


# Function to create folders
def create_folders():
    os.makedirs(source_folder, exist_ok=True)
    os.makedirs(destination_folder, exist_ok=True)


# Function to move image files
def organize_files():
    moved_count = 0
    supported_extensions = [".jpg", ".jpeg"]

    print("\nStarting File Organizer...")
    print("--------------------------------")

    for file in source_folder.iterdir():

        if file.is_file() and file.suffix.lower() in supported_extensions:

            destination = destination_folder / file.name

            # Handle duplicate filenames
            counter = 1

            while destination.exists():
                new_name = f"{file.stem}_{counter}{file.suffix}"
                destination = destination_folder / new_name
                counter += 1

            shutil.move(str(file), str(destination))

            print(f"Moved: {file.name} -> {destination.name}")
            moved_count += 1

    print("--------------------------------")

    if moved_count == 0:
        print("No JPG or JPEG files found.")

    print(f"Total image files moved: {moved_count}")


# Main function
def main():
    print("================================")
    print("       PYTHON FILE ORGANIZER")
    print("================================")

    create_folders()
    organize_files()

    print("\nFile organization completed!")


if __name__ == "__main__":
    main()
