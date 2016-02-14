import os
bind = "127.0.0.1:8101"
workers = 8
worker_class = 'gevent'
timeout = 8000
daemon = True
LOGDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
pidfile = os.path.join(LOGDIR,'gunicorn_server.pid')
errorlog = os.path.join(LOGDIR,'gunicorn_server.log')
loglevel = "error"

