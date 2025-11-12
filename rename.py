import os
import subprocess
from datetime import datetime

FOLDER = "_organizations"

def get_last_commit_date():
    # Get last commit date in YYYY-MM-DD format
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cd", "--date=short"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def rename_files(folder):
    commit_date = get_last_commit_date()
    for filename in os.listdir(folder):
        old_path = os.path.join(folder, filename)
        if os.path.isfile(old_path):
            # Skip if already prefixed
            if filename.startswith(commit_date):
                continue
            new_filename = f"{commit_date}_{filename}"
            new_path = os.path.join(folder, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":

    rename_files(FOLDER)
