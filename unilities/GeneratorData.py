from faker import Faker

fake = Faker()
class GeneratorData:

    def __init__(self):
        self.last_name = fake.last_name()
        self.first_name = fake.first_name()
        self.middle_name = fake.first_name_male()