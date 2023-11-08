from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "Hermes"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1
        return bet

    def act(self, obs: Observation):
        my_hand = obs.my_hand
        min_raise = obs.get_min_raise()
        big_blind = obs.big_blind
        max_spent = obs.get_max_spent()

        if obs.current_round == 0:
            if Range("66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+").is_hand_in_range(my_hand):  # 15%
                return self.bet(min_raise, obs)
            if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
                    and max_spent <= big_blind * 2:  # 30%
                return 1
        else:
            my_hand_type = obs.get_my_hand_type()
            hand_better = my_hand_type.value > obs.get_board_hand_type().value + 1
            if my_hand_type > HandType.PAIR and hand_better:
                return obs.get_max_raise()

            if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
                    and max_spent <= big_blind * 2:  # 30%
                return 1

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
