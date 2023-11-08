from state import Observation
from utils import Range, HandType


class Bot:
    def get_name(self):
        return "NewBot"

    def bet(self, bet: int, obs: Observation, all_in=True):
        if bet > obs.get_max_raise():
            if all_in:
                return obs.get_max_raise()
            return 1

        # pot_size = context['pot']
        # max_pot_size = context['pot'] + stack_size + self.check_stack_size(context, bot, our_stack=False)
        # risk = sqrt(
        #     (4 / 3.0) *
        #     ((bet_size * (2 * bet_size + pot_size)) /
        #      (max_pot_size * (bet_size + pot_size)))
        # )

        return bet

    def act(self, obs: Observation):
        my_hand_type = obs.get_my_hand_type()
        my_hand = obs.my_hand
        call_size = obs.get_call_size()
        min_raise = obs.get_min_raise()
        max_raise = obs.get_max_raise()
        big_blind = obs.big_blind
        max_spent = obs.get_max_spent()

        if obs.current_round == 0:
            if Range("99+, AJs+, KQs, AKo").is_hand_in_range(my_hand):  # 4%
                return self.bet(min_raise * 4, obs)
            if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
                return self.bet(min_raise * 2, obs)
            # 12 before
            if Range("55+, A3s+, K7s+, Q8s+, J9s+, T9s, 75s, 63s-64s, 52s, A9o+, KTo+, QJo").is_hand_in_range(my_hand) \
                    and max_spent <= big_blind * 4:  # 20%
                return 1
            if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(my_hand) \
                    and max_spent <= big_blind * 2:  # 40%
                return 1
        else:
            if my_hand_type > HandType.PAIR and my_hand_type.value > obs.get_board_hand_type().value + 1:
                return obs.get_max_raise()

            if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(my_hand) \
                    and max_spent <= big_blind * 5:  # 40%
                return 1

        if 0 in obs.legal_actions:
            return 0
        else:
            return 1
