from flask import Flask
from threading import Thread
from gevent.pywsgi import WSGIServer

app = Flask('')


@app.route('/')
def home():
  return "Hello hi676"


def run():
  WSGIServer(('0.0.0.0', 8080), app).serve_forever()


def keep_alive():
  server = Thread(target=run)
  server.start()
