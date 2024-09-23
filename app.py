from flask import Flask
from routes import register_routes
from response import error_response

app = Flask(__name__)

# register routes
register_routes(app)

@app.errorhandler(Exception)
def handle_exception(e):
    """Handle all unhandled exceptions."""
    return error_response('An internal server error occurred'), 500


@app.errorhandler(400)
def handle_bad_request(e):
    """Handle bad requests."""
    return error_response('The request could not be understood or was missing required parameters.'), 400

if __name__ == '__main__':
    app.run(debug=True)