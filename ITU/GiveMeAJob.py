from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "Give Me A Job!"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1

        return bet

    def act(self, obs: Observation):
        my_hand = obs.my_hand
        call_size = obs.get_call_size()
        min_raise = obs.get_min_raise()
        max_raise = obs.get_max_raise()
        big_blind = obs.big_blind

        # opening
        if obs.current_round == 0:
            # if Range("99+, AJs+, KQs").is_hand_in_range(my_hand):  # 4%
            #     if call_size < big_blind * 6:
            #         return self.bet(big_blind * 2, obs)
            #     else:
            #         return 1
            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
                if call_size < big_blind * 3:
                    return self.bet(min_raise, obs)
                else:
                    return 1
            # if Range("77+, A7s+, K9s+, QTs+, JTs, AJo+, KQo").is_hand_in_range(my_hand) \
            #         and call_size < big_blind * 3:  # 12%
            #     return 1
            if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
                    and call_size <= big_blind * 3:  # 30%
                return 1

        else:
            my_hand_type = obs.get_my_hand_type()
            hand_much_better = my_hand_type.value > obs.get_board_hand_type().value + 1

            if my_hand_type > HandType.PAIR and hand_much_better:
                return max_raise

            # if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand) \
            #         and obs.get_max_spent() <= big_blind:  # 30%
            #     return 1

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
