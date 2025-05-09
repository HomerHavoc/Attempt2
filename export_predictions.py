import pandas as pd

# Example prediction data (replace with real model output)
predictions = [
    {"player": "Shohei Ohtani", "team": "LAD", "hr_prob": 0.28, "tier": "Ghost"},
    {"player": "Aaron Judge", "team": "NYY", "hr_prob": 0.26, "tier": "Alpha"},
    {"player": "Pete Alonso", "team": "NYM", "hr_prob": 0.25, "tier": "Alpha"},
]

# Convert to DataFrame
df = pd.DataFrame(predictions)

# Save to CSV
df.to_csv("top_100_hr_predictions.csv", index=False)

print("Top 100 HR predictions exported to CSV.")
