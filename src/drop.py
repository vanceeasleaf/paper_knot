
import numpy as np
from aces.graph import fig, pl
import aces.tools as tl
import matplotlib
matplotlib.rcParams['patch.linewidth'] = 1


def getBreakStrains(s):
    n = 5
    sk = np.zeros_like(s[:, 1])
    for j, u in enumerate(s[n:-n]):
        sk[j + n] = s[j:j + n, 1].mean()
    v = []
    n = 30
    for j, u in enumerate(sk[n:-n]):
        var = abs(sk[j + n] - sk[j + n - 1])
        if var > 1.0 and var > sk[j:j + n].std():
            if len(v) > 0 and j - v[-1] < n:
                continue
            v.append(j + n)
    return np.array(v)


if not tl.exists('strain/seed1/cache.npz'):
    c = []
    d = []
    i = 0
    for seed in range(200, 400):
        dir = "strain/seed1/" + str(i)
        s = np.loadtxt(dir + "/cal_stress.txt", skiprows=1)
        v = getBreakStrains(s)
        i += 1
        print(dir, s[v, 0])
        c.append(s[v, 0])
        d.append([s, v])
    i = 0
    for seed in range(400, 600):
        dir = "strain/seed2/" + str(i)
        s = np.loadtxt(dir + "/cal_stress.txt", skiprows=1)
        v = getBreakStrains(s)
        i += 1
        print(dir, s[v, 0])
        c.append(s[v, 0])
        d.append([s, v])
    np.savez('strain/seed1/cache.npz', c=c, d=d)
x = np.load('strain/seed1/cache.npz')
c, d = x['c'], x['d']
s0 = []
s1 = []
s2 = []
s3 = []
i = -1
for s in c:
    i += 1
    # if not len(s)==len(c[0]):print i;continue
    if len(s) > 0:
        s0.append(s[0])
    if len(s) > 1:
        s1.append(s[1])
    if len(s) > 2:
        s2.append(s[2])
    if len(s) > 3:
        s3.append(s[3])
datas = []
u0, p0 = np.histogram(s0, bins=20, range=(0, 1), density=True)
x = np.zeros(len(u0) + 1)
x[1:] = u0
u0 = x
datas.append([p0, u0, '1st drop strain'])
u0, p0 = np.histogram(s1, bins=20, range=(0, 1), density=True)
x = np.zeros(len(u0) + 1)
x[1:] = u0
u0 = x
datas.append([p0, u0, '2nd drop strain'])
u0, p0 = np.histogram(s2, bins=20, range=(0, 1), density=True)
x = np.zeros(len(u0) + 1)
x[1:] = u0
u0 = x
datas.append([p0, u0, '3rd drop strain'])
u0, p0 = np.histogram(s3, bins=20, range=(0, 1), density=True)
x = np.zeros(len(u0) + 1)
x[1:] = u0
u0 = x
datas.append([p0, u0, '4th drop strain'])


# x=c[:,0,:].mean(axis=0)
# y=c[:,1,:].mean(axis=0)
#plot([x,'Strain'],[y,'Stress (GPa)'],filename='ave_stress.png')
s = d[0][0]
start = 0
for i, u in enumerate(s[:, 0]):
    if u > .03:
        start = i
        break
segs = []
j = -1
for s, v in d:
    j += 1
    for i, u in enumerate(v):
        if i > 0:
            c = v[i - 1]
        else:
            c = start
        filter = np.arange(c + 20, u - 20)
        p, residuals, rank, singular_values, rcond = np.polyfit(
            s[filter, 0], s[filter, 1], 1, full=True)
        if p[0] < 0:
            continue
        cc = [
            j, i, p[0], s[c + 20, 0], s[u - 20, 0],
            len(filter),
            np.sqrt(residuals[0] / len(filter))
        ]
        # print cc
        segs.append(cc)
pp = []
for u in segs:
    pp.append(u[2])

u0, p0 = np.histogram(pp, bins=50, density=True)
# plot([p0[1:],'Young\'s Modulous (GPa/m)'],
# [u0,'Probability Density'],filename='young_distribution.png')

pp = []
for s, v in d:
    pp.append(len(v))

# u0,p0=np.histogram(pp, bins=40,density=True)
# plot([p0[1:],'Drop Times'],
# [u0,'Probability Density'],filename='drop_times_dist.png')

n = len(d)
m = len(d[0][0])
ss = np.zeros([n, m])
i = -1
for s, v in d:
    i += 1
    m = len(s)
    ss[i, :m] = s[:, 1]
ss = np.abs(ss) < .5
kk = ss.sum(axis=0)
s = d[0][0]
x = s[:, 0]
y = kk.astype(np.float) / len(d)
from aces.graph import setLegend
with fig('drop.eps', legend=False, ncol=1, figsize=(14, 10)):
    oldpl = pl
    pl = oldpl.subplot(2, 2, 1)
    c = ['g', 'r', 'b', 'orange']
    dx = 0.05
    for i, serie in enumerate(datas):
        pl.fill_between(
            serie[0],
            0,
            serie[1],
            label=serie[2],
            linewidth=0,
            facecolor=c[i],
            alpha=.5)
        pl.plot(serie[0], serie[1],
                label=serie[2], color=c[i], linewidth=2)
    pl.set_xlabel('Strain')
    pl.set_ylabel('Probability Density')
    pl.set_xlim([0, 1.0])
    setLegend(pl)
    pl = oldpl.subplot(2, 2, 2)
    # with fig('young_distribution.png'):
    dx = p0[1] - p0[0]
    pl.bar(p0[1:], u0, alpha=.5, width=dx)
    pl.set_xlabel('Young\'s Modulous (GPa/m)')
    pl.set_ylabel('Probability Density')
    pl.set_xlim([0, 400])
    pl = oldpl.subplot(2, 2, 3)
    # with fig('drop_times_dist.png'):
    pl.hist(pp, bins=20, range=(.5, 9.5), facecolor='gray')
    pl.set_xlabel('Drop Times')
    pl.set_ylabel('Probability Density')
    # with fig('break_strain_dist.png'):
    pl = oldpl.subplot(2, 2, 4)
    pl.plot(x, y, lw=2)
    pl.set_xlabel('Break Strain')
    pl.set_ylabel('Probability Density')
