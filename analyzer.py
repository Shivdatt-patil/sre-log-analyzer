with open("sample.log", "r") as file:
    logs = file.readlines()

info = 0
warn = 0
error = 0

for line in logs:
    if "INFO" in line:
        info += 1
    elif "WARN" in line:
        warn += 1
    elif "ERROR" in line:
        error += 1

print("=== Log Summary ===")
print(f"INFO: {info}")
print(f"WARN: {warn}")
print(f"ERROR: {error}")
from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

errors = []

for line in logs:
    if line.startswith("ERROR"):
        errors.append(line.strip())

counter = Counter(errors)

print("Top Errors:")
for error, count in counter.items():
    print(f"{error} -> {count}")
