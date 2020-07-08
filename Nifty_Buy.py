"""
Author : Sohan Singh
Basic Python Script

"""

print("Enter the Capital Avail\n")
Capital = float(input())
print("Capital Available : ", Capital)


print("Current Strike Price : ")
price = float(input())
print("Price :", price)

Stock = float(Capital/price)

print("Stock Purchasing Capacity :",Stock)


ValidStock = Stock - (Stock % 75);
print("Valid Order Stock", ValidStock)

