from yahoo_fin import stock_info
brand = input ("Enter the company:")
price = stock_info.get_live_price(brand)
print (price)