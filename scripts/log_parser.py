import json
from pathlib import Path


LOG_FILE = Path("data/sample.log")
OUTPUT_FILE = Path("logs/parsed_logs.json")


def parse_logs():
    parsed_logs = []

    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        return

    with open(LOG_FILE, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            log = {
                "date": parts[0],
                "time": parts[1],
                "level": parts[2],
                "message": " ".join(parts[3:])
            }

            parsed_logs.append(log)

    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    with open(OUTPUT_FILE, "w") as output:
        json.dump(parsed_logs, output, indent=4)

    print(f"Successfully parsed {len(parsed_logs)} log entries.")
    print(f"Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    parse_logs()
