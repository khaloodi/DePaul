numShares = eval(input("Number of shares purchased/sold: "))
purchasePrice = eval(input("Purchase price of one share: "))
sellingPrice = eval(input("Selling price of one share: "))

fee = 2.5/100

amountInvested = numShares * purchasePrice
amountSold = numShares * sellingPrice
serviceFees = (amountInvested*fee) + (amountSold*fee)
net = amountSold - amountInvested - serviceFees

print("Amount invested = " + str(amountInvested))
print("Total Service Fees = " + str(serviceFees))
print("Amount of Investment Gains or Losses = " + str(net))

'''
Test 1:
Purchased 200 shares at	$10	a share, sold at $20 a share generates a	
gain of	$10	a share	and	total service fees of $150.
Expected results: An invested amount of	2000.00 dollars, results in	a gain of	
1850.00 dollars. 

Output:
Number of shares purchased/sold: 200
Purchase price of one share: 10
Selling price of one share: 20
Amount invested = 2000
Total Service Fees = 150.0
Amount of Investment Gains or Losses = 1850.0

Test 2:
Purchased 200 shares at	$20	a share, sold at $10 a share generates a	
loss of	$10	a share	and	total service fees of $150.
Expected results: An invested amount of	4000.00 dollars, results in	a lose of	
2150.00 dollars. 

Output:
Number of shares purchased/sold: 200
Purchase price of one share: 20
Selling price of one share: 10
Amount invested = 4000
Total Service Fees = 150.0
Amount of Investment Gains or Losses = -2150.0
'''