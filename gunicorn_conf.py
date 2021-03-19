from loguru import logger

proc_name = "flask_api"
workers = 8
worker_class = 'gevent'
bind = "0.0.0.0:7411"
timeout = 30


def when_ready(server):
    logger.remove()
    log_config = {'enqueue': True, 'rotation': '20:12', 'retention': '2 weeks'}
    logger.add('log/app.log', level='DEBUG', **log_config)
