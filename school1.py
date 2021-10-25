import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

#population data
mean = statistics.mean(data)
stdev = statistics.stdev(data)

def randomsetofmean(count):
    dataset = []
    for i in range(0, count):
        randomindex = random.randint(0, len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0, 1000):
    setofmeans = randomsetofmean(100)
    meanlist.append(setofmeans)

#sampling data
samplemean = statistics.mean(meanlist)
samplestdev = statistics.stdev(meanlist)

#standard deviation start and end
firststdevstart, firststdevend = samplemean-samplestdev, samplemean+samplestdev
twostdevstart, twostdevend = samplemean-(2*samplestdev), samplemean+(2*samplestdev)
threestdevstart, threestdevend = samplemean-(3*samplestdev), samplemean+(3*samplestdev)

print("STD 1", firststdevstart, firststdevend)
print("STD 2", twostdevstart, twostdevend)
print("STD 3", threestdevstart, threestdevend)

#fig = ff.create_distplot([meanlist], ["Math Score"], show_hist = False)
#fig.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.20], mode = "lines", name = "mean"))

#fig.add_trace(go.Scatter(x = [firststdevstart, firststdevstart], y = [0, 0.17], mode = "lines", name = "stdev1start"))
#fig.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "stdev1end"))

#fig.add_trace(go.Scatter(x = [twostdevstart, twostdevstart], y = [0, 0.17], mode = "lines", name = "stdev2start"))
#fig.add_trace(go.Scatter(x = [twostdevend, twostdevend], y = [0, 0.17], mode = "lines", name = "stdev2end"))

#fig.add_trace(go.Scatter(x = [threestdevstart, threestdevstart], y = [0, 0.17], mode = "lines", name = "stdev3start"))
#fig.add_trace(go.Scatter(x = [threestdevend, threestdevend], y = [0, 0.17], mode = "lines", name = "stdev3end"))

#fig.show()

print("Population mean is: " + str(mean))
print("Standard deviation of the population is: " + str(stdev))

print("Sampling mean is: " + str(samplemean))
print("Standard deviation of the the sample is: " + str(samplestdev))

df1 = pd.read_csv("group3.csv")
data1 = df1["Math_score"].tolist()

meanofsample1 = statistics.mean(data1)
print("Mean of sample 1: " + str(meanofsample1))

fig1 = ff.create_distplot([meanlist], ["Math score group 1"], show_hist = False)
fig1.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode = "lines", name = "mean"))
fig1.add_trace(go.Scatter(x = [meanofsample1, meanofsample1], y = [0, 0.17], mode = "lines", name = "meanofsample1"))
fig1.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "stdev1end"))
fig1.add_trace(go.Scatter(x = [twostdevend, twostdevend], y = [0, 0.17], mode = "lines", name = "stdev2end"))
fig1.add_trace(go.Scatter(x = [threestdevend, threestdevend], y = [0, 0.17], mode = "lines", name = "stdev3end"))
fig1.show()

#finding the mean of the students who used app

df1 = pd.read_csv("school1.csv")
data1 = df1["Math_score"].tolist()

meanofsample1 = statistics.mean(data1)
print("Mean of sample 1: " + str(meanofsample1))

fig1 = ff.create_distplot([meanlist], ["Math score group 1"], show_hist = False)
fig1.add_trace(go.Scatter(x = [samplemean, samplemean], y = [0, 0.17], mode = "lines", name = "mean"))
fig1.add_trace(go.Scatter(x = [meanofsample1, meanofsample1], y = [0, 0.17], mode = "lines", name = "meanofsample1"))
fig1.add_trace(go.Scatter(x = [firststdevend, firststdevend], y = [0, 0.17], mode = "lines", name = "stdev1end"))
fig1.add_trace(go.Scatter(x = [twostdevend, twostdevend], y = [0, 0.17], mode = "lines", name = "stdev2end"))
fig1.add_trace(go.Scatter(x = [threestdevend, threestdevend], y = [0, 0.17], mode = "lines", name = "stdev3end"))
fig1.show()

zscore = (meanofsample1-samplemean)/samplestdev
print("Z score is: " + str(zscore))