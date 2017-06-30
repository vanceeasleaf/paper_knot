# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   1970-01-01 08:00:00
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-30 15:43:52

import numpy as np
from aces.graph import fig, pl
x = np.load('strain/seed1/cache.npz')
d = x['d']
c = []
for s, v in d:
    c.append(s)

s = []
for i, u in enumerate(c):
    if not len(u) == len(c[0]):
        print(i)
        continue
    s.append(u)
s = np.array(s)
x = s[0, :, 0]
y = s[:, :, 1].mean(axis=0)
dy = s[:, :, 1].std(axis=0)
y1 = y + dy / 2.0
y2 = y - dy / 2.0
with fig("stress.eps"):
    fi, axes = pl.subplots(1, 2, sharex=True, figsize=(10, 5))
    ax = axes[0]
    for i in range(5):
        v = s[i, :, 1]
        ax.plot(x, v)
    ax.set_xlabel('Strain')
    ax.set_ylabel('Stress (GPa)')
    ax.set_xlim([0, 0.8])
    ax.set_ylim([0, 30])

    ax = axes[1]
    ax.fill_between(x, y1, y2, color="#cccccc")
    ax.plot(x, y, lw=2, color='r')
    ax.set_xlabel('Strain')
    ax.set_ylabel('Stress (GPa)')
    ax.set_xlim([0, 0.8])
    ax.set_ylim([0, 21])
