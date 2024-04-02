from scipy.integrate import quad
import numpy as np
from scipy.stats import truncpareto
import matplotlib.pyplot as plt
import math

from srpt import SRPT_slowdown
from fcfs import FCFS_slowdown
from processor_sharing import PS_slowdown

fig, ax = plt.subplots(1, 1)
ax.set_ylim(0, 20)
x_values = np.linspace(1,20,100)

ax.plot(x_values, PS_slowdown, 'g-', lw=2, alpha=0.6, label='PS')
ax.plot(x_values, FCFS_slowdown, 'r-', lw=2, alpha=0.6, label='FCFS')
ax.plot(x_values, SRPT_slowdown, 'b-', lw=2, alpha=0.6, label='SRPT')

plt.show()
