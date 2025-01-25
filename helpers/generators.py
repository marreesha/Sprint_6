from faker import Faker


def generate_order_data():
    fake = Faker("ru_RU")
    return {
        "name": fake.first_name(),
        "surname": fake.last_name(),
        "address": fake.street_name(),
        "phone": fake.numerify('8##########'),
        "delivery_date": fake.date_between(start_date="today", end_date="+180d").strftime("%d.%m.%Y"),
        "comment": fake.sentence(),
    }
