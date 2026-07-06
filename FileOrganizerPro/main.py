# The File Organizer 
# Imported Libraries
from pathlib import Path
import shutil

# The Dictionary to organize the data.

media_organization_map = {"Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".tiff", ".tif", ".bmp"], "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".odt"], "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"], "Audio": [".mp3", ".wav", ".flac", ".aac", ".m4a"], "Archives": [".zip", ".rar", ".7z", ".tar", ".iso"], "Code": [".py", ".js", ".html", ".css", ".ts", ".cpp", ".c", ".java"], "Others": []}

# Function the takes a file, checks for its extension and returns the correct folder name.

def get_category(filename):
    # Get the extension from the filename
    extension = Path(filename).suffix

    # Loop through the dictionary 
    for category, extensions in media_organization_map.items():
        # If extension matches return the category
        if extension in extensions:
            return category
    return "Others"

# Fuction to organize the folders

def organize_folder(folder_path):
    folder = Path(folder_path)  # convert string to Path

    # Dictionary that counts the file category been moved
    category_counts = {}
    
    for file_path in folder.iterdir():
        # Step 1: Skip folders, only process files
        if not file_path.is_file():
            continue
        
        # Step 2: Get the category name (your pseudocode step 1)
        category = get_category(file_path.name)
        
        # Step 3: Build the destination folder path
        dest_folder = folder / category
        
        # Step 4: Create the folder if missing (your step 3)
        dest_folder.mkdir(exist_ok=True)
        
        # Step 5: Build full destination file path
        dest_file = dest_folder / file_path.name

        try:
            # Step 6: Move the file (your step 4)
            # Print first, then move!
            print(f"Moving {file_path.name} → {category}/")
            shutil.move(file_path, dest_file)

            category_counts[category] = category_counts.get(category, 0) + 1
        except Exception as e:
            print(f"❌ Error moving {file_path.name}: {e}")

    # NEW: Print summary report
    print("\n" + "=" * 40)
    print("📊 ORGANIZATION COMPLETE!")
    print("=" * 40)
    total = sum(category_counts.values())
    print(f"✅ Total files moved: {total}")
    print(f"📁 Categories used: {len(category_counts)}\n")
    print("Breakdown:")
    for cat, count in category_counts.items():
        print(f"   • {cat}: {count} file(s)")
    print("=" * 40)

organize_folder("test_folder")