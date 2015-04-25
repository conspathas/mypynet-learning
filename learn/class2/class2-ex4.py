cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

cisco_ios_split = cisco_ios.split(",")
version_indice = cisco_ios_split[2]
ios_version = version_indice.split("Version ")[1]
print 'ios_version = "%s"' % ios_version

