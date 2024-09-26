import unittest
import os
import sqlite3
from data_handler import create_connection, create_fund, get_fund_by, update_fund_performance, delete_fund
from unittest.mock import patch

class TestDatabaseOperations(unittest.TestCase):
    TEST_DB = 'test_investment_funds.db'

    @classmethod
    def setUpClass(cls):
        cls.conn = create_connection(cls.TEST_DB)
        cls.create_table()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        if os.path.exists(cls.TEST_DB):
            os.remove(cls.TEST_DB)

    @classmethod
    def create_table(cls):
        sql = '''CREATE TABLE IF NOT EXISTS investment_funds (
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
                );'''
        cls.conn.execute(sql)
        cls.conn.commit()

    def test_create_fund(self):
        fund_data = ("Test Fund", "Manager A", "A test fund.", 1000.0, "2023-01-01", 5.0)
        fund_id = create_fund(self.conn, fund_data)
        self.assertIsInstance(fund_id, int)

        # check if data is inserted
        fund = get_fund_by(self.conn, "fund_id", fund_id)
        self.assertIsNotNone(fund)
        self.assertEqual(fund[1], "Test Fund")
        self.assertEqual(fund[2], "Manager A")

    def test_update_fund_performance(self):
        fund_data = ("Performance Fund", "Manager B", "Fund for performance testing.", 2000.0, "2023-01-01", 0.0)
        fund_id = create_fund(self.conn, fund_data)

        update_data = {
            'fund_performance': 10.5,
        }

        # update the performance
        update_fund_performance(self.conn, fund_id, update_data)
        fund = get_fund_by(self.conn, "fund_id", fund_id)
        self.assertEqual(fund[6], 10.5)

    def test_delete_fund(self):
        fund_data = ("Delete Fund", "Manager C", "Fund for deletion testing.", 2500.0, "2023-01-01", 0.0)
        fund_id = create_fund(self.conn, fund_data)

        # delete the fund
        delete_fund(self.conn, fund_id)
        fund = get_fund_by(self.conn, "fund_id", fund_id)
        self.assertIsNone(fund)

if __name__ == '__main__':
    unittest.main()
