import matplotlib.pyplot as plt
import numpy as np
import starry
from matplotlib import rcParams

fontsize = 16
linewidth = 2
tickmajorsize = 6
ylim = (0.995, 1.0006)

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
rcParams['xtick.major.size'] = tickmajorsize
rcParams['ytick.major.size'] = tickmajorsize

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
spot_pos = [[-0, -30],
            [-10, -0],
            [-0, 30],
            [-10, 45]]
spot_pos = [[0, 30]]
colors = ['#FFC300', '#FF5733', '#C7003B', '#900C3E', '#571845']

xo = np.linspace(-2.5, 2.5, 1000)
t = np.linspace(-2.5, 2.5, 100)
yo = 0.3
ro = 0.05856

# Simulate data
np.random.seed(42)
sigma = 0.00025
noise = np.random.normal(1, sigma, len(t))

lines = []
points = []
flux = star.flux(xo=xo, yo=yo, ro=ro)
model = flux/flux.max()
lines.append(model)
flux = star.flux(xo=t, yo=yo, ro=ro)
model = flux/flux.max()
obs = model*noise
points.append(obs)

# star.show()


for i, pos in enumerate(spot_pos):
    lat, lon = pos
    star.add_gaussian(sigma=0.15, amp=-1, lat=lat, lon=lon, lmax=23)
    flux = star.flux(xo=xo, yo=yo, ro=ro)
    model = flux/flux.max()
    lines.append(model)
    flux = star.flux(xo=t, yo=yo, ro=ro)
    model = flux/flux.max()
    obs = model*noise
    points.append(obs)
star.show()


fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.set_xlabel('Time (arbitrary)', fontsize=fontsize)
ax.set_ylabel('Relative Flux', fontsize=fontsize)
ax.set_ylim(ylim)
obs = points[-1]
ax.plot(xo, lines[0], lw=2, color=colors[1])
ax.plot(xo, lines[-1], lw=2, color=colors[2])
ax.errorbar(t, obs, sigma, ls='', marker='o', ms=3, color='k', zorder=9)
fig.savefig(f'starry_occulted_spots.pdf',
            bbox_inches='tight', transparent=True)
