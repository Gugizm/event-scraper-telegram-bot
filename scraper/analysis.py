from datetime import datetime, time

class DecisionMaker:
    def __init__(self, events):
        self.events = events


    def decision(self):
        event_time_list = []
        for event in self.events:
            time_str = event['time']
            parsed_time = datetime.strftime(time_str, "%H:%M").time()
            event_time_list.append(parsed_time)

    @staticmethod
    def parsed_time(times):
