import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random 

def getSample():
    tempList = []
    for i in range(100):
        x = random.randint(1,len(data)-1)
        tempList.append(data[x])
    return(st.mean(tempList))


df = pd.read_csv('hwData.csv')
data = df['claps'].tolist()
meanList = []
for i in range(0,1000):
    meanList.append(getSample())
mean1 = st.mean(meanList)
mean = st.mean(data)
zscore = (mean1 - mean)/st.stdev(data)
print(zscore)
fig = ff.create_distplot([data],['result'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0,0.0017], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.0017], mode = 'lines', name = 'mean'))
fig.show()