class Attendee:
    def __init__(self, name, company, state, email):
        self.name = name
        self.company = company
        self.state = state
        self.email = email

    def getName(self):
        return self.name
    def getCompany(self):
        return self.company
    def getState(self):
        return self.state
    def getEmail(self):
        return self.email

    def __str__(self):
        return "Name:{}, Company:{}, State:{}, Email:{}".format(self.name, self.company, self.state, self.email)

