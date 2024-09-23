from flask import request
from response import success_response, error_response
from data_handler import read_data, write_data
from datetime import datetime

def get_funds():
    funds = read_data()
    return success_response(funds)


def create_fund():
    new_fund = request.json

    required_fields = ['fund_name', 'fund_manager_name', 'fund_description', 'fund_nav']
    for field in required_fields:
        if field not in new_fund:
            return error_response(f'Missing required field: {field}'), 400


    funds = read_data()

    # check if fund_name exists
    if any(fund['fund_name'] == new_fund['fund_name'] for fund in funds):
        return error_response('Fund name already exists.'), 400

    new_fund['fund_id'] = max(fund['fund_id'] for fund in funds) + 1 if funds else 1
    new_fund['fund_creation_date'] = datetime.today().strftime('%Y-%m-%d')
    new_fund['created_at'] = datetime.now().isoformat()
    new_fund['updated_at'] = datetime.now().isoformat()
    new_fund['status'] = 1
    
    funds.append(new_fund)
    write_data(funds)

    return success_response(new_fund, 'Fund created successfully!'), 201


def get_fund(fund_id):
    funds = read_data()

    fund = next((fund for fund in funds if fund['fund_id'] == fund_id), None)
    if fund is None:
        return error_response('Fund not found!'), 404

    return success_response(fund)


def update_fund_performance(fund_id):
    performance_data = request.json

    # input validation
    if 'fund_performance' not in performance_data:
        return error_response('Missing required field fund_performance.'), 400
    
    # check if the performance data is valid
    fund_performance = performance_data['fund_performance']
    if not isinstance(fund_performance, (int, float)):
        return error_response('Fund performance must be a number'), 400
    
    funds = read_data()
    
    fund = next((fund for fund in funds if fund['fund_id'] == fund_id), None)
    if fund is None:
        return error_response('Fund not found!'), 404
    
    fund['fund_performance'] = performance_data['fund_performance']
    fund['updated_at'] = datetime.now().isoformat()

    write_data(funds)

    return success_response(None, 'Fund performance updated successfully.')


def delete_fund(fund_id):
    funds = read_data()

    fund = next((fund for fund in funds if fund['fund_id'] == fund_id), None)
    if fund is None:
        return error_response('Fund not found!'), 404

    funds.remove(fund)
    write_data(funds)

    return success_response(None, 'Fund deleted successfully!')