import numpy as np
from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pii = np.pi
pist_xy = np.array([pii, 5 * pii, 2 * pii, pii, pii, pii, 3 * pii])
nim = np.array([1, 6, 3, 2, 4, 6, 2])
varit = np.array(['black', 'violet', 'red', 'green', 'blue', 'orange', 'purple'])

text = [r'$\pi$', r'$\frac{5\pi}{6}$', r'$\frac{2\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{6}$',
        r'$\frac{3\pi}{2}$']

x = np.cos(pist_xy / nim)
y = np.sin(pist_xy / nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
                 xy=(np.cos(pist_xy[i] / nim[i]), np.sin(pist_xy[i] / nim[i])), xycoords='data',
                 xytext=(+30, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)


plt.figure(figsize=(3*6.4, 4.8))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.plot(X, C, color='hotpink', linewidth=3, linestyle='dashed', label="cos")
plt.plot(X, S, color='darkgrey', linewidth=3, linestyle='dashed', label="sin")
plt.legend(loc='upper left', frameon=False)

plt.show()