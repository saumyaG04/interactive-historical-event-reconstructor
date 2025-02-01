from event_fetcher import fetch_events
from simulator import simulate_event
from rich.console import Console

def run_interactive_cli():
    console = Console()

    console.print("Welcome to the Interactive Historical Event Reconstructor!", style="bold green")

    while True:
        # User Input for Event Search
        event_name = console.input("Enter the event name (or 'exit' to quit): ")
        
        if event_name.lower() == "exit":
            console.print("Exiting... Goodbye!", style="bold red")
            break

        # Fetch matching events
        events = fetch_events(event_name)
        print("DEBUG: Events fetched:", events)  # Debugging statement

        if events and isinstance(events, list):  # Ensure it's a list
            console.print(f"Found {len(events)} event(s) matching '{event_name}':", style="bold yellow")
            for event in events:
                # Use .get() to avoid KeyErrors
                event_name = event.get("event", event.get("name", "Unknown Event"))
                event_year = event.get("year", "Unknown Year")
                event_desc = event.get("description", "No description available")

                console.print(f"{event_name} ({event_year}) - {event_desc}")
        else:
            console.print(f"No events found for '{event_name}'. Try again.", style="bold red")
            continue
        
        # Optional: Run simulation on the event
        simulate = console.input("Would you like to simulate an alternate history for this event? (yes/no): ").strip().lower()
        if simulate == "yes":
            simulate_event(event_name)

if __name__ == "__main__":
    run_interactive_cli()

