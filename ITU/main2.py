import Hellmuth
import bluff_bot
import bluff_bot2
import callBot
import fish_bot
import knockoutbot
import knockoutbot2
import old_bot
import randombot
import randombot2
import DaniRedux
from runner import play_tournament_table
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
from test import run_benchmark_with_analysis, run_benchmark
import Hercules
import Hermes
import GiveMeAJob
import Hellmuth

bot_to_test = Hellmuth
other_bot_to_test = Hercules

bots = [other_bot_to_test, botimus, DaniRedux, bot_to_test, over_3, EMIL, example_bot, EMIL_pair, Simply]
bot_instances = [b.Bot() for b in bots]

# data = [{'name': b.get_name(), 'wins': 0} for b in bot_instances]
# for i in range(20):
#    res, _ = play_tournament_table(bot_instances, 1000)
#    print(i)
#    data[res[0]['id']]['wins'] += 1

data, details = play_tournament_table(bot_instances, 1000, console_output=True, calc_win_chance=True)
print(len(details))
print(data)
