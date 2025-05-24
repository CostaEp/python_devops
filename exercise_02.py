from pathlib import Path
import subprocess

main_dir = Path("Exercise_02")
main_dir.mkdir(exist_ok=True)

(main_dir / ".gitignore").write_text("*.pyc \n__pycache__/\n logs/\n")