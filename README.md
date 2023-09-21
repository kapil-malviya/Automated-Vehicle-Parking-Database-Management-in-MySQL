---

#                                               Vehicle Parking Database Management in MySQL

This project is a comprehensive Vehicle Parking Database Management system developed using MySQL, Python, and the Faker library. It allows you to create and manage a vehicle parking database effortlessly.

## Overview

This project automates the setup of a MySQL database for vehicle parking management. By running the Python script provided, you can create all the necessary tables and populate them with dummy data using Faker. This streamlines the process of setting up and testing the database.

## Requirements

Before getting started, ensure that you have the following requirements met:

- Python 3.x installed on your system.
- A MySQL server installed and running.
- The `mysql-connector-python` package installed. You can install it using `pip install mysql-connector-python`.
- Access to your MySQL server with the necessary privileges to create databases and tables.

## Getting Started

Follow these steps to set up and run the Vehicle Parking Database Management system:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Automated-Vehicle-Parking-Database-Management-in-MySQL.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Automated-Vehicle-Parking-Database-Management-in-MySQL
   ```

3. Open the `config.py` file and update the database connection details, including your MySQL username and password.

4. Execute the Python script to create the database and populate it with dummy data:

   ```bash
   python create_database.py
   ```

   This script will create the necessary tables and populate them with dummy data for testing.

5. You can now use the database for vehicle parking management.

## Project Structure

- `create_database.py`: The Python script responsible for creating the MySQL database, tables, and populating them with dummy data.
- `config.py`: Configuration file where you specify your MySQL connection details.
- `requirements.txt`: Lists the project dependencies. You can install them using `pip install -r requirements.txt`.

## Contribution

Contributions to enhance and expand the functionality of this database management system are welcome. Feel free to fork the repository, make your changes, and submit a pull request.
