import os

folder_path = "."

files = os.listdir(folder_path)

count = 1

for file in files:
    if file.endswith(".py") or file.startswith("file_"):
        continue
    
    old_path = os.path.join(folder_path, file)
    
    name, ext = os.path.splitext(file)
    new_name = f"file_{count}{ext}"
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    
    count += 1

print("Files renamed successfully!")