"""
This test script covers the following cases:

1. Create a new fund and confirm success.
2. Try to create a duplicate fund and confirm the corresponding error is returned.
3. Get a list of all funds.
4. Update the performance of a fund and confirm success.
5. Try to update a non-existent fund and confirm the error is returned.
6. Delete a fund and confirm success.
7. Try to get a non-existent fund and confirm the error is returned.
"""


import unittest
import json
import os
from app import app
from data_handler import create_connection
from unittest.mock import patch
import sqlite3

class TestInvestmentFundAPI(unittest.TestCase):
    TEST_DB = 'test_investment_funds.db'

    @classmethod
    def setUpClass(cls):
        cls.conn = create_connection(cls.TEST_DB)
        cls.create_table()

        # set up Flask test client
        cls.app = app.test_client()
        cls.app.testing = True

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

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_create_fund(self):
        response = self.app.post('/api/v1/funds', 
            data=json.dumps({
                "fund_name": "Test Fund",
                "fund_manager_name": "Test Manager",
                "fund_description": "A test fund.",
                "fund_nav": 1000.0,
                "fund_performance": 5.0
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Success', response.data)

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_duplicate_fund_creation(self):
        # create duplicate fund
        self.app.post('/api/v1/funds', 
            data=json.dumps({
                "fund_name": "Test Fund",
                "fund_manager_name": "Test Manager",
                "fund_description": "A test fund.",
                "fund_nav": 1000.0,
                "fund_creation_date": "2023-01-01",
                "fund_performance": 5.0
            }),
            content_type='application/json'
        )
        
        response = self.app.post('/api/v1/funds', 
            data=json.dumps({
                "fund_name": "Test Fund",
                "fund_manager_name": "Test Manager",
                "fund_description": "A test fund.",
                "fund_nav": 1000.0,
                "fund_creation_date": "2023-01-01",
                "fund_performance": 5.0
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Fund name already exists.', response.data)

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_get_funds(self):
        response = self.app.get('/api/v1/funds')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data['data'], list)

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_update_fund_performance(self):
        # create a fund
        response = self.app.post('/api/v1/funds', 
            data=json.dumps({
                "fund_name": "Performance Fund",
                "fund_manager_name": "Manager A",
                "fund_description": "Fund for performance testing.",
                "fund_nav": 2000.0,
                "fund_creation_date": "2023-01-01",
                "fund_performance": 0.0
            }),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        fund_id = response_data['data']['fund_id']

        # update the fund performance
        update_response = self.app.put(f'/api/v1/funds/{fund_id}/performance',
            data=json.dumps({"fund_performance": 10.5}),
            content_type='application/json'
        )
        self.assertEqual(update_response.status_code, 200)
        self.assertIn(b'Success', update_response.data)

    def test_invalid_update_performance(self):
        # update the fund performance that is not existing
        response = self.app.put('/api/v1/funds/999/performance',
            data=json.dumps({"fund_performance": 10.5}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Fund not found!', response.data)

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_delete_fund(self):
        # create a fund
        self.app.post('/api/v1/funds', 
            data=json.dumps({
                "fund_name": "Delete Fund",
                "fund_manager_name": "Manager B",
                "fund_description": "Fund for deletion testing.",
                "fund_nav": 2500.0,
                "fund_creation_date": "2023-01-01",
                "fund_performance": 0.0
            }),
            content_type='application/json'
        )
        
        response = self.app.delete('/api/v1/funds/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success', response.data)

    @patch('data_handler.get_db_connection', lambda: sqlite3.connect('test_investment_funds.db'))
    def test_get_fund_not_found(self):
        response = self.app.get('/api/v1/funds/999')
        
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Fund not found!', response.data)

if __name__ == '__main__':
    unittest.main()
