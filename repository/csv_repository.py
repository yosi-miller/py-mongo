import csv

from pymongo import errors

# from database.connect import taxi_db, drivers, cars
from database.connect import get_db
from services.logger import log_error, log_info


def read_csv(path):
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def init_taxi_drivers_from_csv():
    client, db = get_db()

    drivers = db['drivers']
    cars = db['cars']

    drivers.drop()
    cars.drop()

    try:
        for row in read_csv('data/practice_data.csv'):
            car = {
                'license_id': row['CarLicense'],
                'brand': row['CarBrand'],
                'color': row['CarColor']
            }

            car_id = cars.insert_one(car).inserted_id

            address  = {
                'city': row['City'],
                'street': row['Street'],
                'state': row['State']
            }

            driver = {
                'passport': row['PassportNumber'],
                'first_name': row['FullName'].split(' ')[0],
                'last_name': row['FullName'].split(' ')[1],
                'car_id': car_id,
                'address': address
            }

            drivers.insert_one(driver)
        log_info(f'action: completed insert  driver and cars to db')
    except errors.PyMongoError as e:
        log_error(f'action: try insert driver and cars to db, error: {e}')
        print(f'Error: {e}')
        return e
    finally:
        client.close()
