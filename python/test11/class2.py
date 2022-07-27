from tool_lib.log import Log

class Class2:
    def __init__(self):
        logger = self.get_logger()
        logger.info("This is class1 logger:%s", logger)
    @classmethod
    def get_logger(cls):
        return Log().getLogger("{}:{}".format(__name__, cls.__name__))
