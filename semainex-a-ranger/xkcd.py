#!/usr/bin/env python

# re-ecriture et adaptation libre de http://xkcd.com/519/

import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, 110])

ax.bar([i-0.125 for i in range(3)], [5, 3, 100], 0.25)
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(["900 HOURS\nOF CLASS", 
                    "400 HOURS\nOF HOMEWORK", 
                    "ONE MOOC\nMESSING WITH\nPYTHON"])
plt.yticks([])
ax.set_ylabel("USEFULNESS\nTO CAREER\nSUCCESS",
              rotation='horizontal',
              labelpad=50)

plt.title("11th-GRADE ACTIVITIES:\nafter http://xkcd.com/519/",
          fontsize=25)

fig.subplots_adjust(left=0.2,top=0.8,bottom=0.12)

fig.savefig('xkcd.png')
plt.show()
