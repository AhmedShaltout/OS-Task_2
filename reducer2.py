import sys

purchase_dic ={}

for line in sys.stdin:
    line = line.strip()
    product_id, user_location = line.split('\t')
    product_id = int(product_id)
    try:
		if user_location not in purchase_dic[product_id]:
			purchase_dic[product_id].append(user_location)
    except:
		purchase_dic[product_id]= [user_location]

for product_id in purchase_dic.keys():
	print '%s\t%s'% ("product number: " +str(product_id), "number of countries: "+str(len(purchase_dic[product_id])))
