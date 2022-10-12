from socket import fromfd
from faker import Faker
from faker.providers import internet
from faker.providers import address
<<<<<<< HEAD
=======
import uuid
>>>>>>> 437b3d25201cf337b6e42dc934701077c3008359

fake = Faker('ru_RU')
fake.add_provider(internet)
print()

print('=Fake name=')
for _ in range(3):  
    print(fake.name())
print()

<<<<<<< HEAD
=======


print('=Fake email=')
for _ in range(3):  
    print (str(uuid.uuid4()) + '@gmail.com')
print()


>>>>>>> 437b3d25201cf337b6e42dc934701077c3008359
print('=random address=')
for _ in range(3):
    print(fake.address())
print()

print('=City=')
for _ in range(3):
    print(fake.city())
print()

print('=ZipCode=')
for _ in range(3):
    print(fake.postcode())
print()

print('=IP address=')
for _ in range(3):
    print(fake.ipv4_private())
print()

print('=Company name=')
for _ in range(3):
    print(fake.company_suffix()+ ' ' + fake.company())
print()