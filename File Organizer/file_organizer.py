import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"]
}

summary = {}
total_files_moved = 0


def get_category(extension):
    """Return the category based on file extension."""
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_folder(folder_path):
    """Organize files into category folders."""

    global summary
    global total_files_moved

    summary = {}
    total_files_moved = 0

    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        items = os.listdir(folder_path)

        for item in items:
            source_path = os.path.join(folder_path, item)

            # Ignore folders
            if os.path.isdir(source_path):
                continue

            # Skip hidden files
            if item.startswith("."):
                continue

            _, extension = os.path.splitext(item)
            category = get_category(extension)

            destination_folder = os.path.join(folder_path, category)

            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            destination_path = os.path.join(destination_folder, item)

            shutil.move(source_path, destination_path)

            summary[category] = summary.get(category, 0) + 1
            total_files_moved += 1

        print("\nFolder organized successfully!")

    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("An error occurred:", e)


def view_summary():
    """Display organization summary."""

    if total_files_moved == 0:
        print("\nNo files have been organized yet.")
        return

    print("\n========== Summary ==========")

    for category, count in summary.items():
        print(f"{category}: {count} file(s)")

    print("-----------------------------")
    print(f"Total Files Moved: {total_files_moved}")


def main():
    while True:
        print("\n========== File Organizer ==========")
        print("1. Organize Folder")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            folder = input("Enter folder path: ").strip()
            organize_folder(folder)

        elif choice == "2":
            view_summary()

        elif choice == "3":
            print("Thank you for using File Organizer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()