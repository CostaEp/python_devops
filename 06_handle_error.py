import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ ERROR:")
        print(result.stderr)
    else:
        print("✅ SUCCESS:")
        print(result.stdout)

run_command(["ls", "-la"])
run_command(["cat", "non_existing_file"])