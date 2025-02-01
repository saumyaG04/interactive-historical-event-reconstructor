

from models.database import get_db

def fetch_events(event_name):
    db = get_db()
    events_collection = db.events
    
    # Search for events that contain the input name
    events = events_collection.find({"name": {"$regex": event_name, "$options": "i"}})

    return list(events)  # Convert the cursor to a list
