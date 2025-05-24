#!/usr/bin/env python3

from pathlib import Path
from git import Repo
import subprocess
import os

# 1. יצירת מבנה תיקיות
project = Path("project")
(project / "logs").mkdir(parents=True, exist_ok=True)
(project / "src").mkdir(parents=True, exist_ok=True)

# 2. יצירת README
readme = project / "README.md"
readme.write_text("# Project Title\n\nThis is a sample project.")
assert readme.exists(), "README.md not created!"

# 3. יצירת קובץ לוג
log_file = project / "logs" / "setup.log"
log_file.write_text("Project setup completed successfully.")

# 4. מעבר אל תיקיית הפרויקט
os.chdir(project)

# 5. אתחול Git כולל יצירת branch ראשוני
repo = Repo.init(".", initial_branch="main")

# 6. הוספה וקומיט דרך git.command (ולא index)
repo.git.add("README.md")
repo.git.commit("-m", "Initial commit")

# 7. פקודת ls עם פלט
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print("📁 Project structure:\n", result.stdout)

print("✅ Git project fully initialized.")