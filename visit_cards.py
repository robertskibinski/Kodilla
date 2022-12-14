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
    def label_length(self,value):
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

PrivateCardList=[]
BusinessCardList=[]

def create_contacts(a, b):
     for i in range(b):
        nam = fake.first_name()
        lna =fake.last_name()
        ppn =fake.phone_number()
        ema = fake.email()
        ll = str(nam.label_length)
        nam = BaseContact(name=nam, surname=lna, private_phone_no=ppn, email=ema)
        PrivateCardList.append(nam)

        if a == 2:
            card2 = BusinessContact(name=nam, surname=lna, private_phone_no=ppn, email=ema, job=fake.job(), company=fake.company(), business_phone_no=fake.phone_number())
            BusinessCardList.append(card2)

        print(ll)
        print(nam.contact)


a = int(input('Podaj typ wizytówki (1-prywatna 2-firmowa): '))
b = int(input('Ile wizytówek chcesz generować?: '))

create_contacts(a,b)