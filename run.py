from forum import app
import os

port = int(os.environ.get('PORT', 5000))
host = os.environ.get('HOST', '127.0.0.1')
debug = bool(os.environ.get('DEBUG', True))

app.secret_key = os.urandom(24)
app.run(host=host, port=port, debug=debug)
