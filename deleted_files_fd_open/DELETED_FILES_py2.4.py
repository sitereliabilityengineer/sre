#!/bin/env python
# -*- coding: utf-8 -*-
# Koldo Oteo Orellana (koldo.oteo@gmail.com) 01-Jun-2017
# https://github.com/SiteReliabilityEngineering
# Program to show deleted files that are still open (fd open)
import os
import sys


## Functions 
## Convert bytes to Mb
MB = (1024.0 * 1024.0)
def bytesMb(bytes):
	return float("%.1f" % (bytes / MB))

# Function to use for sorted . We return de index 6 (element 7) of the list that contains the size in bytes
def getKey(item):
	return item[6]

def print_red():
	sys.stdout.write("\033[1;31m")

def print_green():
	sys.stdout.write("\033[0;32m")

def print_reset():
	sys.stdout.write("\033[0;0m")

def print_bold():
	sys.stdout.write("\033[;1m")
	
##



# result of lsof. It shows the deleted files.
lsof_res = os.popen("lsof -X -a +L1 -s | grep -i \(deleted\)").read()


"""First we strip the null at the end '', then we split in thew newline to 
   create a multidimensional list, and after that, we split every element """
lsof_list = [ elem.split() for elem in lsof_res.strip().split('\n') ]

# convert size to float (Doing this, now we could order by Size)
for a in range(len(lsof_list)):
        lsof_list[a][6] = float(lsof_list[a][6])

# We sort the list by column [6] (filesize). We get the value of [6], bu passing the method getKey.
sorted_list = sorted(lsof_list, key=getKey, reverse=True)

# we obtain the index of the list
lsof_len = len(lsof_list)


# we do a loop, where we iterate in every element of the list, where idx is the index in the multidimensional sorted_list
def getdelfiles():
	idx = 0

	for idx in range(lsof_len):

		comm, pid, fd, sizebytes = sorted_list[idx][0],  sorted_list[idx][1],  sorted_list[idx][3], float(sorted_list[idx][6])
		sizemb, filen = bytesMb(sizebytes), sorted_list[idx][9]
		fd_id = sorted_list[idx][3].rstrip('rw')

		print_red()
		print ("Command: %s, pid: %s, fd: %s, File Size: %s, File_name: %s" % (comm, pid, fd, sizemb, filen))

		print_green()
		print ("You could truncate the file with ':> /proc/%s/fd/%s" % (pid, fd_id))
		print ('\n')
		idx += 1

# Start printing
print ('\n')
print_bold()
print (''List of deleted files, that still haves the file descriptor open, ordered by File Size !!! \n')
print_reset()

# Executing method, that display all the information: pid, fd, filesize, and also the FD location
getdelfiles()

print_reset()
