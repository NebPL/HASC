from datetime import datetime
import json


class module:
    modules = []
    nextjson = ""
    nextiter = 1

    def __init__(self, typeName, triggerFunction) -> None:
        module.modules.append((typeName, triggerFunction))

    @classmethod
    def callModule(cls, typename, json):
        for itermodule in module.modules:
            if itermodule[0] == typename:
                returnval = itermodule[1](json, cls.nextjson)

                if returnval == None:
                    return None

                cls.nextiter = returnval[1]
                cls.nextjson = returnval[2]
                return returnval[0]
        return "No module like that"


""" 
{
  "modules": [
    { "type": "timeTrigger", "time": 18:00 },
    { "type": "UpperCase" },
    { "type": "Print" }
  ]
}
"""


def timeTrigger(data, previous):
    # Aktuelle Uhrzeit im Format HH:MM
    now = datetime.now().strftime("%H:%M")

    # Uhrzeit aus JSON, z. B. "18:00"
    target_time = data.get("time")

    if target_time == now:
        return [True, 1, ""]
    else:
        return [False, 1, ""]


module("timeTrigger", timeTrigger)


def wether(data, previous):

    return [True, 1, """{"jsons":[
                    {"tempuratur": "10"}         
                   ]}"""]


module("wether", wether)


def moduleprint(data, previous):

    parsedPrevious = json.loads(previous)

    print(parsedPrevious["jsons"][0]["tempuratur"])

    return None


module("print", moduleprint)
