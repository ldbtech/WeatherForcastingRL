import gymnasium as gym
from Apis.WeatherApi import setupWeather
from Apis.FlightAPI import flightapi
import numpy as np
from sklearn.model_selection import train_test_split


class AirportEnv(gym.Env):
    def __init__(self, weather_api, weather_data, flight_delay_data):
        self.observation_space = gym.spaces.Discrete(4)
        self.action_space = gym.spaces.Discrete(2)

        # Train the model that Joel Solomone and Miheer Made. (Random Forest).
        self.model = None
        X_train, X_test, y_train, y_test = train_test_split(
            weather_data, flight_delay_data, test_size=0.2, random_state=42
        )
        # Train in here
        self.weather_api = weather_api
        self.current_weather = setupWeather()

        # Predict based on the current weather if flight should be delayed or not.
        prediction = self.model.predict(self.current_weather.reshape(1, -1))[0]

    def reset(self):
        self.total_rewards = 0
        self.reward = 0
        # Return the current state of the weather..
        return self.current_weather

    def step(self, action):
        # 1 - Delayed, 2 - No Delayed
        if action == 1:
            pass
        if action == 2:
            pass

    def computeRewards(
        self,
        action,
    ):
        wind_speed = self.current_weather[0]
        temperature = self.current_weather[1]
        percipitation = self.current_weather[2]
        overall_weather_condition = self.current_weather[3]

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

        reward -= wind_speed * WIND_SPEED_FACTOR
        reward -= temperature * TEMPERATURE_FACTOR
        reward -= percipitation * PERCIPITATION_FACTOR
        reward -= overall_weather_condition * OVERALL_WEATHER_CONDITION_FACTOR

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
