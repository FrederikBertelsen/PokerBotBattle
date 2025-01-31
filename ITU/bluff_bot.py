from state import Observation
from utils import Range, HandType
"""
  This bot will always raise the pot with it's entire cash stack (going "all-in")
"""


class Bot:
    def get_name(self):
        return "bluff_bot"

    def act(self, obs: Observation):
        return obs.get_max_raise()