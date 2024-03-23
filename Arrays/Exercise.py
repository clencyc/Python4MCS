# generate a python code that finds the minimum, reverse and duplicates in an array
def find_min(arr):
    return min(arr) #it 

def reverse_array(arr):
    return arr[::-1]

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Test the functions
arr = [30, 40, 42, 43, 22, 33, 56, 12, 42, 43, 78, 34, 23, 45, 32, 30]

print("Minimum value:", find_min(arr))
print("Reversed array:", reverse_array(arr))
print("Duplicates:", find_duplicates(arr))