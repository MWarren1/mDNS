############################# 
##         mDNS           ## 
##      Python 2.7         ## 
##   By Redemption.Man     ## 
############################# 

###################################
## DNS enumeration from txt file ##
###################################
import argparse
import socket


## CLI switches
parser = argparse.ArgumentParser(prog='mDNS', description='Find DNS records')
parser.add_argument('--domain', required=True, help='base domain to search')
parser.add_argument('--subdomains', required=True, help='file that contains subdomains')

args = parser.parse_args()
domain = args.domain
subfile = args.subdomains

## create output file
output = open("mDNS-"+domain+".csv", 'w+')
output.write("Sub-Domain,IP Address\n")

with open(subfile, 'Ur') as f:
		for line in f:
			line = line.replace('\n', '')
			try:
				ip = socket.gethostbyname(line+"."+domain)
				print "Sub-Domain Found !!!   - "+line+"."+domain
				output.write(line+"."+domain+","+ip+"\n")
			except Exception:
				pass
##