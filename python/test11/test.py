from class1 import Class1
from class2 import Class2

import logging
from tool_lib.log import Log

logging.basicConfig(format="(%(asctime)s - %(name)s - %(funcName)s - %(processName)s - %(threadName)s][%(levelname)s]: %(message)s)")
c1=Class1()

Log().setLevel(logging.DEBUG)

c2=Class2()

Log().getLogger().info("class1 level:{}".format(c1.get_logger().getEffectiveLevel()))
Log().getLogger().info("class2 level:{}".format(c2.get_logger().getEffectiveLevel()))