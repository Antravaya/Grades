import math

def sumN(n):
    sum = 0
    for i in range(n+1):
        sum += i

    return sum

def sumNCubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += math.pow(i, 3)

    return sum

def main():
    n =  int(input("Enter a natural number: "))

    n1 = sumN(n)
    n2 = sumNCubes(n)

    print("The sum of the first {0} natural numbers is {1}".format(n, n1))
    print("The sum of the cubes of the first {0} natural numbers is {1}".format(n, n2))

main()
