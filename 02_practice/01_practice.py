from pathlib import Path
import subprocess
from datetime import datetime

main_dir = Path("practice")
main_dir.mkdir(exist_ok=True)
main_file = main_dir / "log.txt"

file_name = input("please type name for check file if exist:")
command = ["ls", f"{file_name}"]


result = subprocess.run(command ,capture_output=True , text=True)
print("✅ File found" if result.returncode == 0 else "❌ File not found")
   
with open(main_file , "a") as f:
    f.write(f"{datetime.now()} - file exist: {file_name}\n" if result.returncode == 0
             else f"{datetime.now()} - file : {file_name} is not exist !\n")
