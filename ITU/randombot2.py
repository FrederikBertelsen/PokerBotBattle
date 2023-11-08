from random import choice
from state import Observation


class Bot:
    def get_name(self):
        return "---------- randomBot 2 ----------"

    def act(self, observation: Observation):
        return choice(observation.legal_actions)
