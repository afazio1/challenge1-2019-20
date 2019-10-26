# Calculates the sum of the sqaures from 0-100

global sumOfSquares
sumOfSquares = 0

for x in range(0, 101, 1):
	num = x ** 2
	sumOfSquares = num + sumOfSquares

# Calculates the square of the sum from 0-100 

global squareOfSum
num = 0

for x in range(0, 101, 1):
	num = x + num
	squareOfSum = num ** 2

# Calculates the difference between the square of sum and sum of squares

finalAnswer = squareOfSum - sumOfSquares
print(finalAnswer)
	
