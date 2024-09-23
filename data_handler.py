import json
import os
import sqlite3

DATA_FILE = os.path.join(os.path.dirname(__file__), 'funds.json')

def read_data():
    """
    Read data from the funds.json file.
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def write_data(data):
    """
    Write data to the funds.json file.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_fund(conn, fund):
    sql = ''' INSERT INTO investment_funds(fund_name, fund_manager_name, fund_description, fund_nav, fund_creation_date, fund_performance)
              VALUES(?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, fund)
    conn.commit()
    return cur.lastrowid


def get_fund_by_id(conn, fund_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM investment_funds WHERE fund_id=?", (fund_id,))
    return cur.fetchone()


def update_fund_performance(conn, fund_id, performance):
    sql = ''' UPDATE investment_funds
              SET fund_performance = ?
              WHERE fund_id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (performance, fund_id))
    conn.commit()


def delete_fund(conn, fund_id):
    sql = 'DELETE FROM investment_funds WHERE fund_id=?'
    cur = conn.cursor()
    cur.execute(sql, (fund_id,))
    conn.commit()
