import json
import module
import time

rawjson = """
{
  "modules": [
    { "type": "timeTrigger", "time": "22:16" },
    { "type": "wether", "region": "Schweiz"},
    { "type": "print" }
  ]
}
"""

parsedJson = json.loads(rawjson)

modules = []

for jsons in parsedJson["modules"]:
    modules.append(jsons)

count = 0

while True:
    if count == len(modules):
        count = 0
        print("Ende")
        break  # Das hier muss weg soballt man es neu machen will

    rsp = module.module.callModule(modules[count]["type"], modules[count])

    if rsp == None:
        count = 0
    elif rsp == "No module like that":
        print("Theres no Module: " + modules[count]["type"])
        count = 0
        break

    elif rsp:
        count += 1
    else:

        print("resp war false")
        count = 0
    time.sleep(1)


"""
So sollte ein einfaches Json aussehen:


Einfaches beispiel:    
{
  "modules": [
    { "type": "timeTrigger", "time": "18:00" },
    { "type": "wetter", "region": "Schweiz Baden" },
    { "type": "Print"}
  ]
}
"""
