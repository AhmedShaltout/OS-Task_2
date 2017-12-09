import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split("\t")
    product_id = data[5]
    user_location = data[3]
    print '%s\t%s' % (product_id, user_location)
