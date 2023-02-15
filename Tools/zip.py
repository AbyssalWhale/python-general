from pathlib import Path
from zipfile import ZipFile

# Create and write into
# with ZipFile("Tools/testFiles/ZipTest.zip", "w") as zip:
#     for path in Path("Tools/testFiles").rglob("*.*"):
#         zip.write(path)
#     zip.close()

# Print all files and their info from zip
with ZipFile("Tools/testFiles/ZipTest.zip") as zip:
    print(zip.namelist())

    # Extract file info
    fileInfo = zip.getinfo("Tools/testFiles/testFile.txt")
    print(fileInfo.file_size)
    print(fileInfo.compress_size)

    # To extract all
    zip.extractall("Tools/testFiles/ExtractFromZip")
