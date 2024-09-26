import json
import os
import sqlite3
from flask import current_app


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def get_db_connection():
    db_path = current_app.config['DATABASE']
    conn = sqlite3.connect(db_path)
    return conn


def create_fund(conn, fund):
    sql = ''' INSERT INTO investment_funds(fund_name, fund_manager_name, fund_description, fund_nav, fund_creation_date, fund_performance)
              VALUES(?, ?, ?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, fund)
    conn.commit()
    return cur.lastrowid


def get_fund_by(conn, key, val):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM investment_funds WHERE {key}=?", (val,))
    return cur.fetchone()


def update_fund_performance(conn, fund_id, fund):
    sql = "UPDATE investment_funds SET "
    sql += ", ".join([k + " = ?" for k in fund.keys()])
    sql += " WHERE fund_id = ?"

    vals = list(fund.values())
    vals.append(fund_id)

    cur = conn.cursor()
    cur.execute(sql, vals)
    conn.commit()
    return cur.rowcount


def delete_fund(conn, fund_id):
    sql = "DELETE FROM investment_funds WHERE fund_id=?"
    cur = conn.cursor()
    cur.execute(sql, (fund_id,))
    conn.commit()
    return cur.rowcount


def get_funds(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM investment_funds")
    return cur.fetchall()

