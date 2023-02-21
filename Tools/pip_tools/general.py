import subprocess
import requests

# Install and read all available packages
subprocess.run("pip3 install requests==2.28.2")
subprocess.run("pip3 list")

# Usage installed package
response = requests.get("https://www.google.com/")
print(response)
