import random
import sys
from main import db, User
from faker import Faker


def create_fake_users(n):
    faker = Faker()
    for i in range(n):
        user = User(name=faker.name(),
                    age=random.randint(18, 70),
                    address=faker.address().replace('\n', ', '),
                    phone=faker.phone_number(),
                    email=faker.email())
        db.session.add(user)
    db.session.commit()
    print(f'Added {n} fake users to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument.')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))
