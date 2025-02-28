# This program will demonstrate importing own projects and also using pyplot to plot graphs/bin plots

import talisman_exact as te

import matplotlib.pyplot as plt

distr = te.calc_distribution()
# plt.bar([1,2,3],[10,20,30])
plt.bar([i for i in range(3,19)],distr[3:],tick_label=[i for i in range(3,19)])
plt.show()