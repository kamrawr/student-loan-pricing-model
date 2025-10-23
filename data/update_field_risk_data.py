#!/usr/bin/env python3
"""
Update Field Risk Data
Converts CSV field risk data to JSON format for pricing model
"""

import pandas as pd
import json
from datetime import datetime

# Load CSV data
df = pd.read_csv('field_risk_updated.csv', index_col=0)

# Convert to list of dictionaries
field_risk = []
for field, row in df.iterrows():
    field_risk.append({
        'field': field,
        'median_earnings': row['median_earnings'],
        'underemployment_proxy': row['underemployment_proxy'],
        'n_institutions': int(row['n_institutions'])
    })

# Create full JSON structure matching original format
data = {
    "metadata": {
        "generated": datetime.now().isoformat(),
        "source": "College Scorecard Data - Updated Analysis",
        "analysis_date": datetime.now().strftime('%Y-%m-%d'),
        "total_institutions": 7703,
        "institutions_with_earnings": 5693
    },
    "field_risk": field_risk
}

# Save to JSON
with open('field_risk_scores.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✅ Field risk data updated successfully!")
print(f"📊 {len(field_risk)} fields processed")
print("💾 Saved to: field_risk_scores.json")
