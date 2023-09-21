import random
import mysql.connector
from faker import Faker
from datetime import datetime, timedelta
import time

# Define the database name
database_name = "Parking_Management"

# Connect to MySQL 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="88888888"
)

# Create the database if it doesn't exist
cursor = db.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
cursor.close()

# Connect to the specified database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="88888888",
    database=database_name
)
cursor = db.cursor()

# Number of dummy data to be generated
n = 150

# Sleeping time after execution of each table and its dummy data insertion
s = 3

# Create user_table
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_table (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact BIGINT,
    age INT CHECK(age >= 18),
    city VARCHAR(255)
)
""")
db.commit()

# generate dummy user data and insert
fake = Faker()
for _ in range(n):
    first_name = fake.first_name()
    last_name = fake.last_name()
    contact = fake.random_int(min=6000000000, max=9999999999)
    age = fake.random_int(min=18, max=80)
    city = fake.city()
    cursor.execute("""
    INSERT INTO user_table (first_name, last_name, contact, age, city)
    VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, contact, age, city))
db.commit()

# sleep for s seconds
time.sleep(s)

# create vehicle_type
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicle_type (
    vehicle_type_id INT PRIMARY KEY,
    vehicle_type VARCHAR(255)
)
""")
db.commit()

# insert vehicle_type data
vehicle_types = [
    (1, 'Motorcycle'),
    (2, 'Car'),
    (3, 'Pickup vehicle'),
    (4, 'Bus / Truck')
]
cursor.executemany("INSERT INTO vehicle_type (vehicle_type_id, vehicle_type) VALUES (%s, %s)", vehicle_types)
db.commit()

# sleep for s seconds
time.sleep(s)

# create vehicles
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT PRIMARY KEY,
    vehicle_type_id INT,
    license_no VARCHAR(255),
    user_id INT,
    time_in DATETIME,
    time_out DATETIME,
    FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_type(vehicle_type_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user_table(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
""")
db.commit()

# generate dummy vehicles data and insert
for i in range(n):
    vehicle_type_id = random.randint(1, 4)
    license_no = f'{chr(random.randint(65, 90))}{chr(random.randint(65, 90))} ' \
                 f'{random.randint(10, 99)} {chr(random.randint(65, 90))}' \
                 f'{chr(random.randint(65, 90))} {random.randint(1000, 9999)}'
    user_id = random.randint(1, 30)
    time_in = fake.date_time_between(start_date="-1y", end_date="now")
    time_out = time_in + timedelta(hours=random.randint(1, 10))
    cursor.execute("""
    INSERT INTO vehicles (vehicle_id, vehicle_type_id, license_no, user_id, time_in, time_out)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (i+1, vehicle_type_id, license_no, user_id, time_in, time_out))
db.commit()

# sleep for s seconds
time.sleep(s)

# create fare_details
cursor.execute("""
CREATE TABLE IF NOT EXISTS fare_details (
    fare_id INT PRIMARY KEY,
    vehicle_type_id INT,
    fare VARCHAR(255),
    FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_type(vehicle_type_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
""")
db.commit()

# insert fare_details data
fare_data = [
    (1, 1, 'Rs 10'),
    (2, 2, 'Rs 20'),
    (3, 3, 'Rs 25'),
    (4, 4, 'Rs 30')
]
cursor.executemany("INSERT INTO fare_details (fare_id, vehicle_type_id, fare) VALUES (%s, %s, %s)", fare_data)
db.commit()

# sleep for s seconds
time.sleep(s)

# create payment
cursor.execute("""
CREATE TABLE IF NOT EXISTS payment (
    payment_id INT PRIMARY KEY,
    payment_type VARCHAR(255),
    vehicle_id INT,
    amount VARCHAR(255),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
""")
db.commit()

# Generate dummy payment data and insert
for i in range(n):
    payment_type = fake.random_element(elements=("Credit Card", "Cash", "Mobile Wallet"))
    vehicle_id = i + 1
    amount = f'Rs {fake.random_int(min=10, max=800)}'
    cursor.execute("""
    INSERT INTO payment (payment_id, payment_type, vehicle_id, amount)
    VALUES (%s, %s, %s, %s)
    """, (i+1, payment_type, vehicle_id, amount))
db.commit()

# sleep for s seconds
time.sleep(s)

# Create parking_table
cursor.execute("""
CREATE TABLE IF NOT EXISTS parking_table (
    parking_number INT PRIMARY KEY,
    floor_number INT CHECK(floor_number IN (1, 2, 3, 4)),
    vehicle_id INT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
""")
db.commit()

# Generate dummy parking data and insert
for i in range(n):
    parking_number = i + 1
    floor_number = random.choice([1, 2, 3, 4])
    vehicle_id = random.randint(1, n)  
    cursor.execute("""
    INSERT INTO parking_table (parking_number, floor_number, vehicle_id)
    VALUES (%s, %s, %s)
    """, (parking_number, floor_number, vehicle_id))
db.commit()

# close database connection
cursor.close()
db.close()
