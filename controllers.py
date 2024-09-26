from flask import request
from response import success_response, error_response
import data_handler
from datetime import datetime
import sqlite3
from lang import lang

def get_funds():
    try:
        conn = data_handler.get_db_connection()

        funds = data_handler.get_funds(conn)
                
        fund_keys = ["fund_id", "fund_name", "fund_manager_name", "fund_description", "fund_nav", "fund_creation_date", "fund_performance", "fund_status", "created_at", "updated_at"]
        fund_list = [dict(zip(fund_keys, fund)) for fund in funds]

        return success_response(fund_list)
    except sqlite3.Error as e:
        return error_response(str(e)), 500
    except Exception as e:
        return error_response(lang['errors']['unexpected'] + str(e)), 500
    finally:
        if conn:
            conn.close() 


def create_fund():
    new_fund = request.json
    required_fields = ['fund_name', 'fund_manager_name', 'fund_description', 'fund_nav']
    for field in required_fields:
        if field not in new_fund:
            return error_response(f'Missing required field: {field}'), 400
    
    try:
        conn = data_handler.get_db_connection()

        duplicate_fund = data_handler.get_fund_by(conn, "fund_name", new_fund['fund_name'])
        if duplicate_fund:
            return error_response(lang['funds']['duplicate_fund']), 400

        new_fund['fund_creation_date'] = datetime.today().strftime('%Y-%m-%d')

        fund_data = (
            new_fund['fund_name'],
            new_fund['fund_manager_name'],
            new_fund['fund_description'],
            new_fund['fund_nav'],
            new_fund['fund_creation_date'],
            new_fund['fund_performance'],
        )

        id = data_handler.create_fund(conn, fund_data)
        if id:
            new_fund['fund_id'] = id
            return success_response(new_fund), 201
        else:
            conn.rollback()
            conn.close()
            return error_response(lang['errors']['error_create']), 500
    except sqlite3.Error as e:
        return error_response(str(e)), 500
    except Exception as e:
        return error_response(lang['errors']['unexpected'] + str(e)), 500
    finally:
        if conn:
            conn.close() 


def get_fund(fund_id):
    try:
        conn = data_handler.get_db_connection()
        fund = data_handler.get_fund_by(conn, "fund_id", fund_id)

        if fund is None:
            return error_response(lang['funds']['not_found']), 404
        
        fund_keys = ["fund_id", "fund_name", "fund_manager_name", "fund_description", "fund_nav", "fund_creation_date", "fund_performance", "fund_status", "created_at", "updated_at"]
        fund_data = dict(zip(fund_keys, fund))

        return success_response(fund_data)
    except sqlite3.Error as e:
        return error_response(str(e)), 500
    except Exception as e:
        return error_response(lang['errors']['unexpected'] + str(e)), 500
    finally:
        if conn:
            conn.close() 


def update_fund_performance(fund_id):
    performance_data = request.json

    # input validation
    if 'fund_performance' not in performance_data:
        return error_response('Missing required field fund_performance.'), 400
    
    # check if the performance data is valid
    fund_performance = performance_data['fund_performance']
    if not isinstance(fund_performance, (int, float)):
        return error_response(lang['funds']['invalid_performance']), 400
    

    try:
        conn = data_handler.get_db_connection()
        fund = data_handler.get_fund_by(conn, "fund_id", fund_id)

        if fund is None:
            return error_response(lang['funds']['not_found']), 404
        
        update_data = {
            'fund_performance': performance_data['fund_performance'],
            'updated_at': datetime.now().isoformat(),
        }

        update = data_handler.update_fund_performance(conn, fund_id, update_data)
        if update == 0:
            return error_response(lang['funds']['not_found']), 404

        return success_response(None)
    except sqlite3.Error as e:
        return error_response(str(e)), 500
    except Exception as e:
        return error_response(lang['errors']['unexpected'] + str(e)), 500
    finally:
        if conn:
            conn.close() 


def delete_fund(fund_id):
    try:
        conn = data_handler.get_db_connection()
        fund = data_handler.get_fund_by(conn, "fund_id", fund_id)

        if fund is None:
            return error_response(lang['funds']['not_found']), 404
        
        deleted = data_handler.delete_fund(conn, fund_id)
        if deleted == 0:
            return error_response(lang['funds']['not_found']), 404

        return success_response(None)
    except sqlite3.Error as e:
        return error_response(str(e)), 500
    except Exception as e:
        return error_response(lang['errors']['unexpected'] + str(e)), 500
    finally:
        if conn:
            conn.close() 