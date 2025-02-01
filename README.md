Interactive Historical Event Reconstructor
A Python CLI tool that allows users to search historical events stored in MongoDB and simulate alternate histories for them.

Features
Search for historical events by name.
Simulate alternate outcomes for selected events.
User-friendly interface powered by Python's Rich library.
MongoDB for storing and fetching event data.
Requirements
Python 3.8+
MongoDB
Installation
Clone the repository:

bash
Copy
Edit
git clone <repo_url>
cd interactive-historical-event-reconstructor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up MongoDB and create the database:

Ensure MongoDB is running locally or remotely.
Populate the database with historical events using populate_db.py.
Configure environment variables in a .env file:

plaintext
Copy
Edit
MONGO_URI=mongodb://localhost:27017/
Run the app:

bash
Copy
Edit
python src/main.py
Usage
When the app starts, enter the name of a historical event to search.
If the event is found, you can simulate an alternate history for it.
Technologies Used
MongoDB: NoSQL database for storing event data.
Python: Programming language.
Rich: Library for creating attractive command-line interfaces.
pymongo: MongoDB driver for Python.
dotenv: To load environment variables from the .env file.
License
This project is licensed under the MIT License.

