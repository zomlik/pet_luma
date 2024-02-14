from faker import Faker


class FakeData:
    fake = Faker("en_US")

    @property
    def first_name(self):
        return self.fake.first_name

    @property
    def last_name(self):
        return self.fake.last_name

    @property
    def email(self):
        return self.fake.email
