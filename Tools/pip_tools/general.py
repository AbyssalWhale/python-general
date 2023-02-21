import subprocess
import requests

subprocess.run("pip3 install requests==2.28.2")
subprocess.run("pip3 list")


response = requests.get("https://www.google.com/")
print(response)
