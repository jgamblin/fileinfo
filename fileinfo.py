
#!/usr/bin/env python
# Name:     fileinfo.py
# Purpose:  Displays File Informaation
# By:       Jerry Gamblin
# Date:     17.07.15
# Modified  17.08.15
# Rev Level 0.1
# -----------------------------------------------

import os
import stat  # index constants for os.stat()
import time
import hashlib
import sys

#Get File To SCAN
if len(sys.argv) != 2:
    print("Error: specify a file!")
    exit(0)

file_name = sys.argv[1]

file_stats = os.stat(file_name)

# create a dictionary to hold file info
file_info = {
   'fname': file_name,
   'fsize': round((file_stats [stat.ST_SIZE] / 1024) /1024.0, 2),
   'f_lm': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
   'f_la': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_ATIME])),
   'f_ct': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))

}

md5 = hashlib.md5(open(file_name, 'rb').read()).hexdigest() 
sha256 = hashlib.sha256(open(file_name, 'rb').read()).hexdigest()


print "File Size     = %(fsize)s Megabytes" % file_info
print "Last Modified = %(f_lm)s" % file_info
print "Last Accessed = %(f_la)s" % file_info
print "Creation Time = %(f_ct)s" % file_info
print "MD5 Hash      = %s" % md5
print "SHA 256 Hash  = %s" % sha256
