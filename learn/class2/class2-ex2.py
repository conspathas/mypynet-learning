user_input = raw_input('''

Please enter an IP address. 
Input: ''') 

ip_addr_list = user_input.split(".")

first_oct_bin = bin(int(ip_addr_list[0]))
second_oct_bin = bin(int(ip_addr_list[1]))
third_oct_bin = bin(int(ip_addr_list[2]))
fourth_oct_bin = bin(int(ip_addr_list[3]))

print "\n"
print "%-20s %-20s %-20s %-20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "%-20s %-20s %-20s %-20s" % (first_oct_bin, second_oct_bin, third_oct_bin, fourth_oct_bin)

