import os
from chatapp import create_app, socketio

app = create_app()
port = int(os.environ.get('PORT', 5000))
socketio.run(app, host="0.0.0.0", port=port)
# socketio.run(app)