def main():

    rate = float(input("Enter an interest rate: "))
    initial_Investment = 1
    investment = initial_Investment 
    years = 0
    while investment < initial_Investment  * 2:
        investment = investment * (1 + rate)
        years += 1
        print(investment)

    print("It takes", years, "years.")


if __name__ == "__main__":
    main()
