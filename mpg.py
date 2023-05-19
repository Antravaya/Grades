def main():
    
    print("This program calculates MPG")
    starting_odo = float(input("Enter the starting odometer: "))
    prev_odo = starting_odo
    total_trip = 0
    total_gas = 0
    entry = input("Enter current odometer reading and the amount of gas used: (hit 'enter' to quit)")
    while entry != "":
        print("This leg's emtry is", entry, end="")
        data = entry.split()
        current_odo = float(data[0])
        gas_used = float(data[1])
        trip = current_odo - prev_odo
        total_trip += trip
        prev_odo = current_odo
        total_gas += gas_used
        print(": MPG for this trip is", trip/gas_used)
        entry = input("Enter current odometer reading and the amount of gas used: (hit 'enter' to quit)")

    print("Total MGA is", total_trip/total_gas)
    
if __name__ == "__main__":
    main()
