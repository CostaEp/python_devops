# import subprocess
# import re



# ping  = subprocess.Popen(["ping" , "-c" , "3" ,"8.8.8.8"] , stdout=subprocess.PIPE)
# grep = subprocess.Popen(["grep" , "time"] , stdin=ping.stdout , stdout=subprocess.PIPE , text=True)

# ping.stdout.close()
# ping_out = grep.communicate()


# for i in ping_out:
#     if i != None:
#         print("============================================================")
#         print(i)
#         print("\n")
#         print("============================================================")
#     else:
#         print("there is no error")
    
# print("============================================================\n")

# match = re.findall(r"time=([\d.]+)" , ping_out[0]) 
# for i in match:
#     print(f"time run by order: {i} ms\n")



import subprocess
import re

# הרצת פקודת ping דרך pipe ל-grep
ping = subprocess.Popen(["ping", "-c", "3", "8.8.8.8"], stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep", "time"], stdin=ping.stdout, stdout=subprocess.PIPE, text=True)

ping.stdout.close()
stdout, stderr = grep.communicate()

# הדפסת פלט אם קיים
if stdout:
    print("\n======================= Ping Output =======================")
    print(stdout.strip())
    print("============================================================\n")
else:
    print("❌ No output from grep. Possibly no 'time=' lines found.")

# ניתוח זמן התגובה עם regex
match = re.findall(r"time=([\d.]+)", stdout if stdout else "")
if match:
    print("🔎 Times found:")
    for i, t in enumerate(match, 1):
        print(f"time run {i}: {t} ms")

    # חישוב ממוצע, מקסימום ומינימום
    times = [float(t) for t in match]
    avg = sum(times) / len(times)
    print(f"\n⏱️ AVG: {avg:.2f} ms | MIN: {min(times):.2f} ms | MAX: {max(times):.2f} ms")
else:
    print("❌ No times matched.")
