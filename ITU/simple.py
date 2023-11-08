from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "SIMPLE"

    def act(self, obs: Observation):
        my_hand = obs.get_my_hand_type()
        hand_better = my_hand.value > obs.get_board_hand_type().value + 1

        if my_hand > HandType.PAIR and hand_better:
            return obs.get_max_raise()
        if my_hand == HandType.PAIR and hand_better:
            return obs.get_min_raise()

        if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):
            return obs.get_min_raise()
        if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand):
            return 1
        return 0
