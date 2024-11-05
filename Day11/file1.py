
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
    
    def update_age(self, new_age):
        self.age = new_age
        return f"Age updated to {self.age}"


class PersonManager:
    def __init__(self):
        self.people = []

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, age = line.strip().split(',')
                    self.people.append(Person(name, int(age)))
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty list.")

   
    def save_data(self, filename):
        with open(filename, 'w') as file:
            for person in self.people:
                file.write(f"{person.name},{person.age}\n")

 
    def add_person(self, name, age):
        new_person = Person(name, age)
        self.people.append(new_person)
        print(f"Added {name}, Age: {age}")

    def update_person_age(self, name, new_age):
        for person in self.people:
            if person.name == name:
                person.update_age(new_age)
                print(f"Updated {name}'s age to {new_age}")
                return
        print(f"{name} not found in the list.")

    def display_all_people(self):
        for person in self.people:
            print(person.display_info())
