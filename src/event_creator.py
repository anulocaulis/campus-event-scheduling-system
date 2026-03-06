# functions to create campus events at random
# Both linked list and array implementation can call this script

class Event:
    def __init__(self, id, title, date, time, location):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.location = location

    def __repr__(self):
        return f"Event({self.id}, {self.title}, {self.date}, {self.time}, {self.location})"


# Create a unique ID
import random

def unique_ID():
