#sum of two numbers
a=int(input())
b=int(input())
c=a+b
print(c)
#odd or even
a=int(input())
if(a%2==0):
	print("its even")
else:
	print("its odd")
#Factorial calculation
num = 6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
#fobonacci sequence
n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1

while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
#reverse string
a="vikram"
print(a[::-1])
#palindrome check
def isPalindrome(s):
    return s == s[::-1]
s = "tamil"
ans = isPalindrome(s)
if ans:
    print("True")
else:
    print("False")
#leap year
def is_leap_year_modulo(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year_to_check = 2024
result_modulo = is_leap_year_modulo(year_to_check)
print(f"{year_to_check} is a leap year: {result_modulo}")
#amstrong number
def power(x, y):
	if y == 0:
		return 1
	if y % 2 == 0:
		return power(x, y // 2) * power(x, y // 2)
		
	return x * power(x, y // 2) * power(x, y // 2)
def order(x):
	n = 0
	while (x != 0):
		n = n + 1
		x = x // 10
	return n
def isArmstrong(x):
	n = order(x)
	temp = x
	sum1 = 0
	while (temp != 0):
		r = temp % 10
		sum1 = sum1 + power(r, n)
		temp = temp // 10
	return (sum1 == x)
x = 153
print(isArmstrong(x))
x = 1253
print(isArmstrong(x))
