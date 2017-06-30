# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-30 15:31:06
# @Last Modified by:   YangZhou
# @Last Modified time: 2017-06-30 15:49:41
import pandas as pd
from aces.graph import fig, pl, setLegend
df = pd.read_csv("dos/knot/0/region_dos.txt", sep=r"[ \t]", engine="python")
npair = len(df.columns) / 2
datas = []
for i in range(npair):
    rname = df.columns[i * 2][5:]
    datas.append((df['freq_' + rname], df['dos_' + rname], "region:" + rname))
dc = pd.read_csv("dos/knot/0/graphenedos.txt", sep=r"[ \t]", engine="python")
datas.append((dc[dc.columns[0]], dc[dc.columns[1]], 'GNR'))

with fig("dos.eps", figsize=(10, 6)):
    for d in datas:
        pl.plot(d[0], d[1], label=d[2])
    setLegend(pl)
    pl.xlabel("Frequency (THz)")
    pl.ylabel("Phonon Density of States")
    pl.xlim([0, 60])
