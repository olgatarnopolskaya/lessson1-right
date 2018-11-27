def get_vat(price):
	vat = price / 100 * 18
	return round(vat, 2)
	price_no_vat = price - vat
	

result = get_vat(100)
print('Сумма НДС: {}'.format(result))



