# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   1970-01-01 08:00:00
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-30 15:44:36
from aces.graph import fig, pl
import numpy as np

with fig('cycle.eps'):
    fi, axes = pl.subplots(1, 2, sharex=True, figsize=(10, 5))
    y = np.loadtxt("strain/circle/right/9/cal_stress.txt", skiprows=1)
    axes[0].plot(y[:, 0], y[:, 1], color="k", lw=2)
    axes[0].set_xlabel("Strain")
    axes[0].set_ylabel("Stress(GPa)")

    y = np.loadtxt("strain/circle/graphene/0/cal_stress.txt", skiprows=1)
    axes[1].plot(y[:, 0], y[:, 1], color="k", lw=2)
    axes[1].set_xlabel("Strain")
    axes[1].set_ylabel("Stress(GPa)")
