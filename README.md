# Project_4_Guest_House_Management_System-_CRUD_Additional_Functionalities_-3-
This project was assigned  to me during Kiran academy's  Python Internship Course it is  a simple Guest House Management System built in Python using the Command Line Interface (CLI). It performs CRUD operations (Create, Read, Update, Delete) along + functionalities like bill generation and search, designed for managing small guesthouse
# Guest House Management System (Python CLI Project)

This is a simple Guest House Management System built in Python using the Command Line Interface (CLI). It allows you to manage room bookings for a guest house using basic Python data structures and operations.

## Features

- Create Booking: Book a room with customer details, room type, and stay duration.
- View All Bookings: Display all current bookings.
- Update Booking: Modify existing booking information.
- Delete Booking: Cancel and remove a room booking.
- Check Room Availability: View current status of all rooms.
- Generate Bill: Calculate total cost based on room type and number of nights.
- Search Booking by Name: Find bookings by customer name.
- Exit: Close the application.

## Room Types and Pricing

| Room Type         | Price per Night (₹) |
|-------------------|---------------------|
| Single Non-AC     | 1000                |
| Single AC         | 1500                |
| Double Non-AC     | 1800                |
| Double AC         | 2500                |

## Data Structures Used

- `bookings` (dictionary): Stores room numbers as keys and customer booking details as values.
- `RoomStatus` (dictionary): Tracks the availability status of each room.
- `RoomPrices` (dictionary): Contains room type and price mapping.

## Tech Stack

- Language: Python 3
- Interface: Command Line Interface (CLI)

## How to Run

1. Ensure Python 3 is installed on your system.
2. Clone this repository or save the code in a Python file (e.g., `guest_house.py`).
3. Open your terminal or command prompt.
4. Run the script using the following command:

```bash
python guest_house.py
