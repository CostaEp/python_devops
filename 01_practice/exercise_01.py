from pathlib import Path

base_dir = Path("Exercise_01")
for i in range (1, 6):
    (base_dir / f"0{i}_subfolder").mkdir(parents=True, exist_ok=True)




#base_dir = Path("Exercise_01")
#subfolder_names = [f"{i:02}_module" for i in range(1, 6)]

#for name in subfolder_names:
#    folder = base_dir / name
 #   folder.mkdir(parents=True, exist_ok=True)
    
 #  # יצירת קובץ README קטן בכל תיקייה
 #   readme = folder / "README.md"
 #   readme.write_text(f"# {name}\n\nThis is the {name} module.")