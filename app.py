from flask import Flask
from routes import register_routes
from init import init_db
app = Flask(__name__)

# register routes
register_routes(app)

# initialize database connection and tables
init_db(app)

if __name__ == '__main__':
    app.run(debug=True)