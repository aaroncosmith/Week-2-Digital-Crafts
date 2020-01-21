class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

# Write code to:

#  1. instantiate an istance object of Person with name of "Sonny"
# email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# 2. same thing but with Jordan

jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# 3. Have sonny greet jordan using the greet method

sonny.greet(jordan)

# 4. have jordan greet sonny

jordan.greet(sonny)

# 5. write a print statement to print the contact info (email and phone)
# of sonny

print("{}'s contact info is: {} ; {} ".format(sonny.name, sonny.email, sonny.phone))

# 6. do the same for Jordan, we could also add a function to our class to do this

print("{}'s contact info is: {} ; {} ".format(jordan.name, jordan.email, jordan.phone))

