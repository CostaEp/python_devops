# 🐍 Python DevOps Practice

ברוכים הבאים לריפוזיטורי תרגולים מעשיים במסגרת קורס אינטנסיבי **Python for DevOps**.  
מטרת הריפו: ללמוד תכנות DevOps מודרני באמצעות Python, כולל שימוש בכלים כמו `subprocess`, `GitPython`, `Docker`, עבודה עם מערכת הקבצים ועוד.

---

## 📁 מבנה הפרויקט

```
python_devops/
├── 01_practice/
│   ├── 01_practice.txt
│   ├── exercise_01.py
│   ├── exercise_02.py
│   └── exercise_03.py
├── 02_practice/
│   ├── Dockerfile
│   ├── 01_practice.py
│   ├── 02_practice.py
│   ├── 02_practice.txt
│   ├── 03_practice.py
│   └── practice/log.txt
├── Exercise_01/
│   ├── 01_subfolder/
│   ├── 02_subfolder/
│   ├── 03_subfolder/
│   ├── 04_subfolder/
│   └── 05_subfolder/
├── Exercise_02/
│   └── .gitignore
├── Exercise_03/
│   └── log.txt
├── practice/
│   └── practice/
│       ├── log.txt
│       └── 01.py
├── .gitignore
├── 01_Pathlib.py
├── 02_subprocess.py
├── 03_Gitpython.py
├── 04_summery.py
├── 05_subprocess_adv.py
├── 06_handle_error.py
└── 07_handle_exercise.py
```

---

## 📚 נושאים שנלמדו

### 🧱 יסודות Python (Pathlib)
- יצירת תיקיות וקבצים עם `pathlib`
- כתיבת תוכן ל־`README`, `log.txt`
- אימות קיום קבצים עם `.exists()`

### 🖥️ הרצת פקודות מערכת (subprocess)
- שימוש ב־`subprocess.run`, `Popen`, `PIPE`
- קריאת `stdout`, `stderr`, `returncode`
- טיפול בשגיאות מערכת
- ניתוח פינג עם regex + ממוצעים

### 🐳 Docker
- שימוש ב־Alpine image
- התקנת Python, ping, grep
- הרצת קוד מתוך קונטיינר עם `CMD`

### 🧠 Git אוטומטי (GitPython)
- יצירת ריפוזיטורי `Repo.init`
- ביצוע `commit` אוטומטי
- איתור קבצים לא מנוהלים (untracked)
- מעבר בין סניפים, קריאת היסטוריית commits

---

## 🐳 הפעלת קוד ב־Docker

### 🔨 בנייה:

```bash
docker build -t python-devops -f 02_practice/Dockerfile .
```

### ▶️ הרצה:

```bash
docker run --rm python-devops
```

---

## 🧪 תרגולים נוספים (Hands-on)

| קובץ | תרגול |
|------|--------|
| `exercise_01.py` | יצירת תיקיית פרויקט עם תתי־תיקיות |
| `exercise_02.py` | יצירת `.gitignore` דינאמי |
| `exercise_03.py` | הרצת פקודות ping + ניתוח זמן תגובה |
| `06_handle_error.py` | טיפול בשגיאות מתקדמות |
| `03_Gitpython.py` | כתיבה וקריאה ל־Git עם Python |

---

## ⚙️ דרישות

- Python 3.9+
- Docker (להרצת הסקריפטים בקונטיינר)
- Git
- pip install:
  ```bash
  pip install gitpython
  ```

---

## 🔗 מקורות עזר

- [GitPython Docs](https://gitpython.readthedocs.io)
- [Docker Official Docs](https://docs.docker.com)
- [Python subprocess module](https://docs.python.org/3/library/subprocess.html)

---

## ✍️ תרומות

זהו ריפו אישי לצורכי למידה, אך אשמח לקבל הערות, תיקונים או Pull Requests 💬

---

## 📅 תכנון המשך

- [ ] המשך עבודה עם GitHub API
- [ ] אינטגרציה עם Jenkins / GitHub Actions
- [ ] ניטור עם Prometheus דרך Python
- [ ] מימוש פרויקט סיום: מיני מערכת DevOps חכמה