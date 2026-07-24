class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        current_year = 2026
        return current_year - self.dob[2]


person = Person("Alice", "Egypt", [10, 5, 2000])
print("Name:", person.name)
print("Country:", person.country)
print("Age:", person.age())
