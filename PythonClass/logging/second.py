#!/usr/bin/python
# basicConfig
# logging.Formatter
# man date

import logging
logging.basicConfig(filename='myappy.log',filemode='a',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',datefmt='%c')

logging.debug("this is a debug message")
logging.info("this is a info message")
logging.warning("this is a warning message")
logging.error("this is a error message")
logging.critical("this is a critical message")
