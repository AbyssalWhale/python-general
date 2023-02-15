from pathlib import Path
from time import ctime
import shutil

path = Path("Tools/testFiles/testFile.txt")

# Check if exists
print(path.exists())

# Rename
# path.rename("Tools/testFile.txt")

# Delete
# path.unlink()

# Info about file
print(path.stat())

# File creation time
print(ctime(path.stat().st_ctime))

# Read Contnet
print(path.read_text())

# Write
path.write_text("extra text")

# Open File
with open(path, "r") as file:
    print(file.read())

fileCopy = Path("Tools/testFiles/Copy.txt")
shutil.copy(path, fileCopy)
print(f"file copy text: {fileCopy.read_text()}")
