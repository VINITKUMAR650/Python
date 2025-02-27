Exercise 1: Print First 10 natural numbers using while loop

Expected output:
1
2
3
4
5
6
7
8
9
10

SOLUTION:

x = 1
while x <= 10:
    print(x)
    i += 1


Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

SOLUTION:

row = 5
for x in range(1, row + 1, 1):

    for j in range(1, x + 1):
        print(j, end=' ')

    print("")


Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
Expected Output:
Enter number 10
Sum is:  55

SOLUTION:

s = 0
n = 10

for i in range(1, n + 1, 1):
    s += i
print("\n")
print("Sum is: ", s)


Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be
2
4
6
8
10
12
14
16
18
20

SOLUTION:

n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)


Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:
numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:
75
150
145

SOLUTION:

numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)


Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop
For example, the number is 75869, so the output should be 5.

SOLUTION:

num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)


Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

SOLUTION:

n = 5
k = 5
for i in range(0, n+1):
    for j in range(k-i, 0, -1):
        print(j, end=' ')
    print()


Exercise 8: Print list in reverse order using a loop
Given:
list1 = [10, 20, 30, 40, 50]
Expected output:
50
40
30
20
10

SOLUTION:

list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
    print(item)


Exercise 9: Display numbers from -10 to - 1 using for loop
Expected output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1

SOLUTION:

for num in range(-10, 0, 1):
    print(num)


Exercise 10: Use else block to display a message “Done” after successful execution of for loop
For example, the following loop will execute without any error.
Given:
for i in range(5):
    print(i)
Expected output:
0
1
2
3
4
Done!

SOLUTION:

for i in range(5):
    print(i)
else:
    print("Done!")


Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
Examples:
6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
Given:
    # range
start = 25
end = 50
Expected output:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47

SOLUTION:

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0
            break
        else:
            print(num)


Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
Expected output:
Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34

SOLUTION:

num1, num2 = 0, 1

print("Fibonacci sequence:")

for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res


Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.
The factorial(symbol: !) means to multiply all whole numbers from the chosen number down to 1.
For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output:
120

SOLUTION:

num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


Exercise 14: Reverse a given integer number
Given:
76542
Expected output:
24567

SOLUTION:

num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)


Exercise 15: Use a loop to display elements from a given list present at odd index positions
Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0
Expected output:
20 40 60 80 100

SOLUTION:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")


Exercise 16: Calculate the cube of all numbers from 1 to a given number
Write a program to rint the cube of all numbers from 1 to a given number
Given:
input_number = 6
Expected output:
Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216

SOLUTION:

input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i * i * i))


Exercise 17: Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
Given:
    # number of terms
n = 5
Expected output:
24690

SOLUTION:

n = 5
start = 2
sum_seq = 0

for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    start = start * 10 + 2
print(sum_seq)


Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

SOLUTION:

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
