"""Random player"""
import random

from state import *
from utils import *


# your bot class, rename to match the file name
class Bot:

    # change the name of your bot here
    def get_name(self):
        return "good_bot"

    def act(self, obs: Observation):
        # use different strategy depending on pre or post flop (before or after community cards are delt)
        stage = obs.current_round

        if stage == 0:
            return self.handlePreFlop(obs)

        if stage == 1:
            return self.handleFlop(obs)

        if stage == 2:
            return self.handleTurn(obs)

        return self.handleRiver(obs)

    def getHandPercent(self, my_hand: Tuple[str]):
        if Range("99+, AJs+, KQs, AKo").is_hand_in_range(my_hand):  # 5%
            return 5
        if Range("77+, A9s+, KTs+, QJs, AJo+, KQo").is_hand_in_range(my_hand):  # 10%
            return 10
        if Range("66+, A5s+, K9s+, Q9s+, JTs, ATo+, KJo+").is_hand_in_range(my_hand):  # 15%
            return 15
        if Range("55+, A3s+, K7s+, Q8s+, J9s+, T9s, A9o+, KTo+, QJo").is_hand_in_range(my_hand):  # 20%
            return 20
        if Range("55+, A2s+, K5s+, Q8s+, J8s+, T9s, A8o+, K9o+, QTo+, JTo").is_hand_in_range(my_hand):  # 25%
            return 25
        if Range("44+, A2s+, K2s+, Q6s+, J7s+, T7s+, 98s, A7o+, K9o+, Q9o+, JTo").is_hand_in_range(my_hand):  # 30%
            return 30
        if Range("33+, A2s+, K2s+, Q4s+, J7s+, T7s+, 97s+, 87s, A5o+, K8o+, Q9o+, J9o+").is_hand_in_range(my_hand):  # 35%
            return 35
        if Range("33+, A2s+, K2s+, Q4s+, J6s+, T7s+, 97s+, 87s, A3o+, K7o+, Q8o+, J9o+, T9o").is_hand_in_range(my_hand):  # 40%
            return 40
        if Range("22+, A2s+, K2s+, Q2s+, J4s+, T6s+, 96s+, 86s+, 76s, A2o+, K7o+, Q8o+, J8o+, T9o").is_hand_in_range(my_hand):  # 45%
            return 45
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T5s+, 96s+, 86s+, 75s+, A2o+, K5o+, Q7o+, J8o+, T8o+").is_hand_in_range(my_hand):  # 50%
            return 50
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 95s+, 85s+, 75s+, 65s, A2o+, K4o+, Q6o+, J7o+, T8o+, 98o").is_hand_in_range(my_hand):  # 55%
            return 55
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 94s+, 84s+, 74s+, 64s+, 54s, A2o+, K3o+, Q5o+, J7o+, T7o+, 97o+").is_hand_in_range(my_hand):  # 60%
            return 60
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 84s+, 73s+, 64s+, 53s+, A2o+, K2o+, Q4o+, J6o+, T7o+, 97o+, 87o").is_hand_in_range(my_hand):  # 65%
            return 65
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 73s+, 63s+, 53s+, 43s, A2o+, K2o+, Q3o+, J5o+, T6o+, 97o+, 86o+").is_hand_in_range(my_hand):  # 70%
            return 70
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, A2o+, K2o+, Q2o+, J4o+, T6o+, 96o+, 86o+, 76o").is_hand_in_range(my_hand):  # 75%
            return 75
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J3o+, T5o+, 95o+, 86o+, 75o+, 65o").is_hand_in_range(my_hand):  # 80%
            return 80
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T3o+, 95o+, 85o+, 75o+, 64o+, 54o").is_hand_in_range(my_hand):  # 85%
            return 85
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T2o+, 93o+, 84o+, 74o+, 64o+, 54o").is_hand_in_range(my_hand):  # 90%
            return 90
        if Range("22+, A2s+, K2s+, Q2s+, J2s+, T2s+, 92s+, 82s+, 72s+, 62s+, 52s+, 42s+, 32s, A2o+, K2o+, Q2o+, J2o+, T2o+, 92o+, 83o+, 73o+, 63o+, 53o+, 43o").is_hand_in_range(my_hand):  # 95%
            return 95
        return 100

    def handlePreFlop(self, obs: Observation):

        # get my hand's percent value (how good is this 2 card hand out of all possible 2 card hands)
        handPercent = self.getHandPercent(obs.my_hand)

        # if my hand is top 20 percent: raise
        if handPercent <= 35:
            return obs.get_min_raise()

        # 1 = small blind
        if len(obs.get_actions_this_round()) == 0 and handPercent <= 55:
            return obs.small_blind

        elif handPercent <= 50:
            return obs.small_blind

        # else check
        return 1

    def handleFlop(self, obs: Observation):
        # get my hand's percent value (how good is this 2 card hand out of all possible 2 card hands)
        myTwoCardHandPercent = self.getHandPercent(obs.my_hand)
        communityHandPercent = self.getHandPercent(sum((obs.my_hand, obs.board_cards), ()))

        handTypeValue = obs.get_my_hand_type()
        handTypeValueBoard = obs.get_board_hand_type()

        # if my hand is top 20 percent: raise
        if myTwoCardHandPercent <= 15:
            return obs.get_min_raise()

        if communityHandPercent <= 25 and myTwoCardHandPercent <= 80:
            return obs.get_min_raise()

        if handTypeValue.value < handTypeValueBoard.value - 1:
            return obs.get_min_raise()

        if handTypeValueBoard == HandType.THREEOFAKIND and myTwoCardHandPercent <= 30:
            return obs.get_min_raise()

        if handTypeValue < HandType.FULLHOUSE:
            return obs.get_min_raise()

        # if my hand is top 60 percent: call
        elif myTwoCardHandPercent <= 45:
            return 1

        # else fold
        return 0

    def handleTurn(self, obs: Observation):
        myTwoCardHandPercent = self.getHandPercent(obs.my_hand)
        communityHandPercent = self.getHandPercent(sum((obs.my_hand, obs.board_cards), ()))

        handTypeValue = obs.get_my_hand_type()
        handTypeValueBoard = obs.get_board_hand_type()

        if communityHandPercent <= 20 and myTwoCardHandPercent <= 80:
            return obs.get_min_raise()

        if handTypeValue.value < handTypeValueBoard.value - 1:
            return obs.get_min_raise()

        if handTypeValue < HandType.FLUSH:
            return obs.get_min_raise()

        if handTypeValue.value < handTypeValueBoard.value and myTwoCardHandPercent <= 90:
            return 0

        if communityHandPercent >= 65 and handTypeValue > HandType.FULLHOUSE:
            return 1

        return 0

    def handleRiver(self, obs: Observation):
        communityHandPercent = self.getHandPercent(sum((obs.my_hand, obs.board_cards), ()))

        handTypeValue = obs.get_my_hand_type()
        handTypeValueBoard = obs.get_board_hand_type()

        if communityHandPercent <= 25:
            return obs.get_min_raise()

        if handTypeValue.value < handTypeValueBoard.value - 1:
            return obs.get_min_raise()

        if handTypeValue < 6:
            return obs.get_min_raise()

        if handTypeValue.value < handTypeValueBoard.value:
            return 0

        if communityHandPercent > 0.65 and handTypeValue > 7:
            return 1

        return 0


