# Interactive Historical Event Reconstructor

A Python-based CLI tool that allows users to search for historical events and simulate alternate histories based on user input. This project uses MongoDB to store event data and the Rich library to enhance the command-line interface.

## Features

- Search historical events by name.
- Simulate alternate histories for selected events.
- MongoDB integration for storing and retrieving events.
- User-friendly CLI interface powered by Rich.

## Requirements

- Python 3.8+
- MongoDB

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd interactive-historical-event-reconstructor

## Install required dependencies:

pip install -r requirements.txt

## Set up MongoDB:

Make sure MongoDB is running locally or remotely.
Populate the database with historical events by running populate_db.py.

## Configure the MongoDB URI in a .env file:

MONGO_URI=mongodb://localhost:27017/

## Run the application:

python src/main.py

# Usage

Upon starting the app, enter the name of a historical event to search.
If the event is found, you can simulate an alternate history for it.

# Technologies Used

MongoDB: A NoSQL database used for storing event data.
Python: The programming language for building the application.
Rich: A library for creating beautiful command-line interfaces.
pymongo: MongoDB driver for Python.
python-dotenv: Used to load environment variables from the .env file.

# License

This project is licensed under the MIT License.
