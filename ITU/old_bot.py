from state import Observation
from utils import Range


class Bot:
    def get_name(self):
        return "MyOldBot"

    def act(self, obs: Observation):
        good_cards = Range(
            "22+, A2s+, K2s+, Q2s+, J2s+, T5s+, 96s+, 86s+, 75s+, A2o+, K5o+, Q7o+, J8o+, T8o+"
        )
        if (good_cards.is_hand_in_range(obs.my_hand)):
            my_hand = obs.get_my_hand_type()
            board = obs.get_board_hand_type()

            if my_hand > board:
                if (my_hand > 7):
                    return obs.get_max_raise()
                if (my_hand > 4):
                    if (obs.get_min_raise() * 3 < obs.get_max_raise()):
                        return obs.get_min_raise() * 3
                    else:
                        return obs.get_max_raise()
                return obs.get_min_raise()
            else:
                return 1

        return 0