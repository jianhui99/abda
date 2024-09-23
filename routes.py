from flask import Blueprint
from controllers import get_funds, create_fund, get_fund, delete_fund, update_fund_performance

def register_routes(app):
    api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

    api_bp.add_url_rule('/funds', 'get_funds', get_funds, methods=['GET'])
    api_bp.add_url_rule('/funds', 'create_fund', create_fund, methods=['POST'])
    api_bp.add_url_rule('/funds/<int:fund_id>', 'get_fund', get_fund, methods=['GET'])
    api_bp.add_url_rule('/funds/<int:fund_id>', 'delete_fund', delete_fund, methods=['DELETE'])
    api_bp.add_url_rule('/funds/<int:fund_id>/performance', 'update_fund_performance', update_fund_performance, methods=['PUT'])

    app.register_blueprint(api_bp)