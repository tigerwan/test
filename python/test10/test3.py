import logging

logger = logging.getLogger(__name__)

print("before level:{}".format(logger.getEffectiveLevel()))

logger.setLevel(logging.DEBUG)
print("after level:{}".format(logger.getEffectiveLevel()))


logger.info("info")
logger.debug("debug")
logger.warning("warn")
logger.error("error")
