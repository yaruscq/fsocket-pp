import os
from flask import Flask 

from .events import socketio
from .routes import main 

def create_app():
    app = Flask(__name__)
    # app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host="0.0.0.0", port=port)

    # socketio.init_app(app)

    return app