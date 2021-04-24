import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics
import random
import plotly.graph_objects as pgo

df = pd.read_csv(r"D:/python/py/pro-111.csv")

Claplist = df["claps"].tolist()

pmean = statistics.mean(Claplist)
psd = statistics.stdev(Claplist)

print(pmean)
print(psd)

def samplespace():
    
    newlist = []

    for i in range(0,30):
        randomindex = random.randint(0,len(Claplist)-1)
        value = Claplist[randomindex]
        newlist.append(value)
        
    smean = statistics.mean(newlist)
    return smean

mainlist = []

for i in range(0,100):
    mainindex = samplespace()
    mainlist.append(mainindex)

smean = statistics.mean(mainlist)
ssd = statistics.stdev(mainlist)

sd_start1, sd_end1 = smean - ssd, smean + ssd
sd_start2, sd_end2 = smean - 2*ssd, smean + 2*ssd
sd_start3, sd_end3 = smean - 3*ssd, smean + 3*ssd

fig = pff.create_distplot([mainlist],["Claps"],show_hist=False)
fig.add_trace(pgo.Scatter(x=[smean,smean],y=[0,0.005],mode="lines",name="mean"))
fig.add_trace(pgo.Scatter(x=[sd_start1,sd_start1],y=[0,0.005],mode="lines",name="sd_start1"))
fig.add_trace(pgo.Scatter(x=[sd_end1,sd_end1],y=[0,0.005],mode="lines",name="sd_end1"))
fig.add_trace(pgo.Scatter(x=[sd_start2,sd_start2],y=[0,0.005],mode="lines",name="sd_start2"))
fig.add_trace(pgo.Scatter(x=[sd_end2,sd_end2],y=[0,0.005],mode="lines",name="sd_end2"))
fig.add_trace(pgo.Scatter(x=[sd_start3,sd_start3],y=[0,0.005],mode="lines",name="sd_start3"))
fig.add_trace(pgo.Scatter(x=[sd_end3,sd_end3],y=[0,0.005],mode="lines",name="sd_end3"))
fig.show()