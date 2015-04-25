user_input = raw_input('''

Please enter an IP address using the following format options:-
    172.16.1.0
    172.16.1.
    172.16.1

Input: ''') 

ip_addr_list = user_input.split(".")
ip_addr_list = ip_addr_list[:3]
ip_addr_list.append('0')

ip_addr_string = ".".join(ip_addr_list)

print "\n"
print "The IP network is: %s" % ip_addr_string

first_oct_bin = bin(int(ip_addr_list[0]))
first_oct_hex = hex(int(ip_addr_list[0]))

print "\n"
print "%20s %20s %20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%20s %20s %20s" % (ip_addr_string, first_oct_bin, first_oct_hex)

