import gymnasium
from gymnasium import spaces
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


class AirportEnv(gymnasium.Env):
    def __init__(self, weather_api, weather_data, flight_delay_data):
        super(AirportEnv, self).__init__()

        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            weather_data, flight_delay_data, test_size=0.2, random_state=42
        )

        # Train machine learning model on training set
        self.model = LogisticRegression()
        self.model.fit(X_train, y_train)

        # Define action and observation space
        self.action_space = spaces.Discrete(2)  # 0: keep on schedule, 1: delay flight
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(5,), dtype=np.float32
        )  # 5 weather features

        # Initialize state
        self.weather_api = weather_api
        self.current_weather = self.get_weather()
        self.current_schedule = np.zeros(5)  # 5 flights scheduled

        # Define reward function
        self.reward_range = (0, 1)

    def step(self, action):
        # Update current schedule based on action
        if action == 1:
            self.current_schedule += 1

        # Update state with latest weather data
        self.current_weather = self.get_weather()

        # Use machine learning model to predict flight delays based on weather conditions
        prediction = self.model.predict(self.current_weather.reshape(1, -1))[0]

        # Determine reward based on whether the predicted delay matches the actual delay
        actual_delay = np.sum(self.current_schedule)
        reward = 1 if prediction == actual_delay else 0

        # Update info dictionary with current state and reward
        info = {
            "current_weather": self.current_weather,
            "current_schedule": self.current_schedule,
            "reward": reward,
        }

        return self.current_weather, reward, False, info

    def reset(self):
        # Reset state to initial values
        self.current_weather = self.get_weather()
        self.current_schedule = np.zeros(5)

        return self.current_weather

    def get_weather(self):
        # Query weather API for latest weather data
        weather_data = self.weather_api.query()
        # Normalize weather data to range [0, 1]
        normalized_weather_data = (weather_data - np.min(weather_data)) / (
            np.max(weather_data) - np.min(weather_data)
        )

        return normalized_weather_data
