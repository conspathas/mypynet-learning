import snmp_helper 

COMMUNITY_STRING = 'galileo'
SNMP_PORT = (7961,8061)
IP = '50.242.94.227'

OID_ID = '1.3.6.1.2.1.1.5.0'
OID_LIST = ('1.3.6.1.2.1.1.3.0', '1.3.6.1.4.1.9.9.43.1.1.1.0', '1.3.6.1.4.1.9.9.43.1.1.2.0', '1.3.6.1.4.1.9.9.43.1.1.3.0')
 
for PORT in SNMP_PORT:

    a_device = (IP, COMMUNITY_STRING, PORT)

    WRITES = []

    snmp_data = snmp_helper.snmp_get_oid(a_device, oid=OID_ID)
    router_id = snmp_helper.snmp_extract(snmp_data)

    for OID in OID_LIST:

        snmp_data = snmp_helper.snmp_get_oid(a_device, oid=OID)
        output = snmp_helper.snmp_extract(snmp_data)
        # print output
        WRITES.append(output)

    print router_id

    if WRITES[1] > WRITES[2]:
        
        print "The running configuration has not been saved since last change." 

    else:

        print "All appears well with the state of the configuration save."

    if WRITES[3] == 0:

        print "The startup configuration has not been saved since the last boot"
