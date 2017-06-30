import numpy as np
from scanf import sscanf
import aces.tools as tl
from aces.graph import fig, pl, setLegend
kappa = []
i = -1
N = 8
for lx, procs, nodes in [(60, 6, 1), (90, 6, 1), (120, 12, 1), (150, 12, 1)]:
    for j in range(N):
        i += 1
        dir = "sl/lx/" + str(i)
        # if i>19:break
        strain = 0.05 * j / N
        p = tl.shell_exec('tail -1 %s/result.txt' % dir)
        k, = sscanf(p, 'kappa_src=%f')
        kappa.append([lx, strain, k])
i = -1
for lx, procs, nodes in [(180, 12, 1)]:
    for j in range(N):
        continue
        i += 1
        dir = "sl/lx2/" + str(i)
        strain = 0.05 * j / N
        p = tl.shell_exec('tail -1 %s/result.txt' % dir)
        k, = sscanf(p, 'kappa_src=%f')
        kappa.append([lx, strain, k])
kappa = np.array(kappa)

ms = ['D', 'o', 'x', 's', '^', 'p', '.', '+']
with fig('tc_lx.eps', legend=False, figsize=(10, 6)):
    axis = pl.subplot(1, 2, 1)
    strains = np.unique(kappa[:, 1])
    i = -1
    for s in strains:
        i += 1
        filter = kappa[:, 1] == s

        x = kappa[filter, 0]
        y = kappa[filter, 2]
        axis.plot(
            x,
            y,
            marker=ms[i],
            ms=8,
            mec=None,
            mfc='w',
            mfcalt="w",
            mew=1.5,
            linewidth=1,
            alpha=.7,
            label='strain=' + str(s))
    axis.set_xlabel('lx')
    axis.set_ylabel('Thermal Conductivity (W/m2K)')
    # pl.xlim([0,25])
    axis.set_xlim([50, 160])
    axis.set_ylim([0, 20])
    setLegend(axis)

    axis = pl.subplot(1, 2, 2)
    lxs = np.unique(kappa[:, 0])
    i = -1
    for s in lxs:
        i += 1
        filter = kappa[:, 0] == s

        x = kappa[filter, 1]
        y = kappa[filter, 2]
        axis.plot(
            x,
            y,
            marker=ms[i],
            ms=8,
            mec=None,
            mfc='w',
            mfcalt="w",
            mew=1.5,
            linewidth=1,
            alpha=.7,
            label='lx=' + str(s))
    axis.set_xlabel('strain')
    axis.set_ylabel('Thermal Conductivity (W/m2K)')
    axis.set_xlim([-0.002, 0.045])
    axis.set_ylim([0, 20])
    setLegend(axis)
