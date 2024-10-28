import os
from chatapp import create_app, socketio

# LOCAL SETUP
# app = create_app()
# socketio.run(app, debug=True)


# RENDER PLATFORM 1
# @ Render: 
# Start Command: $ gunicorn --worker-class eventlet -w 1 app:app
# port=5000, 5233 成功！
# port=5233， 成功！ 但在 Render Platform 上顯示：Detected service running on port 5000 仍然是 5000

app = create_app()
# port = int(os.environ.get('PORT', 5000))
port = int(os.getenv('PORT', 5000))
socketio.run(app, host="0.0.0.0", port=port)



# RENDER PLATFORM 2 (不成功！)
# @ Render: 
# Start Command: $ gunicorn --worker-class eventlet -w 1 app:app "--bind 0.0.0.0:$PORT"
# Try define environment var $PORT; Try remove "--bind 0.0.0.0:$PORT": both doesn't work!

# app = create_app()
# socketio.run(app)