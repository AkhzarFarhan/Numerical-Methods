x = [100, 150, 200, 250, 300, 350, 400]
y = [10.63, 13.03, 15.04, 16.81, 18.42, 19.9, 21.27]
d1y = []
d2y = []
d3y = []
d4y = []
d5y = []
d6y = []
for i in range(6):
    d1y.append(y[i+1] - y[i])
for i in range(len(d1y)-1):
    d2y.append(d1y[i+1] - d1y[i])
for i in range(len(d2y)-1):
    d3y.append(d2y[i+1] - d2y[i])
for i in range(len(d3y)-1):
    d4y.append(d3y[i+1] - d3y[i])
for i in range(len(d4y)-1):
    d5y.append(d4y[i+1] - d4y[i])
for i in range(len(d5y)-1):
    d6y.append(d5y[i+1] - d5y[i])
p = (218-100)/50
out = y[0] + p*d1y[0] + p*(p-1)*d2y[0]/2 + p*(p-1)*(p-2)*d3y[0]/6 + p*(p-1)*(p-2)*(p-3)*d4y[0]/24 + p*(p-1)*(p-2)*(p-3)*(p-4)*d5y[0]/120 + p*(p-1)*(p-2)*(p-3)*(p-4)*(p-5)*d6y[0]/720
print(d1y, d2y, d3y, d4y, d5y, d6y)
print(out)
