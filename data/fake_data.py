from mimesis import Generic, Locale


class FakeData:
    _generate = Generic(Locale.EN)

    @classmethod
    def first_name(cls):
        return cls._generate.person.first_name()

    @classmethod
    def last_name(cls):
        return cls._generate.person.last_name()

    @classmethod
    def email(cls):
        return cls._generate.person.email()
