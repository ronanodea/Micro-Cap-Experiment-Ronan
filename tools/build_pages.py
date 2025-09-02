import os, csv, glob, datetime

# Look in "Scripts and CSV Files" folder for the newest CSV
csvs = glob.glob("Scripts and CSV Files/*.csv")
if not csvs:
    os.makedirs("docs", exist_ok=True)
    with open("docs/index.html", "w") as f:
        f.write("<h1>No CSVs found yet</h1>")
    raise SystemExit()

latest = max(csvs, key=os.path.getmtime)
rows = []
with open(latest, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

# Make a very simple HTML page
updated = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
html = f"<h1>Portfolio Dashboard</h1><p>Updated: {updated}</p><p>File: {latest}</p><table border=1>"

for r in rows[:50]:  # show first 50 rows
    html += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
html += "</table>"

# Save page to docs/index.html
os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)
