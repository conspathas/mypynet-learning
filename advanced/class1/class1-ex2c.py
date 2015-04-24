import snmp_helper 

COMMUNITY_STRING = 'galileo'
SNMP_PORT = (7961, 8061)
IP = '50.242.94.227'

OID_LIST = ('1.3.6.1.2.1.1.5.0', '1.3.6.1.2.1.1.1.0')
 

for PORT in SNMP_PORT:

    a_device = (IP, COMMUNITY_STRING, PORT)

    for OID in OID_LIST:
    
        snmp_data = snmp_helper.snmp_get_oid(a_device, oid=OID)
        output = snmp_helper.snmp_extract(snmp_data)
        print output

