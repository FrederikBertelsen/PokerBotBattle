from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "DaniRedux"

    def __init__(self):
        self.ranges = {
            5: "99+, AJs+, KQs, AKo",
            10: "77+, A9s+, KTs+, QJs, AJo+, KQo",
            15: "66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+",
            20: "55+, A3s+, K7s+, Q8s+, J9s+, T9s, A9o+, KTo+, QJo",
            25: "55+, A2s+, K5s+, Q8s+, J8s+, T9s, A8o+, K9o+, QTo+, JTo",
            30: "44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo",
            35: "33+, A2s+, K2s+, Q4s+, J7s+, T7s+, 97s+, 87s, A5o+, K9o+, Q9o+, J8o+",
            40: "33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o"
        }


def is_hand_in_range(self, my_hand: tuple[str], target_percentage: int):
    return Range(self.ranges.get(target_percentage)).is_hand_in_range(my_hand)


def get_hand_percentage(self, obs: Observation):
    my_hand = obs.my_hand
    if self.is_hand_in_range(my_hand, 40):
        if self.is_hand_in_range(my_hand, 20):
            if self.is_hand_in_range(my_hand, 10):
                return 5 if self.is_hand_in_range(my_hand, 5) else 10
            return 15 if self.is_hand_in_range(my_hand, 15) else 20
        if self.is_hand_in_range(my_hand, 30):
            return 25 if self.is_hand_in_range(my_hand, 25) else 30
        return 35 if self.is_hand_in_range(my_hand, 35) else 40
    return 100


def act(self, obs: Observation):
    if obs.get_my_hand_type() > HandType.PAIR and obs.get_my_hand_type().value > obs.get_board_hand_type().value + 1:
        return obs.get_max_raise()

    hand_percentage = self.get_hand_percentage(obs)
    if obs.get_max_spent() < (-0.3 * hand_percentage + 15) * obs.big_blind:
        return obs.get_min_raise() if obs.current_round == 0 and hand_percentage <= 15 else 1

    return 0 if 0 in obs.legal_actions else 1
