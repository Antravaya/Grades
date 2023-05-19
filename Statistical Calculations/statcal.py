from statcalClasses import StatSet

def main():
    stat = StatSet()
    more = 'y'
    while more != 'n':
        n = eval(input("Enter a number: "))
        stat.addNumber(n)
        more = input("More number? (y/n): ")

    print("\nMean:", stat.mean())
    print("Median:", stat.median())
    print("SD:", stat.stdDev())
    print("Count:", stat.count())
    print("Min:", stat.min())
    print("Max:", stat.max())

if __name__== "__main__": main()
