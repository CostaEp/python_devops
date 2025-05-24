from pathlib import Path

base_dir = Path("Exercise_01")
for i in range (1, 6):
    (base_dir / f"0{i}_subfolder").mkdir(parents=True, exist_ok=True)

