def getsquare(numbers):
    square = []
    for n in numbers:
        square.append(n*n)
    return square

numbers = [2,3,6,7]
getsquare(numbers)
print("Square of numbers: ", getsquare(numbers))

def find_pe(prices, eps, index):
    pe = prices[index] / eps[index]
    return pe
prices = [100, 200, 300, 400]
eps = [10, 20, 30, 40]
index = 2
print("PE: ", find_pe(prices, eps, index))

list = [1, 2, 3, 4, 5, 5, 7, 8, 3, 5, 9, 1, 2]
for i in range (len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            print("Duplicate: ", list[j])
            break
def find_five(numbers):
    numbers = [2, 3, 6, 5, 7, 6, 7, 8, 9]
    try:
        return f"Found at index: {numbers.index(5)}"
    except ValueError:
        return "Number 5 not found in the list."

print(find_five(numbers))

