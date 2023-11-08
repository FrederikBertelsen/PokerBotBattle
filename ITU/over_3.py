from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "over 3 bot"

    def act(self, obs: Observation):
        my_hand = obs.get_my_hand_type()
        board = obs.get_board_hand_type()


        if obs.current_round == 0:  # preflop
            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(obs.my_hand) or my_hand >= HandType.PAIR:
                return 1
            else:
                return 0

        if my_hand > board+1:
            if my_hand >= HandType.THREEOFAKIND:
                return obs.get_max_raise()
            if my_hand >= HandType.PAIR:
                return obs.get_min_raise()
            return obs.get_min_raise()
        else:
            return 1
