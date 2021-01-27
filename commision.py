print("PRICE OF STOCK = 30/-.")
print("PRICE OF LOCK = 45/-.")
print("PRICE OF BARREL = 25/-.")
stocks = int(input("Enter number of stocks sold:"))
barrels = int(input("Enter number of barrels sold:"))
locks = int(input("Enter number of locks sold:"))
if locks==-1:
    exit()

if stocks<1 or stocks>80:
    print("Total stocks sold should be between 1 and 80.")
    exit()
if barrels<1 or barrels>90:
    print("Total barrels sold should be between 1 and 90.")
    exit()
if locks<1 or locks>70:
    print("Total locks sold should be between 1 and 70.")
    exit()
sales = stocks*30 + locks*45 + barrels*25
if sales<=1000:
    commission = sales*0.1
elif sales>1000 and sales<=1800:
    commission = 1000*0.1
    commission += 0.15*(sales-1000)
else:
    commission = 1000*0.1
    commission += 0.15*800
    commission += 0.2*(sales-1800)
print("Total sales amount is : ",sales)
print("Commission given to the sales person is : ",commission)

