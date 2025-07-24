import pandas as pd

# Load the dataset
df = pd.read_csv("AgriDataset.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[()]", "", regex=True)

# Replace empty strings with NaN and clean data
df.replace('', pd.NA, inplace=True)

# Drop fully empty rows
df.dropna(how='all', inplace=True)

# Convert year column to numeric if it exists
if 'year' in df.columns:
    df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')

# Convert all numeric-looking columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype(str).str.replace(',', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='ignore')

# Fill remaining NaNs with 0
df.fillna(0, inplace=True)

# Save cleaned dataset
df.to_csv("Cleaned_ICRISAT_Data.csv", index=False)

print("✅ Data cleaning complete. Cleaned dataset saved as 'Cleaned_ICRISAT_Data.csv'")
