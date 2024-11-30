class SimpleReflexAgent:
    def __init__(self, threshold):
        self.threshold = threshold
        self.action = None
    def perceive(self, temperature):
        if temperature < self.threshold:
            self.action = "Turn on the heater"
        else:
            self.action = "Turn off the heater"
    def act(self):
        return self.action
rooms = {
    "Living Room": 28,
    "Bedroom": 18,
    "Kitchen": 32,
}
agent = SimpleReflexAgent(22)
for room_name, temp in rooms.items():
    agent.perceive(temp)
    print(f"{room_name} (Temp: {temp}) ==> {agent.act()}")
