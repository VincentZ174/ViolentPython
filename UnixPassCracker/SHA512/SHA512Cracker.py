import hashlib

def comparepass(cryptedPass):
	dictFile = open('dictionary.txt', 'r')
	for words in dictFile.readlines():
		words = words.strip('\n')
		hash_object = hashlib.sha512(words.encode())
		cryptedWord = hash_object.hexdigest()
		if cryptedWord == cryptedPass:
			print "[+]Password found: " + words + "\n"
		else:
			print "[-]Password not found.\n"

def main():
	passFile = open('password.txt', 'r')
	for password in passFile.readlines():
		if ":" in password:
			user = password.split(':')[0]
			cryptedPass = password.split(':')[1].strip(' ')
			print '[*] Cracking Password for: ' + user
			comparepass(cryptedPass)

if __name__ == "__main__":
	main()
			