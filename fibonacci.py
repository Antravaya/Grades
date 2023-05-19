def fib(n):
    if n in {1, 2}:
        return 1

    prev, curr = 1, 1
    for i in range(3, n+1):
        prev, curr = curr, prev + curr

    return curr


def main():

    n = int(input("Enter a number: "))
    print("The {0}th Fibonacci number is {1}".format(n, fib(n)))

main()

