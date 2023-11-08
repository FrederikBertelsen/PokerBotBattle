from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "ThoseAreMyFish"

    def act(self, obs: Observation):

        if obs.current_round == 0:
            # see if A or K in hand
            ak_in_hand = False
            for i in range(2):
                if "K" in obs.my_hand[i] or "A" in obs.my_hand[i]:
                    ak_in_hand = True
                    break

            if obs.get_call_size() > 500:
                if ak_in_hand:
                    return 1
                else:
                    if 0 in obs.legal_actions:
                        return 0
                    else:
                        return 1
            else:
                if Range("99+").is_hand_in_range(obs.my_hand):
                    if obs.get_max_raise() <= obs.get_call_size() * 4:
                        return obs.get_max_raise()
                    else:
                        return min(obs.get_call_size() * 4, obs.get_max_raise())
        else:
            if obs.get_my_hand_type() >= HandType.PAIR:
                return obs.get_max_raise()
            else:
                if obs.get_min_raise() + 10 < obs.get_max_raise():
                    return obs.get_min_raise() + 10
                else:
                    return obs.get_max_raise()

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1