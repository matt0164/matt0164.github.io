import os
import shutil

# Define source and destination paths
source_index = "/Users/mattalevy/PycharmProjects/snow-plots/index.html"
dest_index = "/Users/mattalevy/PycharmProjects/matt0164.github.io/index.html"

source_html_dir = "/Users/mattalevy/PycharmProjects/snow-plots/html"
dest_html_dir = "/Users/mattalevy/PycharmProjects/matt0164.github.io/html"

# Copy index.html
try:
    shutil.copy(source_index, dest_index)
    print(f"Copied {source_index} to {dest_index}")
except Exception as e:
    print(f"Error copying index.html: {e}")

# Ensure the destination html directory exists
if not os.path.exists(dest_html_dir):
    try:
        os.makedirs(dest_html_dir)
        print(f"Created destination directory: {dest_html_dir}")
    except Exception as e:
        print(f"Error creating destination directory: {e}")

# Copy each file from source_html_dir to dest_html_dir
for filename in os.listdir(source_html_dir):
    source_file = os.path.join(source_html_dir, filename)
    dest_file = os.path.join(dest_html_dir, filename)
    if os.path.isfile(source_file):
        try:
            shutil.copy(source_file, dest_file)
            print(f"Copied {source_file} to {dest_file}")
        except Exception as e:
            print(f"Error copying {source_file}: {e}")