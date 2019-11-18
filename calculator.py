#this needs work

print("\nWelcome to the C00L Calculator!")
userCalculation = input("\nEnter a calculation: ")
userCalculation = [userCalculation]
print(userCalculation);

if "+" in userCalculation:
    x = userCalculation.index("+")
    sum = int(userCalculation[x-1]) + int(userCalculation[x+1])
    print(sum)
