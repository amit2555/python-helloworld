from flask import Flask
import logging


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info("Status request successful")
    return {"result": "OK - healthy"}

@app.route("/metrics")
def metrics():
    return {"data": {"UserCount": 140, "UserCountActive": 23}}


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
