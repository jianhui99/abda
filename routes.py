from flask import Blueprint
from response import error_response
from lang import lang
from controllers import get_funds, create_fund, get_fund, delete_fund, update_fund_performance

def register_routes(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle all unhandled exceptions."""
        return error_response(e), 500


    @app.errorhandler(400)
    def handle_bad_request(e):
        """Handle bad requests."""
        return error_response(lang['server']['bad_request']), 400

    api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

    api_bp.add_url_rule('/funds', 'get_funds', get_funds, methods=['GET'])
    api_bp.add_url_rule('/funds', 'create_fund', create_fund, methods=['POST'])
    api_bp.add_url_rule('/funds/<int:fund_id>', 'get_fund', get_fund, methods=['GET'])
    api_bp.add_url_rule('/funds/<int:fund_id>', 'delete_fund', delete_fund, methods=['DELETE'])
    api_bp.add_url_rule('/funds/<int:fund_id>/performance', 'update_fund_performance', update_fund_performance, methods=['PUT'])

    app.register_blueprint(api_bp)