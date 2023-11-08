"""You have been terminated!"""
from typing import Sequence

from bots.BotInterface import BotInterface
from environment.Constants import Action, HandType, Stage
from environment.Observation import Observation
from utils.handValue import getBoardHandType, getHandPercent, getHandType

# your bot class, rename to match the file name
class T800(BotInterface):

    # change the name of your bot here
    def __init__(self, name="T-800"):
        '''init function'''
        super().__init__(name=name)

    def act(self, action_space: Sequence[Action], observation: Observation) -> Action:
        # use different strategy depending on pre or post flop (before or after community cards are delt)
        stage = observation.stage
        opponent_actions_this_round = observation.get_opponent_history_current_stage()
        # Get the last action the opponent have done
        
        last_action = opponent_actions_this_round[-1] if len(
            opponent_actions_this_round) > 0 else None
        if stage == Stage.PREFLOP:
            return self.handlePreFlop(observation)

        return self.handlePostFlop(observation)

    def handlePreFlop(self, observation: Observation) -> Action:
        # get my hand's percent value (how good is this 2 card hand out of all possible 2 card hands)
        handPercent, _ = getHandPercent(observation.myHand)
        handType = getHandType(observation.myHand)
        if handType == HandType.PAIR:
            return Action.RAISE
        # if my hand is top 20 percent: raise
        if handPercent < .20:
            return Action.RAISE
        # if my hand is top 60 percent: call
        elif handPercent < .70:
            return Action.CALL
        # else fold
        return Action.FOLD

    def handlePostFlop(self, observation: Observation) -> Action:
        # get my hand's percent value (how good is the best 5 card hand i can make out of all possible 5 card hands)
        handPercent, cards = getHandPercent(
            observation.myHand, observation.boardCards)
        # if my hand is top 30 percent: raise
        if handPercent <= .25:
            return Action.RAISE
        # if my hand is top 80 percent: call
        elif handPercent <= .80:
            return Action.CALL
        # else fold
        return Action.FOLD