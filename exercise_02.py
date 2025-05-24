from pathlib import Path
import subprocess
from datetime import datetime

main_dir = Path("Exercise_02")
main_dir.mkdir(exist_ok=True)

(main_dir / ".gitignore").write_text("*.pyc \n__pycache__/\n logs/\n")





# main_dir = Path("Exercise_02")
# main_dir.mkdir(exist_ok=True)

# patterns = ["*.pyc", "__pycache__/", "logs/"]
# timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
# content = f"# Auto-generated .gitignore\n# Created on {timestamp}\n" + "\n".join(patterns) + "\n"

# (main_dir / ".gitignore").write_text(content)

# print(".gitignore created with patterns:")
# print(content)