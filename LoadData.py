import pyodbc
import csv

# Connect to the SQL Server database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=crop_dataset_db;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

csv_file_path = "D:/Project- DsAgriDataExplorer/cleaned_agri_data.csv"

with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)

    for i, row in enumerate(reader, start=1):
        row = row[:24]  # Trim to expected column count
        row = [None if val == '' else val for val in row]

        if len(row) != 23:
            print(f"❌ Skipping row {i}: incorrect number of columns → {len(row)}")
            continue

        try:
            cursor.execute("""
            INSERT INTO AgriDataset (
                    dist_code, year, state_code, state_name,
                    dist_name,
                    rice_area_1000_ha,
                    rice_production_1000_tons,
                    rice_yield_kg_per_ha,
                    wheat_area_1000_ha,
                    wheat_production_1000_tons,
                    wheat_yield_kg_per_ha,
                    maize_area_1000_ha,
                    maize_production_1000_tons,
                    maize_yield_kg_per_ha,
                    groundnut_area_1000_ha,
                    groundnut_production_1000_tons,
                    groundnut_yield_kg_per_ha, 
                    oilseeds_area_1000_ha,
                    oilseeds_production_1000_tons,
                    oilseeds_yield_kg_per_ha,
                    cotton_area_1000_ha,
                    cotton_production_1000_tons,
                    cotton_yield_kg_per_ha
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, row)
        except Exception as e:
            print(f"❌ Row {i} failed to insert: {e}")

conn.commit()
print("✅ CSV data loaded successfully.")

cursor.close()
conn.close()
