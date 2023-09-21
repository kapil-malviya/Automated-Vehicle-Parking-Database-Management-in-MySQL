---

#                                               Vehicle Parking Database Management in MySQL

This project is a comprehensive Vehicle Parking Database Management system developed using MySQL, Python, and the Faker library. It allows you to create and manage a vehicle parking database effortlessly.

## Overview

This project automates the setup of a MySQL database for vehicle parking management. By running the Python script provided, you can create all the necessary tables and populate them with dummy data using Faker. This streamlines the process of setting up of the Database Tables and inserting dummy entries.

## Requirements

Before getting started, ensure that you have the following requirements met:

- Python 3.10 installed on your system.
- A MySQL server installed and running.
- The `mysql-connector-python` package installed. You can install it using ```pip install mysql-connector-python```.
- Access to your MySQL server with the necessary privileges to create databases and tables.

## Getting Started

Follow these steps to set up and run the Vehicle Parking Database Management system:

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/kapil-malviya/Automated-Vehicle-Parking-Database-Management-in-MySQL.git
   ```

2. Navigate to the project directory:

   ```
   cd Automated-Vehicle-Parking-Database-Management-in-MySQL
   ```

3. Open the `parking_management_script.py` file and update the database connection details, including your MySQL username and password.

4. Execute the Python script to create the database and populate it with dummy data:

   ```
   python3 parking_management_script.py
   ```

   This script will create the necessary tables and populate them with dummy data for testing.

5. You can now use the database for vehicle parking management.

## Project Structure

- `parking_management_script.py` : Configuration and SQL Query file where you specify your MySQL connection details and queries responsible for creating the MySQL database, tables, and populating them with dummy data.
- `requirements.txt` : Lists the project dependencies. You can install them using `pip install -r requirements.txt`.

## Contribution

Contributions to enhance and expand the functionality of this database management system are welcome. Feel free to fork the repository, make your changes, and submit a pull request.
