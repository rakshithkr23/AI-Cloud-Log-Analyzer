import json


def detect_alerts():

    with open(
        "logs/parsed_logs.json"
    ) as file:

        logs=json.load(file)


    alerts=[]


    for log in logs:

        if log["level"] in [
            "ERROR",
            "CRITICAL"
        ]:

            alerts.append(log)


    return alerts
