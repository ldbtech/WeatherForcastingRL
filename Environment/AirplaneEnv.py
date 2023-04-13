class AirplaneEnv:
    """
    # Flight Parameters:
     - This will come mostly from API that takes every flight parameters that its destination is JFK.
     -

    """

    def __init__(self):
        self.action_space = 4
        self.state_space = None
        self.flightParameters = {
            "lat": 0.0,
            "long": 0.0,
            "speed": 0.0,
            "distance": 0.0,
            "landingLoc": None,
        }

    def reset(self):
        pass

    def step(self, action):
        pass

    def action(self, act):
        pass

    def render(self):
        pass
