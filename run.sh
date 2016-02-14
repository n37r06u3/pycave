#!/bin/bash
PROJECT_NAME=pycave
filepath=$(cd "$(dirname "$0")"; pwd)

cd $filepath

start() {
    echo "gunicorn start..."
    gunicorn ${PROJECT_NAME}.wsgi:application -c conf/gunicorn_conf.py
}

stop() {
    echo "gunicorn stop..."
    cat log/gunicorn_server.pid | xargs kill -9
}

static() {
    python manage.py collectstatic --noinput
}
debug() {
    python manage.py runserver 0.0.0.0:8101
}

case "$1" in
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    stop
    start
    ;;
static)
    static
    ;;
debug)
    debug
    ;;
*)
    echo $"Usage: $0 {start|stop|restart|static|debug}"
    exit 1
esac
