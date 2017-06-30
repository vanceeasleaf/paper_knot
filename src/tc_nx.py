# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-30 15:23:41
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-30 15:27:18
import numpy as np
import aces.tools as tl
from scanf import sscanf
from aces.graph import fig, pl, setLegend
data = []
kappa = []
i = -1
for lx, procs, nodes in [(1, 4, 1), (2, 4, 1), (3, 6, 1),
                         (5, 6, 1), (9, 12, 1), (13, 12, 3)]:
    i += 1
    dir = "sl/nx/" + str(i)
    p = np.loadtxt(dir + '/tempAve.txt', skiprows=1)
    x = np.linspace(0, 1, len(p))
    data.append([x, p[:, 3], 'nx=' + str(lx)])
    dt = p[10:, 3] - p[:-10, 3]
    p = tl.shell_exec('tail -1 %s/result.txt' % dir)
    k, = sscanf(p, 'kappa_src=%f')

    dt = np.sort(np.abs(dt))[-lx:].mean()

    kappa.append([lx, k, dt])
    # dataT=p[30,3]-p[20,3]
    # j=(p[:,4]*p[:,2]).sum()/p[:,2].sum()
    # kapitza.append([dT,np.abs(j)/dataT])
    # kapitza=np.array(kapitza)
i = -1
for lx, procs, nodes in [(17, 12, 1), (24, 12, 2)]:
    i += 1
    dir = "sl/nx2/" + str(i)
    p = np.loadtxt(dir + '/tempAve.txt', skiprows=1)
    x = np.linspace(0, 1, len(p))
    data.append([x, p[:, 3], 'nx=' + str(lx)])
    dt = p[10:, 3] - p[:-10, 3]
    p = tl.shell_exec('tail -1 %s/result.txt' % dir)
    k, = sscanf(p, 'kappa_src=%f')

    dt = np.sort(np.abs(dt))[-lx:].mean()
    kappa.append([lx, k, dt])
data = np.array(data)[::3]


kappa = np.array(kappa)
with fig('tc_nx.eps', figsize=(10, 10)):

    # tc-nx
    axis = pl.subplot(2, 2, 1)
    x = kappa[:, 0]
    y = kappa[:, 1]
    axis.plot(
        x,
        y,
        marker='D',
        ms=12,
        mec='b',
        mfc='w',
        mfcalt="w",
        mew=1.5,
        linewidth=1,
        alpha=.7)
    axis.set_xlabel('nx')
    axis.set_ylabel('Thermal Conductivity (W/m2K)')
    axis.set_xlim([0, 25])
    # pl.xlim([-5,55])
# plot([kapitza[:,0],'dT(K)'],[kapitza[:,1],
#'Kapitza Conductance (W/m2K)'],'kapitza.png')

    # dT-nx
    axis = pl.subplot(2, 2, 2)
    x = kappa[:, 0]
    y = kappa[:, 2]
    axis.plot(
        x,
        y,
        marker='D',
        ms=12,
        mec='b',
        mfc='w',
        mfcalt="w",
        mew=1.5,
        linewidth=1,
        alpha=.7)
    axis.set_xlabel('nx')
    axis.set_ylabel('dT (K)')
    axis.set_xlim([0, 25])

    # dTnx_nx
    axis = pl.subplot(2, 2, 3)
    x = kappa[:, 0]
    y = kappa[:, 2] * x
    axis.plot(
        x,
        y,
        marker='D',
        ms=12,
        mec='b',
        mfc='w',
        mfcalt="w",
        mew=1.5,
        linewidth=1,
        alpha=.7)
    axis.set_xlabel('nx')
    axis.set_ylabel('dT (K)')
    axis.set_xlim([0, 25])
    # profile
    axis = pl.subplot(2, 2, 4)
    for d in data:
        x = d[0]
        y = d[1]
        l = d[2]
        axis.plot(x, y, label=l)
    axis.set_xlabel('x (Reduced)')
    axis.set_ylabel('Temperature (K)')
    setLegend(axis)
