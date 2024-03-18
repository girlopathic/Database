import pandas as pd

# Load your Excel database
DATABASE_PATH = 'General-Archival-Database.xlsx'
db = pd.read_excel(DATABASE_PATH)

# Convert the entire DataFrame to HTML
html_content = db.to_html()

# Save to an HTML file
with open('index.html', 'w') as f:
    f.write(html_content)
