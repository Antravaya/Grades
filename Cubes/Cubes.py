import math

def main():
    n = eval(input("Enter a natural number: "))
    sum = 0
    for i in range(1, n+1):
        sum = sum + math.pow(i,3)

    print("The sum of the cubes of the first", n, "natural numbers is:  ", sum)

main()
