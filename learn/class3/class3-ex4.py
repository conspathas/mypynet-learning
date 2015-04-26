#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
else:
    print "You made an error"

octets = ip_addr.split(".")

if len(octets) != 4:
    print "You made an error"

elif (octets[0] == "127") or ((octets[0] == "169") and (octets[1] == "254")):
    print "You made an error" 

elif not 1 <= int(octets[0]) <= 223: 
    print "You made an error" 

elif not ((0 <= int(octets[1]) <= 255) and (0 <= int(octets[2]) <= 255) and (0 <= int(octets[3]) <= 255)):
    print "You made an error" 
     
else:
    print "Your entered IP address %s is valid." % ip_addr

