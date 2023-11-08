from runner import play_tournament_table
import random


def run_benchmark(bots, run_count, stacksize=1000, console_output=False):
    bot_instances = [b.Bot() for b in bots]

    data = []
    for i in range(len(bot_instances)):
        b = bot_instances[i]
        data.append({'name': f"{b.get_name()} {i}", 'wins': 0})
    # data = [{'name': b.get_name(), 'wins': 0} for b in bot_instances]

    print("--- 0/" + str(run_count) + " ---")

    for i in range(run_count):
        res, _ = play_tournament_table(bot_instances, stacksize, True, console_output)

        data[res[0]['id']]['wins'] += 1

        if (i + 1) % 500 == 0:
            print("--- " + str(i + 1) + "/" + str(run_count) + " ---")

    [print(d) for d in data]
    return data


def run_benchmark_with_analysis(bots, run_count, stacksize=1000):
    bot_instances = [b.Bot() for b in bots]
    data = [{'N': b.get_name(), 'W': 0, 'S': 0, 'AP': 0.0, "F": 0}
            for b in bot_instances]

    for i in range(len(data)):
        for j in range(len(data)):
            data[i][str(j + 1)] = 0

    print("--- 0/" + str(run_count) + " ---")

    for i in range(run_count):

        # bot_instances = bot_instances[1:] + [bot_instances[0]]
        random.shuffle(bot_instances)

        res, json_data = play_tournament_table(bot_instances, stacksize)#, console_output=True, calc_win_chance=True)

        # calc folds
        for u in range(len(json_data)):
            events = json_data[u]["hand_events"]
            for o in range(len(events)):
                if events[o]["type"] == "action" and events[o]["action"] == 0:
                    for y in range(len(data)):
                        if data[y]["N"] == events[o]["name"]:
                            data[y]["F"] += 1
                            break
        # calc wins
        for j in range(len(res)):
            if res[0]['name'] == data[j]['N']:
                data[j]['W'] += 1
        # calc
        for j in range(len(res)):
            for k in range(len(data)):
                if res[j]['name'] == data[k]['N']:
                    data[k][str(j + 1)] += 1
                    data[k]['S'] += j + 1
                    data[k]['AP'] = data[k]['S'] / (i + 1)
                    break

        # print(chr(27) + "[2J")
        if (i + 1) % 500 == 0:
            print("--- " + str(i + 1) + "/" + str(run_count) + " ---")
        # print("--- " + str(i + 1) + "/" + str(run_count) + " ---")

        # [print(d) for d in data]

    percent = (run_count / 100)

    for i in range(len(data)):
        d = data[i]
        d['T3'] = (d['1'] + d['2'] + d['3']) / percent

    data.sort(key=lambda x: x['T3'], reverse=True)

    print("\nW = Win %\nT3 = Top 3 %\nAP = Average placement\nTF = A score describing the [Fold count] to [Top 3 %] ratio. Basicly how few fold that where used to get into the top 3 (higher is better).\nF = Average folds per game\n- placement % for each possible placement\n")

    for i in range(len(data)):
        d = data[i]
        if d['N'] in ['knockout_bot', 'bluff_bot', 'bluff_bot 2', 'knockout_bot 2', 'callBot']:
            continue

        d['F'] /= run_count
        d['W'] /= percent

        f_percent = d['F'] / 100
        if f_percent > 0:
            d['TF'] = d['T3'] / f_percent
        else:
            d['TF'] = 0.0


        places = ""
        for j in range(len(bot_instances)):
            places = places + f"{round(d[str(1 + j)] / percent, 1)} "

        print(
            f"{d['N']}\nW:{round(d['W'], 3)}  T3:{round(d['T3'], 3)}  AP:{round(d['AP'], 3)}  TF:{round(d['TF'], 3)}  F:{round(d['F'], 3)} - {places}")

    # [print(d) for d in data]

    return data


def run_table(bots, stacksize=1000):
    bot_instances = [b.Bot() for b in bots]

    res, _ = play_tournament_table(bot_instances,
                                   stacksize,
                                   use_timeout=False,
                                   console_output=True)
    print()
    print("bots ordered by final position")
    print([r['name'] for r in res])
    return res
