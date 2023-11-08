from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "BOTIMUS PRIME"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1
        return bet

    def act(self, obs: Observation):
        hand = obs.get_my_hand_type()
        min = obs.get_min_raise()
        hand_better = hand.value > obs.get_board_hand_type().value + 1

        if obs.current_round == 0:
            if hand >= HandType.PAIR:
                if min > 300:
                    if Range("TT+, AKs").is_hand_in_range(obs.my_hand):
                        return 1
                    else:
                        return 0
                return obs.get_min_raise()

            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(obs.my_hand):
                return 1
            else:
                return 0

        if hand > HandType.PAIR and hand_better:
            return self.bet(obs.get_max_raise(), obs)
        elif hand == HandType.PAIR and hand_better:
            return self.bet(obs.get_min_raise(), obs)

        return 0
