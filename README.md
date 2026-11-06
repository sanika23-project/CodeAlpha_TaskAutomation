# Python File Organizer

## Project Description
Python File Organizer is an automation project developed using Python. It automatically identifies and moves JPG and JPEG image files from a source folder to a destination folder.

The project reduces manual file organization and demonstrates the use of Python automation and file handling.

## Features
- Automatically identifies JPG and JPEG files.
- Supports uppercase and lowercase extensions.
- Moves images into a separate destination folder.
- Creates folders automatically if they do not exist.
- Handles duplicate filenames without overwriting existing files.
- Displays the total number of files moved.

## Technologies Used
- Python
- os module
- shutil module
- pathlib module

## Project Structure

```text
CodeAlpha_TaskAutomation/
│
├── file_organizer.py
├── source_images/
├── organized_images/
└── README.md
```

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Add JPG or JPEG images to the `source_images` folder.
5. Open the terminal.
6. Execute:

```bash
python file_organizer.py
```

## Sample Output

```text
================================
       PYTHON FILE ORGANIZER
================================

Starting File Organizer...
--------------------------------
Moved: photo1.jpg -> photo1.jpg
Moved: photo2.jpeg -> photo2.jpeg
--------------------------------
Total image files moved: 2

File organization completed!
```

## Python Concepts Used
- Functions
- Loops
- Conditional statements
- File handling
- Directory management
- Exception-free file movement with duplicate checks

## Internship
Developed as part of the CodeAlpha Python Programming Internship.

## Author
Sanika Mali