products = ['phone', 'tablet', 'laptop']
quantities  = (343, 13, 74, 200)
tags = 'abd'
products_quantities = zip(products, quantities)

products_quant_dict = dict(products_quantities)
print(products_quant_dict)