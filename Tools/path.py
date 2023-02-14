import sys
from pathlib import Path


def test_func():
    pass


# Current file path + all python pathes
print(sys.path)

# Absolute path for windows
# r is like $ in c#
Path(r"D:\Repo\O\bio\cc-automation-tests-core\ApplicationFramework")
Path("\Repo\O\bio\cc-automation-tests-core")

# Current Folder
Path()

# Relative path for subfolder
Path("Modules/basics.py")

# Combine pathes
PATH_COMBINED = Path() / Path("Modules/basics.py")

# Home directory of current user
Path.home()

#To check file
PATH_COMBINED.exists()
PATH_COMBINED.is_file()
PATH_COMBINED.is_dir()

#Print only file/folder name with extenstion
print(PATH_COMBINED.name)

#Print only file/folder name without extenstion
print(PATH_COMBINED.stem)