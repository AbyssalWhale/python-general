# import sys
import subprocess

# Catch what user input to call this file
# Try to call via terminal with: py .\Tools\comdLine.py 123
# if len(sys.argv) == 1:
#     print("USAGE: python3 app.py <password>")
# else:
#     PASSWORD = sys.argv[1]
#     print(f"pass {PASSWORD}")

# Call external programs. Unix: subprocess.run(["ls", "-l"])
RESULT = subprocess.run(["dir"], shell=True)
MESSAGE = "Hello World"
