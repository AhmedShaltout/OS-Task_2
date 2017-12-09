import sys

purchase_dic ={}
customer_dic={}
for line in sys.stdin:
    line = line.strip()
    id, user_email, user_language, user_location, transaction_id, product_id, user_id, purchase_amount, product_description = line.split('\t')

    id = int(id)
    user_id = int(user_id)
    if id ==-1:
		try:
			purchase_dic[user_id].append(transaction_id)
			purchase_dic[user_id].append(product_id)
			purchase_dic[user_id].append(purchase_amount)
			purchase_dic[user_id].append(product_description)
		except:
			purchase_dic[user_id] = [transaction_id, product_id, purchase_amount, product_description]
    else:
        customer_dic[id] = [user_email, user_language, user_location]

for id in customer_dic.keys():
	try:
		user_email = customer_dic[id][0]
		user_language = customer_dic[id][1]
		user_location = customer_dic[id][2]
		while len(purchase_dic[id]) > 0:
			transaction_id = purchase_dic[id].pop(0)
			product_id = purchase_dic[id].pop(0)
			purchase_amount = purchase_dic[id].pop(0)
			product_description = purchase_dic[id].pop(0)
			print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'% (id, user_email, user_language, user_location, transaction_id, product_id, purchase_amount, product_description)
	except:
		continue
