
import logging

from f1 import f1
from f2 import f2

FORMAT = '%(asctime)s - %(name)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

logger = logging.getLogger("main")
logger.info("main1")

f1()

logger.info("main2")

f2()

logger.info("main3")

f1()

logger.info("main4")