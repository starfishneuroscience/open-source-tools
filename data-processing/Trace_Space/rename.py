import os
import re

def rename_items_with_pattern(root_path):
    pattern = re.compile(r'^(W)(\d{3})(.*\.jpg)$')  # Matches W followed by 3 digits, exactly

    for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
        # Rename files
        for filename in filenames:
            print(filename)
            match = pattern.match(filename)
            if match:
                new_filename = f"{match.group(1)}-{match.group(2)}{match.group(3)}"
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, new_filename)
                if os.path.exists(old_file):
                    os.rename(old_file, new_file)
                    print(f"Renamed file: {old_file} -> {new_file}")
# Run from current directory
rename_items_with_pattern(os.getcwd())
