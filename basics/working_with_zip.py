products = ['phone', 'tablet', 'laptop']
quantities = [343, 13, 74]
tags = 'asd'


products_quant = zip(products, quantities, tags)
print(products_quant)
print(type(products_quant))

#products_quant_list = list(products_quant)
#print(products_quant_list)

for product in products_quant:
    print(product[0])