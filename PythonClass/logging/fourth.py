#!/usr/bin/python
# basicConfig
# logging.Formatter
# man date
# monitoring the disk /dev/sda1
# cronjob(linux) - cat /etc/crontab and scheduler(windows)

import logging
from subprocess import Popen,PIPE
import re
logging.basicConfig(filename='myappy.log',filemode='a',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',datefmt='%c')

# checking the disk space

# df -h /|tail -n 1|awk '{print $5}'|sed -e 's#%##g'
#disk_size = int(raw_input("please enter the disk size:"))

p1 = Popen(["df","-h","/"],stdout=PIPE)
p2 = Popen(["tail","-n","1"],stdin=p1.stdout,stdout=PIPE)
output = p2.communicate()[0]  # /dev/sda1        26G  4.9G   20G  21% /
disk_size = int(re.search('(\d+)%',output).group(1))

if disk_size < 60:
  logging.info("The disk is looking very healty {}".format(disk_size))
elif disk_size < 75:
  logging.warning("The disk is getting filled up - {}".format(disk_size))
elif disk_size < 85:
  logging.error("One of the disk has gone bad - {}".format(disk_size))
elif disk_size < 95:
  logging.critical("your application is down {}".format(disk_size))

