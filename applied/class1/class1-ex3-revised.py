# Import Kirk Byers snmp_helper library.
import snmp_helper 

# Set some constants
COMMUNITY_STRING = 'galileo'
IP = '50.242.94.227'

# Define our routers
router1 = (IP, COMMUNITY_STRING, 7961)
router2 = (IP, COMMUNITY_STRING, 8061)

# Create a dictionary of interesting OIDs
oid_list = {
    'sysName': '1.3.6.1.2.1.1.5.0',
    'ccmHistoryRunningLastChanged': '1.3.6.1.4.1.9.9.43.1.1.1.0',
    'ccmHistoryStartupLastChanged': '1.3.6.1.4.1.9.9.43.1.1.3.0'
}

# Loop through our routers
for a_device in (router1, router2):

    # Retrieve the system name    
    snmp_data = snmp_helper.snmp_get_oid(a_device, oid=oid_list['sysName'])
    router_id = snmp_helper.snmp_extract(snmp_data)

    # Retrieve the RunningLastChanged data
    snmp_data = snmp_helper.snmp_get_oid(a_device, oid=oid_list['ccmHistoryRunningLastChanged'])
    running_last_changed = snmp_helper.snmp_extract(snmp_data)

    # Retrieve the StartupLastChanged data
    snmp_data = snmp_helper.snmp_get_oid(a_device, oid=oid_list['ccmHistoryStartupLastChanged'])
    startup_last_changed = snmp_helper.snmp_extract(snmp_data)

    # Print the system name
    print router_id

    # Evaluate if the value of RunningLastChanged is greater than StartupLastChanged
    if running_last_changed > startup_last_changed:
        
        print "The running configuration has not been saved since the last configuration change." 

    # Evaluate if the value of RunningLastChanged is less than or equal to StartupLastChanged
    elif running_last_changed <= startup_last_changed:

        print "The running configuration has been saved since the last configuration change."

    # Determine if the StartupLastChanged is 0 and advise accordingly
    if startup_last_changed == 0:

        print "Please note - the startup configuration has not been saved since the last boot."
