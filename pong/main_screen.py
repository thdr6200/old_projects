import os
import json

current_directory = os.getcwd()
with open("settings.json", 'r') as file:
    settings = json.load(file)

print(settings)