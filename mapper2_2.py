import sys
for line in sys.stdin:
	line = line.strip()
	line = line.split("\t")
	product_id = line[5]
	user_location = line[3]
	product_quantity = line[6]
	print '%s\t%s\t%s'%(product_id,user_location,product_quantity)