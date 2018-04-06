x = [0, 2, 3, 6]
y = [648, 704, 729, 792]
a = 4
d1y = []
d2y = []
d3y = []
for i in range(len(x)-1):
    d1y.append((y[i+1]-y[i])/(x[i+1]-x[i]))
for i in range(len(d1y)-1):
    d2y.append((d1y[i+1]-d1y[i])/(x[i+2]-x[i]))
for i in range(len(d2y)-1):
    d3y.append((d2y[i+1]-d2y[i])/(x[i+3]-x[i]))
f = y[0] + (a-x[0])*d1y[0] + (a-x[0])*(a-x[1])*d2y[0] + (a-x[0])*(a-x[1])*(a-x[2])*d3y[0]
print(d1y)
print(d2y)
print(d3y)
print(f)
