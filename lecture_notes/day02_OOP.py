class User:
    # Attributes
    def __init__(self, username_from_user='unknownUser', email_from_user='unknownEmail', password_from_user='00000000'):
        self.username = username_from_user
        self.email = email_from_user
        self.password = password_from_user
        self.alive = True
    
    # Methods
    def say_hi(self, person): #this method can now be used on any item with class User
        print(f"hi, {person.username} my name is {self.username}")

    def murder(self, person):
        person.alive = False
        print(person.username, "has died at the hands of ", self.username)

john = User('johndoe1989', 'johndoe@email.com', 'p@$$w0rd')     # arguments passed in override defaults
mary = User()                                                   # no arguments passed, so defaults will be applied

print(john.username)
print(john.email)
print(john.password)
print(john)             # give us a bunch of garbage about the instance john
print(john.__dict__)    # turns john's attributes into a dict and prints it (really only for viewing or API input)

mary.say_hi(john)
john.say_hi(mary)

mary.murder(john)
print(john.__dict__)
