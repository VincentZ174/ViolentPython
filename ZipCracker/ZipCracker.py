#!/usr/bin/python

import zipfile
import optparse
from threading import Thread

def extractZip(ZipFile, password):
	try:
		print "Testing Password: " + password 
		ZipFile.extractall(pwd=password)
		print '[+]Password found: ' + password + '\n'
	except:
		pass

def main():
	parser = optparse.OptionParser("python ZipCracker.py "+ "-f <zipfile> -d <dictfile>")
	parser.add_option('-f', dest='ZipName', type='string', help='Specify a zip file')
	parser.add_option('-d', dest='DictName', type='string', help='Specify a zip file')
	(options, args) = parser.parse_args()
	if (options.ZipName == None) | (options.DictName == None):
		print parser.usage
		exit(0)
	else:
		ZipName = options.ZipName
		DictName = options.DictName
	ZipFile = zipfile.ZipFile(ZipName)
	passFile = open(DictName)
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractZip, args=(ZipFile, password))
		t.start()

if __name__ == '__main__':
	main()
