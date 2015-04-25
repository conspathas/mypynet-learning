#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
else:
    print "You made an error"

ip_addr_octet_list = ip_addr.split(".")

ip_addr_bin_list = []

for i,element in enumerate(ip_addr_octet_list):
    ip_addr_bin_list.append(bin(int(ip_addr_octet_list[i]))) 

for i,element in enumerate(ip_addr_bin_list):
    ip_addr_bin_list[i] = element[2:]

    while len(ip_addr_bin_list[i]) < 8:
        ip_addr_bin_list[i] = "0" + ip_addr_bin_list[i] 

ip_addr_bin = ".".join(ip_addr_bin_list)    

print "\n"
print "%-20s %-20s" % ("IP address", "Binary")
print "%-20s %-20s" % (ip_addr, ip_addr_bin)

