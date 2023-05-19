from attendee import Attendee

class ConferenceApp:
    def __init__(self):
        self.attendees = []
        self.number = 0
        self.readAttendees()

    def readAttendees(self):
        infile = open("attendees.txt", 'r')
        for line in infile.readlines():
            if line != "\n":
                tokens = line.split(",")
                name, company, state, email = tokens[0], tokens[1], tokens[2], tokens[3]
                attendee = Attendee(name, company, state, email)
                self.attendees.append(attendee)
                self.number += 1
            infile.close()

    def display(self, attendee):
        print(attendee)

    def listAttendees(self):
        for attendee in self.attendees:
            print(attendee, end = "")

    def add(self, attendee):
        self.attendees.append(attendee)
        self.number += 1

    def find(self, name):
        for attendee in self.attendees:
            if attendee.getName() == name:
                return attendee

    def delete(self, name):
        attendee = self.find(name)
        self.attendees.remove(attendee)

    def listAttendeesByState(self, state):
        for attendee in self.attendees:
            if attendee.getState() == state:
                print(attendee, end = "")

def getAttendee():
    name, company, state, email = input("Enter name, company, state, email: ").split(",")
    return Attendee(name, company, state, email)

def choice():
    print("\n============Menu============")
    print("1. Add new attendee")
    print("2. List all attendees")
    print("3. List all attendees by state")
    print("4. Delete an attendee by name")
    print("0. Quit")
    return eval(input(": "))

def main():
    app = ConferenceApp()
    app.listAttendees()
    m = choice()
    while m != 0:
        
        if m == 1:
            attendee = getAttendee()
            app.add(attendee)
        if m == 2:
            app.listAttendees()
        if m == 3:
            state = input("Enter a state: ")
            app.listAttendeesByState(state)
        if m == 4:
            name = input("Enter a name to delete: ")
            app.delete(name)
            
        m = choice()


if __name__ == "__main__": main()

    
