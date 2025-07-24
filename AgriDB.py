import pyodbc

# Step 1: Connect to the master DB to create new database
conn_master = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=master;'
    'Trusted_Connection=yes;'
)

conn_master.autocommit = True  # 🔧 Fix: Needed to run CREATE DATABASE
cursor_master = conn_master.cursor()

# Step 2: Create the crop_dataset_db if it doesn't exist
cursor_master.execute("IF DB_ID('crop_dataset_db') IS NULL CREATE DATABASE crop_dataset_db")
conn_master.commit()
print("✅ Database 'crop_dataset_db' created.")
cursor_master.close()
conn_master.close()

# Step 3: Connect to the new database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=crop_dataset_db;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Step 4: Create the table
create_table_sql = """
IF OBJECT_ID('AgriDataset', 'U') IS NULL
CREATE TABLE AgriDataset (
    dist_code INT,
    year INT,
    state_code INT,
    state_name NVARCHAR(100),
    dist_name NVARCHAR(100),
    rice_area_1000_ha FLOAT,
    rice_production_1000_tons FLOAT,
    rice_yield_kg_per_ha FLOAT,
    wheat_area_1000_ha FLOAT,
    wheat_production_1000_tons FLOAT,
    wheat_yield_kg_per_ha FLOAT,
    maize_area_1000_ha FLOAT,
    maize_production_1000_tons FLOAT,
    maize_yield_kg_per_ha FLOAT,
    groundnut_area_1000_ha FLOAT,
    groundnut_production_1000_tons FLOAT,
    groundnut_yield_kg_per_ha FLOAT,
    oilseeds_area_1000_ha FLOAT,
    oilseeds_production_1000_tons FLOAT,
    oilseeds_yield_kg_per_ha FLOAT,
    cotton_area_1000_ha FLOAT,
    cotton_production_1000_tons FLOAT,
    cotton_yield_kg_per_ha FLOAT
)
"""
cursor.execute(create_table_sql)
conn.commit()
print("✅ Table 'AgriDataset' created.")

# Close connection
cursor.close()
conn.close()
