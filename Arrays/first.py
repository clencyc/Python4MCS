dog = [10, 20, 40]
sam = ['c', 'd', 'e']
arr3 = [10, 20, 40, 60, 70, 80]

print(dog[0])
# there are 2 types of arrays, static and dynamic
# stock prices of apple for 5days 
# retrieve the first price
# on what day was the price 432
# 

stock = [200, 400, 500, 432, 677]
print(stock[2]) # time complexity is O(1)

for i in range(len(stock)):
    if stock[i] == 432:
        print(i)
stock[2]
stock.insert(0, 100) # time complexity is O(n)
print(stock)   
stock.remove(677)# time complexity is O(n)
print(stock)
stock_name = ["AAPL", "GOOGL", "AMZN"]
stock_data = [
    {"name": "AAPL", "price": 200},
    {"name": "GOOGL", "price": 300},
    {"name": "AMZN", "price": 400}
]
print("first stock: " + stock_data[0]["name"])
