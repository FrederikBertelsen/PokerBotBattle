import botimus
import old_bot
import simple
import over_3
import example_bot
import knockoutbot
import knockoutbot2
import bluff_bot
import bluff_bot2
import randombot
import randombot2
import callBot
import callBot2
import fish_bot
import EMIL
import EMIL_pair
import NewBot
import UnfairAdvantage
import Simply
import Simply2
import SimplyJob
import Dani
import oddsBot
from test import run_benchmark_with_analysis, run_benchmark
import Hercules
import Hermes
import GiveMeAJob
import Hellmuth
import nissemand
import DaniRedux
import mobot

bot_to_test = oddsBot

# bot_to_test = Hellmuth
# other_bot_to_test = Hercules
# bots = [other_bot_to_test, botimus, simple, DaniRedux, bot_to_test, over_3, EMIL, example_bot, EMIL_pair, Simply]

# super board
# bots = [example_bot, simple, Hercules, bot_to_test, UnfairAdvantage, GiveMeAJob, Simply, Hermes]
# high board
bots = [Simply, botimus, simple, example_bot, bot_to_test, over_3, EMIL, old_bot, EMIL_pair, fish_bot]
# mid board
# bots = [bot_to_test, Hermes, old_bot, callBot, over_3, EMIL, nissemand, fish_bot, botimus, bluff_bot]
# low board
# bots = [bot_to_test, randombot, fish_bot, old_bot, knockoutbot2, bluff_bot, callBot, randombot2, knockoutbot, bluff_bot2]



games = 10000  # Change this variable for a different number of test runs
stacksize = 1000  # Change this variable for a different stack size

# run_table(bots, stacksize) # This runs 1 single tournament to the end, and outputs details to the console.

run_benchmark_with_analysis(bots, games, stacksize)
# run_benchmark(bots, rounds, stacksize, True)
