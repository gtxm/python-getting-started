from celery import Celery
import os
import pydevd_pycharm
from flask import Flask

app = Flask(__name__)

celery_app = Celery()
celery_app.conf.broker_url = 'amqp://@hello-world-rabbitmq:5672/'


@celery_app.task()
def debug():
    attach()
    return


@app.route('/')
def hello_world():
    msg = 'Hello World!'
    # comment out to use Pycharm's remote debugger
    # debug.delay()
    return msg


def attach():
    if os.environ.get('WERKZEUG_RUN_MAIN'):
        print('Connecting to debugger...')
        pydevd_pycharm.settrace('0.0.0.0', port=3500, stdoutToServer=True, stderrToServer=True)


if __name__ == '__main__':
    print('Starting hello-world server...')
    # comment out to use Pycharm's remote debugger
    # attach()

    app.run(host='0.0.0.0', port=8080)
