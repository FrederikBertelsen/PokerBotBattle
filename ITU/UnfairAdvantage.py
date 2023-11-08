from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "Unfair Advantage"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1
        return bet

    def act(self, obs: Observation):
        my_hand_type = obs.get_my_hand_type()
        my_hand = obs.my_hand
        call_size = obs.get_call_size()
        min_raise = obs.get_min_raise()
        max_raise = obs.get_max_raise()
        big_blind = obs.big_blind

        if obs.current_round == 0:
            if Range("99+, AJs+, KQs").is_hand_in_range(my_hand):  # 4%
                if call_size < big_blind * 6:
                    return self.bet(big_blind * 2, obs)
                else:
                    return 1
            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
                if call_size < big_blind * 3:
                    return self.bet(big_blind, obs)
                else:
                    return 1
            if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(my_hand) \
                    and call_size < big_blind * 3:  # 40%
                return 1
            if Range("33+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, A2o+, K2o+, Q2o+, J3o+, T5o+, 95o+, 86o+, 75o+, 65o").is_hand_in_range(my_hand) \
                    and call_size <= big_blind * 2:  # 80%
                return 1
        else:
            hand_better = my_hand_type.value > obs.get_board_hand_type().value + 1
            if my_hand_type > HandType.PAIR and hand_better:
                return max_raise

            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand) \
                    and call_size < big_blind * 10:  # 10%
                return 1
            if Range("22+, A2s+, K2s+, Q2s+, J2s+, T5s+, 96s+, 86s+, 75s+, A2o+, K5o+, Q7o+, J8o+, T8o+").is_hand_in_range(my_hand) \
                    and call_size < big_blind * 6:  # 50%
                return 1

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
