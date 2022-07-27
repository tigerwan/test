import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
