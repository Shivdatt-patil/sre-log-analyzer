from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

info = 0
warn = 0
error = 0
errors = []

for line in logs:
    line = line.strip()

    if line.startswith("INFO"):
        info += 1

    elif line.startswith("WARN"):
        warn += 1

    elif line.startswith("ERROR"):
        error += 1
        errors.append(line)

total_logs = len(logs)

top_errors = Counter(errors)

# Generate Report

report_html = f"""
<!DOCTYPE html>
<html>
<head>
<title>SRE Log Report</title>
<style>
body {{
    font-family: Arial;
    margin: 40px;
}}

.error {{
    color: red;
}}

.warn {{
    color: orange;
}}

.info {{
    color: green;
}}
</style>
</head>
<body>

<h1>SRE Log Analyzer Report</h1>

<h2>Summary</h2>

<p class="info">INFO: {info}</p>
<p class="warn">WARN: {warn}</p>
<p class="error">ERROR: {error}</p>

<h2>Top Errors</h2>
"""

for err, count in top_errors.items():
    report_html += f"<p>{err} : {count}</p>"

report_html += """
</body>
</html>
"""

with open("report.html", "w") as report:
    report.write(report_html)

# Generate Dashboard

dashboard_html = f"""
<!DOCTYPE html>
<html>
<head>
<title>SRE Dashboard</title>

<style>

body {{
    background-color: #121212;
    color: white;
    font-family: Arial, sans-serif;
    margin: 40px;
}}

h1 {{
    text-align: center;
}}

.container {{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    justify-content: center;
}}

.card {{
    background-color: #1e1e1e;
    border-radius: 12px;
    padding: 20px;
    width: 220px;
    text-align: center;
}}

.total {{
    border-left: 5px solid dodgerblue;
}}

.errors {{
    border-left: 5px solid red;
}}

.warnings {{
    border-left: 5px solid orange;
}}

.info {{
    border-left: 5px solid green;
}}

</style>

</head>

<body>

<h1>SRE Monitoring Dashboard</h1>

<div class="container">

<div class="card total">
<h3>Total Logs</h3>
<p>{total_logs}</p>
</div>

<div class="card errors">
<h3>Errors</h3>
<p>{error}</p>
</div>

<div class="card warnings">
<h3>Warnings</h3>
<p>{warn}</p>
</div>

<div class="card info">
<h3>Info Logs</h3>
<p>{info}</p>
</div>

</div>

<h2>Top Errors</h2>
"""

for err, count in top_errors.items():
    dashboard_html += f"<p>{err} : {count}</p>"

dashboard_html += """
</body>
</html>
"""

with open("dashboard.html", "w") as dashboard:
    dashboard.write(dashboard_html)

print("Dashboard Generated Successfully")
print("Report Generated Successfully")
