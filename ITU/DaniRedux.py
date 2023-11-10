from state import Observation
from utils import Range, HandType
from math import sqrt


class Bot:
    def get_name(self):
        return "DaniRedux"

    def get_hand_percentage(self, obs: Observation):
        my_hand = obs.my_hand
        if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(
                my_hand):  # 40%
            if Range("55+, A3s+, K7s+, Q8s+, J9s+, T9s, A9o+, KTo+, QJo").is_hand_in_range(my_hand):  # 20%
                if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
                    if Range("99+, AJs+, KQs, AKo").is_hand_in_range(my_hand):  # 5%
                        return 5
                    return 10
                if Range("66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+").is_hand_in_range(my_hand):  # 15%
                    return 15
                return 20
            if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand):  # 30%
                if Range("55+, A2s+, K5s+, Q8s+, J8s+, T9s, A8o+, K9o+, QTo+, JTo").is_hand_in_range(my_hand):  # 25%
                    return 25
                return 30
            if Range("33+, A2s+, K2s+, Q4s+, J7s+, T7s+, 97s+, 87s, A5o+, K9o+, Q9o+, J8o+").is_hand_in_range(
                    my_hand):  # 35%
                return 35
            return 40
        return 100

    def max_call_function(self, obs: Observation, hand_percentage: int):
        # return (-0.35 * hand_percentage + 15) * obs.big_blind
        return (-0.4 * hand_percentage + 14) * obs.big_blind

    def act(self, obs: Observation):
        if obs.get_my_hand_type() > HandType.PAIR and obs.get_my_hand_type().value > obs.get_board_hand_type().value + 1:
            return obs.get_max_raise()

        hand_percentage = self.get_hand_percentage(obs)
        if obs.get_max_spent() < self.max_call_function(obs, hand_percentage):
            return obs.get_min_raise() if obs.current_round == 0 and hand_percentage <= 15 else 1

        return 0 if 0 in obs.legal_actions else 1
