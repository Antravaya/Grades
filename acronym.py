def main():
    phrase = input("Enter a phrase: ")
    words = phrase.split()

    acronym = ""
    for word in words:
        acronym += word[0]
        
    print("Acronym is", acronym.upper())
main()
