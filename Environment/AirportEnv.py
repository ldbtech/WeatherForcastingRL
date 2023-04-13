import numpy as np
import socket
from Apis.WeatherApi import setupWeather
from Apis.FlightAPI import flightapi


class Airport:
    """
    # Airport Environment Description:
    This environment corresponds to a weather prediction in order to decide what state airport should proceeed with.
    We will have two dataset, one is climate change (Weather change) in Buffalo, second one will be realtime
    data of weather.

    We have to train the environment to send the right order to pilots.
    We will not need to train AirplaneEnv since, it is just a simulation. We will just collect long/lat and distance.

    # Action Space: is an ndarray with shape `(1, )` which can take a value of 0, 1, 2.
    | Num | Action       |
    | --- | -------------|
    | 0   |
    | 1   |
    | 2   |
    # Observation Space:

    # Reset Method

    # Step Method
    Step method based on action value passed to it. Environment will send to the airplane environment
    if he should land, not fly (Delay) or Send them to a new airport.

    # SELECT NEW AIRPORT:
    This method, will look for near by airport that is safe to land. Will look around Airplane location and fuel.

    #

    """

    def __init__(self, port, airport_ip):
        self.observation_space = {1: "Wind_Speed", 2: "Temperature", 3: "Precipitation"}

        self.action_space = {0: "Delay", 1: "cancel", 2: "Proceed", 3: "Redirect"}
        self.port = port
        self.airport_ip = airport_ip
        self.packet = {}

    def socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def reset(self):
        self.total_rewards = 0
        self.reward = 0
        self.socket()
        self.sock.connect((self.airport_ip, self.port))

    def step(self, action):
        self.sock.send(str(action).encode())
        self.action(action=action)

    def action(self, action):
        response = self.sock.recv(self.port).decode()
        if response == "Ready":  # if there is plane ready to land.
            # if the wind is below 30mph and temp is above freezing F.
            if self.packet[1] < 30 and self.packet[2] > 32:
                self.sock.send("safe".encode())
                self.packet = self.sock.recv(self.port).encode()
            elif self.packet[1] >= 30 and self.packet[2] <= 32:
                self.sock.send("changeAirport".encode())
                self.packet = self.sock.recv(self.port).encode()
            elif self.packet[3] > 50:
                self.sock.send("Grounded".encode())
                self.packet = self.sock.recv(self.port).encode()
        if response == "changeAirport":
            new_airport = self.select_new_airport()
            self.sock.send(str(new_airport).encode())
            self.calculate_reward()
        elif response == "Delay":
            pass

    def calculate_reward(self, action):
        reward = 0
        # Get the current observation
        wind_speed = self.packet[1]
        temperature = self.packet[2]
        precipitation = self.packet[3]

        # If the action is to land
        if action == 1:
            # If the weather is safe for landing
            if wind_speed < 30 and temperature > 32:
                reward += 100  # incentivize safe landing
            else:
                reward -= 100  # penalize unsafe landing

        # If the action is to cancel the flight
        if action == 1:
            reward -= 50  # penalize cancellations

        # If the action is to delay the flight
        if action == 0:
            reward -= 20  # penalize delays

        return reward

    def select_new_airport(self):
        return {}
