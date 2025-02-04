# Event class with participant tracking
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initially, no participants

    # Method to add a participant
    def add_participant(self):
        self.participant_count += 1
        print(f"A new participant has been added. Current participant count: {self.participant_count}")

    # Method to get the current participant count
    def get_participant_count(self):
        return self.participant_count

# Creating an instance of Event
event1 = Event("Tech Conference", "2025-06-15")

# Demonstrating adding participants
event1.add_participant()  # Adding one participant
event1.add_participant()  # Adding another participant

# Retrieving and displaying the current participant count
print(f"Total participants in {event1.name}: {event1.get_participant_count()}")
