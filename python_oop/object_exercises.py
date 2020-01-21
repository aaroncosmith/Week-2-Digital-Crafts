class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
    
    def print_contact_info(self, name, email, phone):
        print("{}'s contact info is: {} ; {} ".format(self.name, self.email, self.phone))

    def add_friend(self, friends):
        self.friends.append(friends)

    def num_friends(self):
        print(len(self.friends))

    
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

################################
# 2. create a class vehicle

class Vehicle: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # add a method
    def print_info(self, year, make, model):
        print("{} {} {}".format(self.year, self.make, self.model) )

car = Vehicle("Dodge", "Charger", "1969")
car.print_info(car.year, car.make, car.model)

# test adding our function on line 10
# sonny.print_contact_info(sonny.name, sonny.email, sonny.phone)

# add an instance variable (attribute)
# added it in __init__
# append into the list for each object

#jordan.friends.append(sonny)
#sonny.friends.append(jordan)

# find how many friends using len()
# print(len(jordan.friends))

# now I will add an add_friend method to Person line 15
jordan.add_friend(sonny)
sonny.add_friend(jordan)

# now lets add a num_friends method
jordan.num_friends()
# it works!!

# now we can count the number of greetings, added greeting_count attribute, added some
# code to the greet function
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)

print(sonny.greeting_count)