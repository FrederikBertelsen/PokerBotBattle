"""ABIS player"""
from typing import Sequence

from bots.BotInterface import BotInterface
from environment.Constants import Action, Stage
from environment.Observation import Observation
from utils.handValue import getHandPercent


# your bot class, rename to match the file name
class Abots(BotInterface):

    # change the name of your bot here
    def __init__(self, name="Abots"):
        '''init function'''
        super().__init__(name=name)


    def act(self, action_space: Sequence[Action], observation: Observation) -> Action:
        stage = observation.stage

        ratio = self.bestCardsOnHandRatio(observation)

        if stage == Stage.PREFLOP:
            return self.handlePreFlop(observation)

        if ratio < 0.20:
            return Action.FOLD

        if ratio > 0.33:
            return Action.RAISE

        return Action.CALL

    def bestCardsOnHandRatio(self, observation: Observation) -> float:
        handPercent, bestPossibleHand = getHandPercent(observation.myHand, observation.boardCards)

        onHand = 0
        for card in bestPossibleHand:
            if card in observation.myHand:
                onHand += 1

        return onHand / len(bestPossibleHand)


    def handlePreFlop(self, observation: Observation) -> Action:
        # get my hand's percent value (how good is this 2 card hand out of all possible 2 card hands)
        handPercent, _ = getHandPercent(observation.myHand)
        # if my hand is top 20 percent: raise
        if handPercent < .20:
            return Action.RAISE
        # if my hand is top 60 percent: call
        elif handPercent < .60:
            return Action.CALL
        # else fold
        return Action.FOLD


    def handlePostFlop(self, observation: Observation) -> Action:
        # get my hand's percent value (how good is the best 5 card hand i can make out of all possible 5 card hands)
        handPercent, cards = getHandPercent(observation.myHand, observation.boardCards)
        # if my hand is top 30 percent: raise
        if handPercent <= .30:
            return Action.RAISE
        # if my hand is top 80 percent: call
        elif handPercent <= .80:
            return Action.CALL
        # else fold
        return Action.FOLD
