
from multiprocessing.dummy import Pool as ThreadPool
from concurrent import futures
import logging
import random

import logging
import time

format = "[%(asctime)s,%(name)s,%(funcName)s,%(threadName)s][%(levelname)s] %(message)s"
logging.basicConfig(format=format,level=logging.DEBUG)



def f1():
    logger=logging.getLogger("f1")
    for i in range(10):
        logger.info("{}".format(i))


def f2():
    logger=logging.getLogger("f2")
    for i in range(10):
        logger.info("{}".format(i))



logger=logging.getLogger("main")
for i in range(10):
    logger.info("{}".format(i))

f1()

f2()

f1()



