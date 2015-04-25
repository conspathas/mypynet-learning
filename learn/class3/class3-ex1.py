#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    print "The IP address is: %s" % ip_addr
else:
    print "You made an error"

ip_addr_list = ip_addr(".")

first_oct_bin = bin(int(ip_addr_list[0]))
second_oct_bin = bin(int(ip_addr_list[1]))
third_oct_bin = bin(int(ip_addr_list[2]))
fourth_oct_bin = bin(int(ip_addr_list[3]))

print "\n"
print "%-20s %-20s %-20s %-20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%-20s %-20s %-20s %-20s" % (first_oct_bin, second_oct_bin, third_oct_bin, fourth_oct_bin)

