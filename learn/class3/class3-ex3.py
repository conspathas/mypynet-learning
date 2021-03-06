show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10         YES     NVRAM       up          up
NVI0                  6.9.4.10        YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

split_data = show_ip_int_brief.split()
data_list = []

for i in range(len(split_data)/6):
    if (split_data[4] == "up") and (split_data[5] == "up"):
        data_list.append(tuple(split_data[0:6]))
        del split_data[0:6]
    else:
        del split_data[0:6]

for output in enumerate(data_list):
    print output
