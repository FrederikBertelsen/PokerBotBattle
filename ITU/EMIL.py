from state import Observation


class Bot:
    def get_name(self):
        return "EMIL"

    def act(self, obs: Observation):
        hand = obs.my_hand
        for i in range(len(hand)):
            if "A" in hand[i]:
                return obs.get_max_raise()
        return 0
