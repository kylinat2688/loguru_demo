from loguru import logger
from flask import Flask

app = Flask(__name__)


@app.route('/write_log')
def write_log():
    for i in range(100):
        logger.info('I also meet a problem like this, and I have used the parameter equeue=True')
    return '{}'
