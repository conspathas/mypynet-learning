entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "\n%-15s %-15s" % ("ip_prefix", "as_path")






split1 = entry1.split(" ")
splice1_start = split1.index('701')
splice1 = split1[splice1_start:-1]
print "%-15s %-15s\n" % (split1[2], splice1)

split2 = entry2.split(" ")
splice2_start = split2.index('701')
splice2 = split2[splice2_start:-1]
print "%-15s %-15s\n" % (split2[2], splice2)

split3 = entry3.split(" ")
splice3_start = split3.index('701')
splice3 = split3[splice3_start:-1]
print "%-15s %-15s\n" % (split3[2], splice3)

split4 = entry4.split(" ")
splice4_start = split4.index('701')
splice4 = split4[splice4_start:-1]
print "%-15s %-15s\n" % (split4[2], splice4)
