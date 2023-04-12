
import numpy as np
class Airport: 
    """
        # Airport Environment Description: 
        This environment corresponds to a weather prediction in order to decide what state airport should proceeed with. 

        # Action Space: is an ndarray with shape `(1, )` which can take a value of 0, 1, 2. 
        | Num | Action       |
        | --- | -------------|
        | 0   |
        | 1   |
        | 2   |
        # Observation Space: 
        | Num | Observation           | Min                 | Max               |
        |-----|-----------------------|---------------------|-------------------|
        | 0   | Cart Position         | -4.8                | 4.8               |
        | 1   | Cart Velocity         | -Inf                | Inf               |
        | 2   | Pole Angle            | ~ -0.418 rad (-24°) | ~ 0.418 rad (24°) |
        | 3   | Pole Angular Velocity | -Inf                | Inf               |

    """
    def __init__(self):
        self.observation_space = {1: 'Wind_Speed',
                                  2: 'Temperature', 
                                  3: 'Precipitation'}
        
        self.action_space = {0: 'Delay', 
                             1: 'cancel', 
                             2:'Proceed'}

    def reset(self):
        pass

    def step(self, action):
        pass

    def action(self, action):
        if (action == 0): # Fly 
            pass
        if action == 1: # Land 
            pass
        if action == 2: # Delay (Grounded)
            pass
    
    def render(self, rendering_type): # can be web or pygame.
        pass 
