from state import Observation
from utils import Range, HandType
from math import sqrt


class Bot:
    def get_name(self):
        return "Hellmuth"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1
        return bet

    def get_hand_percentage(self, obs: Observation):
        my_hand = obs.my_hand
        if Range("99+, AJs+, KQs, AKo").is_hand_in_range(my_hand):
            return 5
        if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):
            return 10
        if Range("66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+").is_hand_in_range(my_hand):
            return 15
        if Range("55+, A3s+, K7s+, Q8s+, J9s+, T9s, A9o+, KTo+, QJo").is_hand_in_range(my_hand):
            return 20
        if Range("55+, A2s+, K5s+, Q8s+, J8s+, T9s, A8o+, K9o+, QTo+, JTo").is_hand_in_range(my_hand):
            return 25
        if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand):
            return 30
        return 100
        if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(my_hand):
            return 40
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T5s+, 96s+, 86s+, 75s+, A2o+, K5o+, Q7o+, J8o+, T8o+").is_hand_in_range(my_hand):
            return 50
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 94s+, 84s+, 74s+, 64s+, 54s, A2o+, K3o+, Q5o+, J7o+, T7o+, 97o+").is_hand_in_range(my_hand):
            return 60
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 73s+, 63s+, 53s+, 43s, A2o+, K2o+, Q3o+, J5o+, T6o+, 97o+, 86o+").is_hand_in_range(my_hand):
            return 70
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J3o+, T5o+, 95o+, 86o+, 75o+, 65o").is_hand_in_range(my_hand):
            return 80
        return 100

    def act(self, obs: Observation):
        hand_percentage = self.get_hand_percentage(obs)

        if obs.current_round == 0:
            if hand_percentage <= 15:
                return self.bet(obs.get_min_raise(), obs)
            if hand_percentage <= 30 and obs.get_max_spent() <= obs.big_blind * 3:
                return 1
        else:
            if obs.get_my_hand_type() > HandType.PAIR and obs.get_my_hand_type().value > obs.get_board_hand_type().value + 1:
                return obs.get_max_raise()

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
