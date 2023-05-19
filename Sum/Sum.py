import math

def main():
    n = eval(input("How many numbers do you want to enter? "))
    sum = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        sum = sum + number
        
    print("The sum of the numbers is: ", sum)

main()
