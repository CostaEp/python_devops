import subprocess

ps = subprocess.Popen(["ps" , "aux"] , stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep", "python"] , stdin=ps.stdout , stdout=subprocess.PIPE , text=True)

ps.stdout.close()

output = grep.communicate()[0]

print(output)

