# Simulation of the martingale strategy with initial money m and probability of winning w

import random

money = 1000
starting_bet = 1
win_prob = 0.33
repetitions = 100

def reward(win_prob : float, bet : float):
    if random.random() < win_prob:
        return bet
    else:
        return -bet

money_history = [money]
bet_history = [starting_bet]
reward_history = [0]
current_bet = starting_bet
for i in range(repetitions):
    outcome = reward(win_prob,current_bet)
    money += outcome
    if outcome < 0:
        current_bet = current_bet * 2
    else:
        current_bet = 1
    money_history.append(money)
    bet_history.append(current_bet)
    reward_history.append(outcome)
    if money < 0:
        break

# when using fstring -> {"something":20} prints something inside a box for which 20 spaces are reserved
print(f"|{"round":^10}|{"money":^10}|{"bet":^10}|{"reward":^10}|")
print(f"|{"":-^10}|{"":-^10}|{"":-^10}|{"":-^10}|")
for i in range(len(money_history)):
    print(f"|{i:^10}|{money_history[i]:^10}|{bet_history[i]:^10}|{reward_history[i]:^10}|")

# Why is martingale a good strategy?

# Every time we loose money, say x dollars, then the next bet will be 2x dollars
# so if we win the next bet we will be in positive numbers by x

# Lets assume we will be losing n times, then we lost:
# 1 + 2 + 4 + ... + 2^(n-1)
# but on the next step, if we win, we will get 2^n money which covers all the previous losses

# Is it always a good strategy? 
# What are drawbacks of this strategy?
    