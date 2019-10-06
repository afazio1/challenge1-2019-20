#loop through numbers
#check if numbers are divisible by 3: return no remainder when divided by 3
#check if numbers are divisible by 5: return no remainder when divided by 5
#store the numbers and add them to a sum
#display the sum

def sumNumsToNumber(x):
  global sum
  for i in range(1, x):
    if i%3 == 0 or i%5 == 0:
      sum = sum + i
  sum = str(sum)
  x = str(x)
  print("The sum of all numbers below " + x +" that are multiples of 3 or 5 is " + sum)
    
sum = 0
endNum = input("Choose the ending number: ")
endNum = int(endNum)
sumNumsToNumber(endNum)