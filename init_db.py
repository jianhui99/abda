"""
Currently it is just a simple fund table. 
In the future, we can:
1. put fund_manager_name into a separate fund_managers table and associate it through fund_manager_id.
2. creating indexes for fields that are frequently used as query conditions (such as fund_name, fund_creation_date, fund_manager_id, status) to speed up query performance.
"""

import sqlite3

# connect to sqlite database
try:
    conn = sqlite3.connect('investment_funds.db')
    cursor = conn.cursor()

    # create investment_funds table
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

    # insert data into investment_funds table
    cursor.execute('''
    INSERT INTO investment_funds (fund_name, fund_manager_name, fund_description, fund_nav, fund_creation_date, fund_performance) VALUES
    ('Growth Fund', 'John', 'A fund focused on long-term capital appreciation.', 15000000.00, '2020-01-15', 15),
    ('Income Fund', 'Bob', 'A fund aimed at providing regular income through dividends.', 10000000.00, '2020-01-20', 7);
    ''')

    conn.commit()
    conn.close()
    
except sqlite3.Error as e:
    print('sqlite3 error: ', e)
finally:
    if conn:
        conn.close()

print("Table initialized successfully!")
