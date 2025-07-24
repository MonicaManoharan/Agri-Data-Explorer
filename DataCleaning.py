import pandas as pd
import numpy as np

# Load your CSV file
df = pd.read_csv("AgriDataset_Cleaned.csv")  # Replace with your filename

# Step 1: Replace all -1 values with NaN
df.replace(-1, np.nan, inplace=True)

# Step 2: Replace 0 with NaN in columns where 0 likely means missing
zero_invalid_columns = [
    'rice_yield_kg_per_ha', 'wheat_yield_kg_per_ha', 'maize_yield_kg_per_ha',
    'groundnut_yield_kg_per_ha', 'oilseeds_yield_kg_per_ha', 'cotton_yield_kg_per_ha',
    'rice_production_1000_tons', 'wheat_production_1000_tons', 'maize_production_1000_tons',
    'groundnut_production_1000_tons', 'oilseeds_production_1000_tons', 'cotton_production_1000_tons'
]

df[zero_invalid_columns] = df[zero_invalid_columns].replace(0, np.nan)

# Step 3: Fill NaNs with column mean (numeric columns only)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.mean()))

# Step 4 (Optional): Save the cleaned dataset
df.to_csv("cleaned_agri_data.csv", index=False)

print("✅ Dataset cleaned and saved as 'cleaned_agri_data.csv'")
