import json
import sqlite3

# read data from json file
with open('funds.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

conn = sqlite3.connect('investment_funds.db')
cursor = conn.cursor()

# create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS investment_funds (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_name TEXT NOT NULL,
    fund_manager_name TEXT NOT NULL,
    fund_description TEXT,
    fund_nav DECIMAL(15, 4) NOT NULL,
    fund_creation_date DATE NOT NULL,
    fund_performance DECIMAL(10, 4) NOT NULL,
    fund_status INT NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')),
    updated_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime'))
);
''')

cursor.execute('''
CREATE TRIGGER IF NOT EXISTS trigger_investment_funds_updated_at AFTER UPDATE ON investment_funds
BEGIN
    UPDATE investment_funds SET updated_at = DATETIME('now', 'localtime') WHERE rowid == NEW.rowid;
END;
''')

# migrate json data to database
for fund in data:
    # skip if the data is duplicated
    cursor.execute('SELECT COUNT(*) FROM investment_funds WHERE fund_name = ?', (fund['fund_name'],))
    if cursor.fetchone()[0] > 0:
        print(f"Skipping duplicate fund: {fund['fund_name']}")
        continue

    cursor.execute('''
    INSERT INTO investment_funds (fund_name, fund_manager_name, fund_description, fund_nav, fund_creation_date, fund_performance, created_at, updated_at, fund_status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        fund['fund_name'],
        fund['fund_manager_name'],
        fund['fund_description'],
        fund['fund_nav'],
        fund['fund_creation_date'],
        fund['fund_performance'],
        fund['created_at'],
        fund['updated_at'],
        1
    ))

conn.commit()
conn.close()

print("Data migration completed successfully.")
