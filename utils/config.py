import json

def load_settings():
    with open("config.json") as file:
        content = file.read()
        settings = json.loads(content)
        resolution = settings["resolution"].split(";")
        return (int(resolution[0]), int(resolution[1]))