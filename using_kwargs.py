def product_price_info(**product):
    
    title = product["product_title"]
    price = product["product_price"]
    
    print(f'{title} costs {price}$')
    
product_price_info(product_title='Bottle of water', product_price=2)