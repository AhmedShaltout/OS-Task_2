import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    id = "-1"
    user_email= "-1"
    user_language = "-1"
    user_location = "-1"
    transaction_id = "-1"
    product_id = "-1"
    user_id= "-1"
    purchase_amount= "-1"
    product_description= "-1"
    if len(line) == 4:
        id = line[0]
        user_email = line[1]
        user_language = line[2]
        user_location = line[3]
    else:
		transaction_id = line[0]
		product_id= line[1]
		user_id= line[2]
		purchase_amount= line[3]
		product_description= line[4]
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (id, user_email, user_language, user_location, transaction_id, product_id, user_id, purchase_amount, product_description)
