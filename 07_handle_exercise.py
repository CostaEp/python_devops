import subprocess

commands = {
    "System": ["uname", "-a"],
    "Memory": ["vm_stat"],
    "Disk": ["df", "-h"],
    "User": ["whoami"]
}

for title, cmd in commands.items():
    print(f"\n🔹 {title}:")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout if result.returncode == 0 else result.stderr)