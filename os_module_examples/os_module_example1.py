'''
crated by Krishna Karki os module example

'''
import os

# print current working directory
print(os.getcwd())

# print all the directories, files inside the given path
for dirpath, dirnames, filenames in os.walk('/home/krishna/Downloads'):
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print(' ')