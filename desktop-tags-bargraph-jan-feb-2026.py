import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import requests
import io

# 1. Download Data
urls = {
    "Jan_2026": "https://raw.githubusercontent.com/thunderbird/thunderbird-desktop-metrics-and-reports/refs/heads/main/CONCATENATED_FILES/2026-01-thunderbird-questions.csv",
    "Feb_2026": "https://raw.githubusercontent.com/thunderbird/thunderbird-desktop-metrics-and-reports/refs/heads/main/CONCATENATED_FILES/2026-02-thunderbird-questions.csv"
}

def get_df(url):
    response = requests.get(url)
    return pd.read_csv(io.StringIO(response.text))

df_jan = get_df(urls["Jan_2026"])
df_feb = get_df(urls["Feb_2026"])
print(df_feb)
exit
# 2. Process Top Tags
top_tags = ['windows-11', 'send-and-receive-email', 
            'windows-10','email-and-messaging','customization',
            'passwords-and-sign-in', 'account-management',
            'import-and-export-email', 'linux','connectivity', 'contacts', 'calendar',
            'install', 'events']

#feb_counts = [df_feb[df_feb['tags'] == t]['count'].sum() for t in top_tags]
feb_counts_series = df_feb.groupby('tags')['count'].sum()
print(feb_counts_series)
exit
jan_counts = [df_jan[df_jan['tags'] == t]['count'].sum() for t in top_tags]

# 3. Create Graph
plt.figure(figsize=(10, 6))
x = range(len(top_tags))
plt.bar([i - 0.2 for i in x], dec_counts, width=0.4, label='Jan 2026', color='#2196F3')
plt.bar([i + 0.2 for i in x], jan_counts, width=0.4, label='Feb 2026', color='#FF9800')
plt.xticks(x, top_tags, rotation=45)
plt.ylabel('Absolute Count')
plt.title('Thunderbird Support Tag Volume (Dec 2025 vs Jan 2026)')
plt.legend()
plt.tight_layout()
plt.savefig("comparison_graph.png") # Save graph as image for PDF

# 4. Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Thunderbird Support Metrics Report", ln=True, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, "Monthly Tag Comparison (Absolute Counts)", ln=True)

# Add Table
pdf.set_font("Courier", size=10)
pdf.cell(40, 10, "Tag", 1)
pdf.cell(40, 10, "Jan 2026", 1)
pdf.cell(40, 10, "Feb 2026", 1)
pdf.ln()

for i in range(len(top_tags)):
    pdf.cell(40, 10, top_tags[i], 1)
    pdf.cell(40, 10, str(jan_counts[i]), 1)
    pdf.cell(40, 10, str(feb_counts[i]), 1)
    pdf.ln()

# Add Image
pdf.image("2026-01-2026-02-tags-comparison_graph.png", x=10, y=120, w=190)

pdf.output("2026-01-2026-02-tags-comparison_graph..pdf")
print("PDF 'Thunderbird_Desktop 2026-01-2026-02-tags-comparison_graph.Report.pdf' generated successfully!")
