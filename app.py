import os
from chatapp import create_app, socketio

# LOCAL SETUP
# app = create_app()
# socketio.run(app, debug=True)


# RENDER PLATFORM 1
# @ Render: 
# Start Command: $ gunicorn --worker-class eventlet -w 1 app:app

# app = create_app()
# port = int(os.environ.get('PORT', 5000))
# socketio.run(app, host="0.0.0.0", port=port)


# RENDER PLATFORM 2
# @ Render: 
# Start Command: $ gunicorn --worker-class eventlet -w 1 app:app --bind 0.0.0.0:$PORT
app = create_app()
socketio.run(app)