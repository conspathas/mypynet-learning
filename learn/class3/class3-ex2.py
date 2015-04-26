entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24      157.130.10.233         0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

print "\n%-15s %-15s" % ("ip_prefix", "as_path")

for per_entry in (entry1, entry2, entry3, entry4):
    split_entry = per_entry.split(" ")
    splice_entry_start = split_entry.index('701')
    splice_entry = split_entry[splice_entry_start:-1]
    print "\n%-15s %-15s" % (split_entry[2], splice_entry)
