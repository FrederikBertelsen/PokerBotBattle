from utils import HandType
from state import Observation


class Bot:
    def get_name(self):
        return "EMIL Pair"

    def act(self, obs: Observation):
        hand_type = obs.get_my_hand_type()
        if hand_type == HandType.PAIR:
            return obs.get_max_raise()
        return 0
