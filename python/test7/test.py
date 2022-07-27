
from multiprocessing.dummy import Pool as ThreadPool
from concurrent import futures
import logging
import random
import time

class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('id', self.extra['id'])
        return '[%s] %s' % (my_context, msg), kwargs


def worker(x):
    logger = logging.getLogger(x)
    logger.setLevel(logging.DEBUG)
    adapter = CustomAdapter(logger, {"id": None})
    for i in range(5):
        time.sleep(random.randint(0,2))
        adapter.info("log message {}".format(i), id=x)


def lambda_handler(event, context):
    """
    pool = ThreadPool(2)
    pool.map(worker, ["a","b"])
    pool.close()
    pool.join()
    """
    pool = futures.ThreadPoolExecutor(max_workers=2)
    pool.map(worker,["a","b"])

    pool.shutdown(wait=True)

