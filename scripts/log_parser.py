import json
import re


INPUT_FILE = "data/sample.log"
OUTPUT_FILE = "logs/parsed_logs.json"


def detect_level(message):

    message = message.lower()

    if "failed" in message or "error" in message:
        return "ERROR"

    elif "critical" in message or "fatal" in message:
        return "CRITICAL"

    elif "warning" in message:
        return "WARNING"

    else:
        return "INFO"



def parse_logs():

    logs = []


    with open(INPUT_FILE,"r") as file:

        for line in file:

            level = detect_level(line)


            log = {

                "level": level,

                "message": line.strip()

            }


            logs.append(log)



    with open(
        OUTPUT_FILE,
        "w"
    ) as json_file:

        json.dump(
            logs,
            json_file,
            indent=4
        )


    print("Log parsing completed")



if __name__=="__main__":
    parse_logs()
