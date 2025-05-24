from pathlib import Path
import subprocess
from datetime import datetime


log_dir = Path("practice")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "log.txt"
commands = [
    ("ls -ls",["ls","-la"])
    ,("ping -c 4",["ping","-c","4","127.0.0.1"])
    ,("uname -a",["uname",])
    ,("whoami",["whoami"])
    ]

log_file.write_text(f"========LOG========\nlog file - time: {datetime.now()}\n===================\n")

for title , cmd in commands:
    with open(log_file, "a") as f:
        f.write("-----------------------\n")
        f.write(f"Command title: {title} \n")
        f.write("-----------------------\n")

        result = subprocess.run(cmd, capture_output=True ,text=True)
        f.write(result.stdout)

