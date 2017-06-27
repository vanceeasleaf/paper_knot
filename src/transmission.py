# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-27 23:39:13
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-27 23:43:11


import numpy as np
from aces.graph import fig, pl
with fig('transmission.eps'):
    fi, axes = pl.subplots(figsize=(10, 7))
    ax = axes
    file = "negf/knot/0/transmission.txt"
    f = np.loadtxt(file, skiprows=1)
    freq = f[:, 0]
    trans = f[:, 3]
    ax.plot(freq, trans, color="r")
    fi.text(0.5, 0.04, 'Phonon Frequency (THz)', ha='center')
    fi.text(0.07, 0.5, 'Phonon Transmission', va='center', rotation='vertical')
    fi.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0,
        hspace=0)
