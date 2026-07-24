# File Organizer

## Overview

File Organizer is a terminal-based Python application that automatically organizes files inside a selected folder based on their file extensions. It creates folders for different file categories and moves files into their respective folders, making directories clean and organized.

---

## Features

* Organizes files based on file extensions.
* Automatically creates category folders if they do not exist.
* Moves files into the appropriate folders.
* Displays a summary of the organization process.
* Skips hidden files.
* Ignores existing folders while organizing.
* Handles invalid folder paths and permission errors gracefully.
* Simple menu-driven interface.

---

## File Categories

* **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg`
* **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv`
* **Videos:** `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`
* **Audio:** `.mp3`, `.wav`, `.aac`, `.ogg`, `.flac`
* **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
* **Others:** Any unsupported or unknown file type.

---

## Technologies Used

* Python 3
* `os` module
* `shutil` module

---

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this project.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python file_organizer.py
```

---

## Usage

When the program starts, the following menu is displayed:

```text
========== File Organizer ==========
1. Organize Folder
2. View Summary
3. Exit
```

Choose **Option 1** and enter the full path of the folder you want to organize.

Example (Windows):

```text
C:\Users\YourName\Downloads
```

Example (macOS/Linux):

```text
/home/username/Downloads
```

After organizing, choose **Option 2** to view a summary of the files moved.

---

## Example Output

```text
========== File Organizer ==========
1. Organize Folder
2. View Summary
3. Exit

Enter your choice: 1
Enter folder path: C:\Users\John\Downloads

Folder organized successfully!

========== Summary ==========
Images: 8 file(s)
Documents: 5 file(s)
Videos: 2 file(s)
Audio: 3 file(s)
Archives: 1 file(s)
Others: 4 file(s)

Total Files Moved: 23
```

---

## Python Concepts Used

* Variables
* User Input
* Conditional Statements
* Loops
* Functions
* Dictionaries
* Exception Handling
* File and Directory Management
* Modules (`os` and `shutil`)

---

## Future Improvements

* Organize files into subfolders based on extension.
* Add an undo feature.
* Allow custom file categories.
* Generate a log file after each organization.
* Add a graphical user interface (GUI).

---

## License

This project is for educational purposes and can be modified and used for learning.
