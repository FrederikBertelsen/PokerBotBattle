from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "Hercules"


    def act(self, obs: Observation):
        hand_type = obs.get_my_hand_type()
        my_hand = obs.my_hand
        call_size = obs.get_call_size()
        min_raise = obs.get_min_raise()
        max_raise = obs.get_max_raise()
        big_blind = obs.big_blind

        if obs.current_round == 0:
            if hand_type == HandType.PAIR:
                return min_raise

            if Range("99+, AJs+, KQs").is_hand_in_range(my_hand):  # 4%
                return min_raise * 4
            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
                return min_raise * 2

            if Range("77+, A7s+, K9s+, QTs+, JTs, AJo+, KQo").is_hand_in_range(my_hand) \
                    and call_size < big_blind * 3:  # 12%
                return 1
            if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
                    and call_size <= big_blind:  # 30%
                return 1

        my_hand_type = obs.get_my_hand_type()
        hand_better = my_hand_type.value > obs.get_board_hand_type().value + 1
        if my_hand_type > HandType.PAIR and hand_better:
            return max_raise

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
