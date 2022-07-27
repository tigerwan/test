import logging

def singleton(cls):
    instances = {}
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls.__name__] = cls(*args, **kwargs)
        return instances[cls.__name__]
    return getinstance


@singleton
class Log:

    def __init__(self):
        self.__loggers = {}
        self.__level = logging.INFO
        self.__format = None

    def getLoggers(self):
        """
        Return the singleton logger and set logging level
        """
        return self.__loggers


    def getLogger(self, name="root"):
        """
        Return the singleton logger and set logging level
        """
        if not self.__loggers.get(name):
            if name == "root":
                self.__loggers[name] = logging.getLogger()
            else:
                self.__loggers[name] = logging.getLogger(name)

        if self.__loggers[name].getEffectiveLevel() != self.__level:
            self.__loggers[name].setLevel(self.__level)

        logging.critical("add {} into {}".format(self.__loggers[name], self.__loggers))
        return self.__loggers[name]

    def setLevel(self, level=logging.INFO):
        """
        Apply logging level to all loggers
        """
        self.__level = level
        for name in self.__loggers:
            self.__loggers[name].setLevel(self.__level)

