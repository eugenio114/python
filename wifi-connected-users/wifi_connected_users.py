import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = [ls[x] for x in range(len(ls)) if x % 5 == 0]
print(ssids)