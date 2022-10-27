from flask import Flask
from routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)

    return app




# app = Flask(__name__)
# app.config["TEST"] = "Isso eh um teste"
# app.register_blueprint(routes)

# # @app.route('/')
# # def index():
# #     return 'index page'

# if __name__ == "__main__":
#     app.run(debug=True)