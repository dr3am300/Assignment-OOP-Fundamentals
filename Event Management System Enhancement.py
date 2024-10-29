# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
    # class Event:
        # def __init__(self, name, date):
            # self.name = name
            # self.date = date
            
            
            
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
        
    def get_participant_count(self):
        return self.participant_count
    
event1 = Event("Music Concert", "2021-12-25")
event1.add_participant()
event1.add_participant()
event1.add_participant()

print("Event Name:", event1.name)
print("Event Date:", event1.date)
print("Participant Count:", event1.get_participant_count())

event2 = Event("Food Festival", "2021-11-20")
event2.add_participant()
event2.add_participant()

print("\nEvent Name:", event2.name)
print("Event Date:", event2.date)
print("Participant Count:", event2.get_participant_count())


