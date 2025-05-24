from pathlib import Path

base_dir = Path("devops_lab")
base_dir.mkdir(exist_ok=True)

log_path = base_dir / "log.txt"
log_path.write_text("Start log")
print("Log written to:", log_path)