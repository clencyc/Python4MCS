my_expences = [
    {"month": "January", "amount": 2200},
    {"month": "February", "amount": 2350},
    {"month": "March", "amount": 2600},
    {"month": "April", "amount": 2130},
    {"month": "May", "amount": 2190}
]
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
print("Expenses in February: " + str(my_expences[1]["amount"]))
print("Extra amount spent in February: " + str(my_expences[1]["amount"] - my_expences[0]["amount"]))
print("Total in first quarter: " + str(my_expences[0]["amount"] + my_expences[1]["amount"] + my_expences[2]["amount"]))
for i in range(len(my_expences)):
    if my_expences[i]["amount"] == 2000:
        print("Spent exactly 2000 in " + my_expences[i]["month"])
my_expences.append({"month": "June", "amount": 1980})
print(my_expences, end="\n")