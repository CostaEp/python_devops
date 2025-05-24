import subprocess

result = subprocess.run(['ls','-la'], capture_output=True, text=True)
print("Output : ", result.stdout)