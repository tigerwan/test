import logging
# by default this is WARNING.  Leaving it as WARNING here overrides 
# whatever setLevel-ing you do later so it seems they are ignored.
logging.basicConfig()

l = logging.getLogger(__name__)
l.setLevel(level=logging.INFO)
# if I hadn't called basicConfig with DEBUG level earlier, 
# info messages would STILL not be shown despite calling 
# setLevel above.  However now debug messages will not be shown 
# for l because setLevel set it to INFO

l.warning('A warning message will be displayed')
l.info('A friendly info message will be displayed')
l.debug('A friendly debug message will not be displayed')
