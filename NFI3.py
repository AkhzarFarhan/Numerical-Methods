x = [-0.75, -0.5, -0.25, 0]
y = [-0.0718125, -0.02475, 0.3349375, 1.10100]
d1y = []
d2y = []
d3y = []
for i in range(3):
    d1y.append(y[i+1] - y[i])
for i in range(len(d1y)-1):
    d2y.append(d1y[i+1] - d1y[i])
for i in range(len(d2y)-1):
    d3y.append(d2y[i+1] - d2y[i])
p = 1.6666666666
out = y[0] + p*d1y[0] + p*(p-1)*d2y[0]/2 + p*(p-1)*(p-2)*d3y[0]/6
print(d1y, d2y, d3y)
print(out)
