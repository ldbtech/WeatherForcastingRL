import gymnasium as gym
from Training.weather_flight_data import weather_flight_data, get_weather_flight
import numpy as np
import pickle


class AirportEnv(gym.Env):
    def __init__(self, weather_api, max_flights=10):
        self.observation_space = gym.spaces.Discrete(4)
        self.action_space = gym.spaces.Discrete(2)

        # Train the model that Joel Solomone and Miheer Made. (Random Forest).
        self.model = pickle.load(open("modelpred.pkl", "rb"))
        # Test Data - 600 flights (rows)
        self.test_data = weather_flight_data()

        # it is like data to consider in stock market environment. Flight to consider.
        self.max_flights = min(max_flights, len(self.test_data))
        self.current_flight = 0
        self.current_weather = get_weather_flight(self.current_flight, self.test_data)

        self.timestep = 0
        self.reset()

    def reset(self):
        self.total_rewards = 0
        self.reward = 0
        self.done = False
        self.current_flight = 0
        self.n_flight += 1
        self.current_weather = self.get_weather_for_flight(self.current_flight)
        # Return the current state of the weather..
        return self.current_weather

    def step(self, action):
        # Timestep can be configured to reflect how many flights are about to take off.
        # Take an action.
        # self.action(act=action)
        # This is for computing the rewards based on action.
        self.reward = self.computeRewards(action=action)
        print("ACtion: ", action)
        self.n_flight = self.current_flight
        if self.n_flight >= self.max_flights - 1:
            self.done = True
        else:
            self.done = False

        info = {"Flight": self.n_flight}

        return self.current_weather, self.reward, self.done, info

    def computeRewards(
        self,
        action,
    ):
        wind_speed = self.current_weather[4]
        temperature = self.current_weather[3]
        percipitation = self.current_weather[0]
        overall_weather_condition = self.current_weather[2]

        prediction = self.model.predict(self.current_weather.reshape(1, -1))[0]

        if action == prediction:
            self.reward += 10
        else:
            self.reward -= 10
        # Calculating rewards
        # Additional factors based on the weather conditions
        WIND_SPEED_FACTOR = 0.1
        TEMPERATURE_FACTOR = 0.05
        PERCIPITATION_FACTOR = 0.2
        OVERALL_WEATHER_CONDITION_FACTOR = 0.5

        self.reward -= wind_speed * WIND_SPEED_FACTOR
        self.reward -= temperature * TEMPERATURE_FACTOR
        self.reward -= percipitation * PERCIPITATION_FACTOR
        self.reward -= overall_weather_condition * OVERALL_WEATHER_CONDITION_FACTOR

        # Penalize if the flight is not delayed, but there is a safety issue
        HAZARDOUS_WEATHER_THRESHOLD = 3
        if overall_weather_condition >= HAZARDOUS_WEATHER_THRESHOLD and action == 2:
            SAFETY_PENALTY = -5
            self.reward += SAFETY_PENALTY
        return self.reward

    def render(self, render_type):
        if render_type == "fake_data":
            pass
        if render_type == "realtime_data":
            pass
