from pathlib import Path
log_file = Path("/var/log/syslog")
if log_file.exists():
    with log_file.open("r") as file:
        line = file.readlines()
    print(f"Total number of lines : {len(line)}")

    print("\nfirst 5 lines")
    for lines in line[:5]:
        print(lines,end = '')
    print("\nlast 5 lines")
    for lines in line[-5:]:
        print(lines,end='')
else:
    print(f"File not found {log_file}")
