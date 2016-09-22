#!/usr/bin/python
# basicConfig
# logging.Formatter
# man date

import logging
logging.basicConfig(filename='myappy.log',filemode='a',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',datefmt='%c')

# checking the disk space

disk_size = int(raw_input("please enter the disk size:"))

if disk_size < 60:
  logging.info("The disk is looking very healty {}".format(disk_size))
elif disk_size < 75:
  logging.warning("The disk is getting filled up - {}".format(disk_size))
elif disk_size < 85:
  logging.error("One of the disk has gone bad - {}".format(disk_size))
elif disk_size < 95:
  logging.critical("your application is down {}".format(disk_size))
