from pymongo import MongoClient

# Connect to MongoDB (Ensure MongoDB is running)
client = MongoClient("mongodb://localhost:27017/")
db = client["historyDB"]
events_collection = db["events"]

# Sample list of 100 historical events
historical_events = [
    {"event_id": 1, "name": "Battle of Hastings", "year": 1066, "location": "England",
     "description": "William the Conqueror defeats King Harold II, establishing Norman rule in England.",
     "factors": ["Superior strategy", "Archery tactics"], "outcome": "Norman rule begins in England.",
     "tags": ["war", "England", "medieval"]},

    {"event_id": 2, "name": "Fall of Constantinople", "year": 1453, "location": "Turkey",
     "description": "The Ottoman Empire captures Constantinople, marking the end of the Byzantine Empire.",
     "factors": ["Cannons", "Naval blockade"], "outcome": "Ottoman control of Eastern Europe.",
     "tags": ["war", "Ottoman Empire", "Byzantine"]},

    {"event_id": 3, "name": "American Revolution", "year": 1775, "location": "USA",
     "description": "Colonists revolt against British rule, leading to the formation of the United States.",
     "factors": ["Taxation", "Desire for independence"], "outcome": "USA gains independence in 1783.",
     "tags": ["war", "USA", "revolution"]},

    {"event_id": 4, "name": "French Revolution", "year": 1789, "location": "France",
     "description": "A social and political revolution that overthrew the monarchy.",
     "factors": ["Economic crisis", "Monarchy corruption"], "outcome": "Rise of democracy, fall of monarchy.",
     "tags": ["revolution", "France", "politics"]},

    {"event_id": 5, "name": "Industrial Revolution", "year": 1760, "location": "England",
     "description": "A period of technological advancement that transformed industries.",
     "factors": ["Steam engine", "Factory system"], "outcome": "Urbanization, modern economy.",
     "tags": ["technology", "economy", "industrial"]},

    {"event_id": 6, "name": "World War I", "year": 1914, "location": "Worldwide",
     "description": "A global war triggered by assassination and complex alliances.",
     "factors": ["Alliances", "Militarism"], "outcome": "Treaty of Versailles, League of Nations.",
     "tags": ["war", "Europe", "global"]},

    {"event_id": 7, "name": "World War II", "year": 1939, "location": "Worldwide",
     "description": "A global conflict between Axis and Allied powers.",
     "factors": ["Nazi expansion", "Pearl Harbor attack"], "outcome": "Formation of the UN, Cold War begins.",
     "tags": ["war", "global", "politics"]},

    {"event_id": 8, "name": "Moon Landing", "year": 1969, "location": "USA",
     "description": "Apollo 11 lands humans on the Moon for the first time.",
     "factors": ["Cold War space race", "NASA technology"], "outcome": "Advancement in space exploration.",
     "tags": ["space", "technology", "USA"]},

    {"event_id": 9, "name": "Fall of the Berlin Wall", "year": 1989, "location": "Germany",
     "description": "The Berlin Wall is torn down, leading to German reunification.",
     "factors": ["End of Cold War", "Gorbachev reforms"], "outcome": "Germany reunifies in 1990.",
     "tags": ["politics", "Germany", "Cold War"]},

    {"event_id": 10, "name": "COVID-19 Pandemic", "year": 2020, "location": "Worldwide",
     "description": "A global pandemic caused by the SARS-CoV-2 virus.",
     "factors": ["Global travel", "Virus mutation"], "outcome": "Lockdowns, vaccine development.",
     "tags": ["health", "global", "pandemic"]},
]

# Insert data into MongoDB
events_collection.insert_many(historical_events)
print("Database populated with historical events!")
