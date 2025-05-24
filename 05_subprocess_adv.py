import subprocess

# Example of running a command and capturing its output
# result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# print(result.stdout)


# Example of capturing output from a command that fails
result = subprocess.run(["ls", "error"], capture_output=True, text=True)
print("stderr:", result.stderr)
print("exit code:", result.returncode)
print("========================================")

# Example of running a command with grep and capturing its output
result = subprocess.run(["grep", "hello"], input="hello world", capture_output=True, text=True)
print(result.stdout)
print("========================================")

# Exmple of code that runs a command and captures its output line by line
process = subprocess.Popen(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE, text=True)
for line in process.stdout:
    print(line.strip())
print("========================================")