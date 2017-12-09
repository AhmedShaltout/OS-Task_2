import sys

purchase_dic = {}
index=0
for line in sys.stdin:
	index=index+1
	line = line.strip()
	line = line.split("\t")
	product_id = int(line[0])
	user_location = line[1]
	product_quantity = int(line[2])
	if product_id in purchase_dic.keys():
		boolean = True
		for item in purchase_dic[product_id]:
			if user_location in item.keys():
				item[user_location] = item[user_location] + product_quantity
				boolean = False
		if boolean==True:
			try:
				purchase_dic[product_id].append({user_location:product_quantity})
			except:
				purchase_dic[product_id] = [{user_location:product_quantity}]
	else:
		purchase_dic[product_id]=[{user_location:product_quantity}]
for item in purchase_dic.keys():
	for index in range(0, len(purchase_dic[item])):
		for country in purchase_dic[item][index].keys():
			print 'product:%s \tcountry:%s  \t%s sold'%(item,country,purchase_dic[item][index][country])