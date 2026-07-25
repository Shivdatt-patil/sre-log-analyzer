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

from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

info = 0
warn = 0
error = 0

errors = []

for line in logs:
    if "INFO" in line:
        info += 1
    elif "WARN" in line:
        warn += 1
    elif "ERROR" in line:
        error += 1
        errors.append(line.strip())

top_errors = Counter(errors)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>SRE Log Report</title>
</head>
<body>
    <h1>SRE Log Analyzer Report</h1>

    <h2>Summary</h2>

    <p>INFO: {info}</p>
    <p>WARN: {warn}</p>
    <p>ERROR: {error}</p>

    <h2>Top Errors</h2>
"""

for err, count in top_errors.items():
    html += f"<p>{err} : {count}</p>"

html += """
</body>
</html>
"""

with open("report.html", "w") as report:
    report.write(html)

print("report.html generated successfully")
