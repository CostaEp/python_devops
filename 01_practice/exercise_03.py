from pathlib import Path
import subprocess

main_dir = Path("Exercise_03")
main_dir.mkdir(exist_ok=True)

log_file = main_dir / "log.txt"
log_file.write_text("")

# run uname -a command and write to log_file
result_01 = subprocess.run(["uname", "-a" ], capture_output=True, text=True)

with open(log_file, "a") as f:
    f.write(result_01.stdout)

# run df -h command and append to log_file
result_02 = subprocess.run(["df","-h"],  capture_output=True, text=True)  

with open(log_file, "a") as f:
    f.write(result_02.stdout)

# append with shell command
subprocess.run(f"ls -la >> {log_file}", shell=True)


# print cat from log file
result_03 = subprocess.run([f"cat {log_file}"], shell=True, capture_output=True, text=True)
print(result_03.stdout)


# main_dir = Path("Exercise_03")
# main_dir.mkdir(exist_ok=True)

# log_file = main_dir / "log.txt"

# # כתיבת כותרת עם תאריך
# log_file.write_text(f"# System Log – {datetime.now()}\n\n")

# # רשימת פקודות להרצה
# commands = [
#     ("uname -a", ["uname", "-a"]),
#     ("df -h", ["df", "-h"]),
#     ("ls -la", ["ls", "-la"])
# ]

# # הרצת כל פקודה וכתיבת הפלט
# for title, cmd in commands:
#     log_file.write_text(f"\n\n## {title}\n", append=True) if hasattr(log_file, 'append') else None
#     result = subprocess.run(cmd, capture_output=True, text=True)
#     with open(log_file, "a") as f:
#         f.write(result.stdout)

# # הדפסת הלוג למסך
# print(log_file.read_text())