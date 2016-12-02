import optparse
import socket

def connectScan(Host, Port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((Host, Port))
		s.send('ViolentPython\r\n')
		recv = s.recv(100)
		print '[+] %d/tcp Open' % Port
		print '[+] ' + str(recv)
		s.close()
	except:
		print '[-] %d/tcp Closed' % Port

def portScan(Host, Ports):
	try:
		IP = socket.gethostbyname(Host)
	except:
		print "[-] Cannot resolve '%s': Unknown host" % Host
		return
	try:
		Name = socket.gethostbyaddr(IP)
		print '\n[+] Scan Results for: ' + Name[0]
	except:
		print '\n[+] Scan Results for: ' + IP
	socket.setdefaulttimeout(1)
	for Port in Ports:
		print 'Scanning port: ' + Port
		connectScan(Host, int(Port))

def main():
	parser = optparse.OptionParser("usage %prog " + "-H <target host> -p <target port>")
	parser.add_option('-H', dest='Host', type='string', help='specify target host')
	parser.add_option('-p', dest='Port', type='string', help='specify target port(s) separated by commas')
	(options, args) = parser.parse_args()
	Host = options.Host
	Ports = str(options.Port).split(', ')
	if(Host == None) | (Ports[0] == None):
		print '[-] You must specify a target host and port'
		exit(0)
	portScan(Host, Ports)

if __name__ == '__main__':
	main()


