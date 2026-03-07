import pandas as pd

# ---------------------------------------------------------
# Step 1: Simulate Test Execution Data
# In reality, you would read this from your test framework:
# df = pd.read_csv('daily_regression_results.csv')
# ---------------------------------------------------------
dummy_data = {
    'TestCase_ID': [
        'TC_RRC_Setup_01', 'TC_RRC_Setup_01', 'TC_RRC_Setup_01', 'TC_RRC_Setup_01',
        'TC_Handover_Inter_CU', 'TC_Handover_Inter_CU', 'TC_Handover_Inter_CU', 'TC_Handover_Inter_CU',
        'TC_NGAP_Paging_03', 'TC_NGAP_Paging_03', 'TC_NGAP_Paging_03', 'TC_NGAP_Paging_03'
    ],
    'gNB_Build': [
        'Build_101', 'Build_102', 'Build_103', 'Build_104',
        'Build_101', 'Build_102', 'Build_103', 'Build_104',
        'Build_101', 'Build_102', 'Build_103', 'Build_104'
    ],
    'Status': [
        'Pass', 'Pass', 'Pass', 'Pass',         # Stable Test
        'Pass', 'Fail', 'Pass', 'Fail',         # Flaky Test (Simulator issue?)
        'Pass', 'Pass', 'Fail', 'Fail'          # Hard Bug introduced in Build 103
    ]
}

# Load data into a Pandas DataFrame
df = pd.DataFrame(dummy_data)

# ---------------------------------------------------------
# Step 2: Create the Heatmap Grid (Pivot Table)
# Rows = Test Cases | Columns = Builds | Values = Status
# ---------------------------------------------------------
heatmap_df = df.pivot(index='TestCase_ID', columns='gNB_Build', values='Status')

# ---------------------------------------------------------
# Step 3: Calculate the "Flakiness Score"
# ---------------------------------------------------------
def evaluate_flakiness(row):
    statuses = row.dropna().unique()
    if 'Pass' in statuses and 'Fail' in statuses:
        # If it flipped back and forth, it's flaky
        if list(row).count('Pass') > 0 and list(row).count('Fail') > 0 and row.iloc[-1] == 'Pass':
            return 'High (Flaky)'
        # If it was passing, but failed recently and stayed failed, it's a real bug
        return 'Recent Hard Fail'
    elif 'Fail' in statuses:
        return 'Persistent Fail'
    return 'Stable'

# Add the flakiness status as a new column at the end
heatmap_df['Diagnosis'] = heatmap_df.apply(evaluate_flakiness, axis=1)

# ---------------------------------------------------------
# Step 4: Apply Color Coding to the HTML
# ---------------------------------------------------------
def color_cells(val):
    color = ''
    if val == 'Pass': 
        color = '#c8e6c9' # Light Green
    elif val == 'Fail': 
        color = '#ffcdd2' # Light Red
    elif val == 'High (Flaky)': 
        color = '#fff9c4' # Light Yellow
    elif val == 'Recent Hard Fail' or val == 'Persistent Fail': 
        color = '#ff8a80' # Dark Red
    elif val == 'Stable':
        color = '#e2f0cb' # Very Light Green
    
    return f'background-color: {color}; color: black; text-align: center; border: 1px solid #ddd;' if color else ''

# Apply the styles
styled_df = heatmap_df.style.map(color_cells)

# Add some basic CSS for the overall table structure
html_output = f"""
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        h2 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th {{ background-color: #f2f2f2; padding: 10px; text-align: center; border: 1px solid #ddd; }}
        td {{ padding: 10px; font-weight: bold; }}
    </style>
</head>
<body>
    <h2>gNB Daily Regression - Flakiness Heatmap</h2>
    <p>This report highlights which test failures are likely real bugs vs. simulator flakiness.</p>
    {styled_df.to_html()}
</body>
</html>
"""

# ---------------------------------------------------------
# Step 5: Save to an HTML file
# ---------------------------------------------------------
with open('regression_heatmap.html', 'w') as f:
    f.write(html_output)

print("✅ Success! Open 'regression_heatmap.html' in your web browser to see the dashboard.")
