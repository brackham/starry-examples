import matplotlib.pyplot as plt
import numpy as np
import starry
from matplotlib import rcParams

fontsize = 16
linewidth = 2

rcParams['font.size'] = fontsize
rcParams['axes.titlesize'] = fontsize
rcParams['axes.labelsize'] = fontsize
rcParams['xtick.labelsize'] = fontsize
rcParams['ytick.labelsize'] = fontsize
rcParams['legend.fontsize'] = fontsize
rcParams['figure.titlesize'] = fontsize
rcParams['lines.linewidth'] = linewidth
rcParams['axes.linewidth'] = linewidth
rcParams['xtick.major.width'] = linewidth
rcParams['xtick.minor.width'] = linewidth
rcParams['ytick.major.width'] = linewidth
rcParams['ytick.minor.width'] = linewidth
rcParams['xtick.major.size'] = 6
rcParams['ytick.major.size'] = 6

# plt.rc('font', size=fontsize)
# plt.rc('axes', titlesize=fontsize)
# plt.rc('axes', labelsize=fontsize)
# plt.rc('xtick', labelsize=fontsize)
# plt.rc('ytick', labelsize=fontsize)
# plt.rc('legend', fontsize=fontsize)
# plt.rc('figure', titlesize=fontsize)
# plt.rc('axes', linewidth=linewidth)
# plt.rc('xtick', linewidth=linewidth)
# plt.rc('ytick', linewidth=linewidth)
# plt.rc('lines', linewidth=linewidth)

star = starry.Map(lmax=25)
star.axis = [0, 1, 0]
star[1] = 0.4
star[2] = 0.26
spot_pos = [[-30, -30],
            [-30, -0],
            [-30, 30]]
colors = ['#FFC300', '#FF5733', '#C7003B', '#900C3E', '#571845']

xo = np.linspace(-2.5, 2.5, 1000)
yo = 0.3
ro = 0.1

lines = []
flux = star.flux(xo=xo, yo=yo, ro=ro)
lines.append(flux/np.max(flux))
# star.show()

for i, pos in enumerate(spot_pos):
    lat, lon = pos
    star.add_gaussian(sigma=0.15, amp=-1, lat=lat, lon=lon, lmax=23)
    flux = star.flux(xo=xo, yo=yo, ro=ro)
    lines.append(flux/np.max(flux))
    # star.show()

fig, ax = plt.subplots(figsize=(4, 6))
for i, line in enumerate(lines):
    ax.plot(xo, line, lw=2, color=colors[i])

ax.set_xlabel('Time (arbitrary)', fontsize=fontsize)
ax.set_ylabel('Relative Flux', fontsize=fontsize)

fig.savefig('starry_unocculted_spots.pdf', bbox_inches='tight')
