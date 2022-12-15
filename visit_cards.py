from faker import Faker

fake = Faker('pl_PL')


class BaseContact:
    def __init__(self, name, surname, private_phone_no, email):
        self.name = name
        self.surname = surname
        self.private_phone_no = private_phone_no
        self.email = email

        self._label_length = 0

    @property
    def contact(self):
        print(f"Wybieram numer {self.private_phone_no} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
    def __init__(self, job, company, business_phone_no, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_phone_no = business_phone_no

    @property
    def contact(self):
        print(f"Wybieram numer {self.private_phone_no} i dzwonię do {self.name} {self.surname}")


def create_contacts(card_type, quantity):
    cards = []
    if card_type == 1:
        use_class = BaseContact
    else:
        use_class = BusinessContact

    for i in range(quantity):
        nam = fake.first_name()
        per = nam
        lna = fake.last_name()
        ppn = fake.phone_number()
        ema = fake.email()
        # ll = nam.label_length
        per = BaseContact(name=nam, surname=lna, private_phone_no=ppn, email=ema)
        if card_type == 2:
            comp = fake.company()
            job_ = fake.job()
            bpno = fake.phone_number()
            per = BusinessContact(name=nam, surname=lna, private_phone_no=ppn, email=ema, job=job_, company=comp, business_phone_no=bpno)

        cards.append(per)

card_type = int(input('Podaj typ wizytówki (1-prywatna 2-firmowa): '))
quantity = int(input('Ile wizytówek chcesz generować?: '))

create_contacts(card_type, quantity)
