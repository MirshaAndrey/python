import random
import string
import uuid

from faker import Faker

fake = Faker("ru_RU")

k = int(15)


def generator_pw():
    pwd = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(pwd) for x in range(random.randint(k, k)))


data = [
    ["Название", "Данные"],
    {
        "Fake name": fake.name(),
        "Password": generator_pw(),
        "Fake email": str(uuid.uuid4()) + "@gmail.com",
        "random address": fake.address(),
        "City": fake.city(),
        "ZipCode": fake.postcode(),
        "IP address": fake.ipv4_private(),
        "Company name": fake.company_suffix() + " " + fake.company(),
    },
]

print(
    "{0:^14}|{1:^8}".format(*data[0]),
    "-" * 15 + "+" + "-" * 58,
    "\n".join("{0:<15}|{1:>58}".format(*i) for i in data[1].items()),
    sep="\n",
)
