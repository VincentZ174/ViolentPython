#!/usr/bin/python
import crypt

def comparepass(cryptPass):
	salt = cryptPass[0:2]
	dictionaryFile = open('dictionary.txt', 'r')
	for password in dictionaryFile.readlines():
		password = password.strip('\n')
		cryptWord = crypt.crypt(password,salt)
		if cryptWord == cryptPass:
			print "[+]Password found: " + password  + "\n" 
		else:
			print "[-]Password not found.\n"

def main():
	passFile = open('password.txt', 'r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*]Cracking password for: " + user 
			comparepass(cryptPass)

if __name__ == "__main__":
	main()



