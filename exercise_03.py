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


