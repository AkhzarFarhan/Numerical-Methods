x = [3, 4, 5, 6, 7, 8, 9]
y = [4.8, 8.4, 14.5, 23.6, 36.2, 52.8, 73.9]
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
p1 = -2
p2 = 7
out2 = y[0] + p2*d1y[0] + p2*(p2-1)*d2y[0]/2 + p2*(p2-1)*(p2-2)*d3y[0]/6 + p2*(p2-1)*(p2-2)*(p2-3)*d4y[0]/24 + p2*(p2-1)*(p2-2)*(p2-3)*(p2-4)*d5y[0]/120 + p2*(p2-1)*(p2-2)*(p2-3)*(p2-4)*(p2-5)*d6y[0]/720
out1 = y[0] + p1*d1y[0] + p1*(p1-1)*d2y[0]/2 + p1*(p1-1)*(p1-2)*d3y[0]/6 + p1*(p1-1)*(p1-2)*(p1-3)*d4y[0]/24 + p1*(p1-1)*(p1-2)*(p1-3)*(p1-4)*d5y[0]/120 + p1*(p1-1)*(p1-2)*(p1-3)*(p1-4)*(p1-5)*d6y[0]/720
print(d1y, d2y, d3y, d4y, d5y, d6y)
print("1st term: ", out1, "\n10th term: ", out2)
