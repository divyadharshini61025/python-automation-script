import os
import shutil

source = "source_folder"
dest = "destination_folder"

if not os.path.exists(dest):
    os.makedirs(dest)

for file in os.listdir(source):
    if file.endswith('.jpg'):
        shutil.move(os.path.join(source, file), os.path.join(dest, file))

print("All .jpg files moved successfully.")
