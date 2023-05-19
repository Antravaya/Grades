def main():
    n = int(input("Enter the number of credits earned: "))

    standing = "Freshman"
    if n >= 7 and n < 16:
        standing = "Sophomore"
    elif n >= 16 and n < 26:
        standing = "Junior"
    elif n >= 26:
        standing = "Senior"

    print("Student's class standing is ", standing)


if __name__ == "__main__":
    main()
