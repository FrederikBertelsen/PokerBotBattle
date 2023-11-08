from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "Simply"

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
        max_raise = obs.get_max_raise()
        big_blind = obs.big_blind

        hand_better = my_hand_type.value > obs.get_board_hand_type().value + 1
        if my_hand_type > HandType.PAIR and hand_better:
            return max_raise

        if Range("99+, AJs+, KQs, AKo").is_hand_in_range(my_hand):  # 5%
            if call_size <= big_blind * 5:
                return self.bet(big_blind * 2, obs)
            else:
                return 1
        if Range("66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+").is_hand_in_range(my_hand):  # 10%
            if call_size <= big_blind * 2:
                return self.bet(big_blind, obs)
            else:
                return 1

        if Range("44+, A2s+, KTs+, K2s-K8s, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
                and call_size <= big_blind * 6:  # 30%
            return 1
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 94s+, 84s+, 74s+, 64s+, 54s, A2o+, K3o+, Q5o+, J7o+, T7o+, 97o+").is_hand_in_range(my_hand) \
                and call_size <= big_blind * 2:  # 60%
            return 1

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
