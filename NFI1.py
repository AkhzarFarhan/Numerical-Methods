from sympy import symbols, init_printing
p = symbols('n')
init_printing(use_unicode=True)
x = [1, 2, 3, 4, 5]
y = [1, 9, 36, 100, 225]
d1y = []
d2y = []
d3y = []
d4y = []
for i in range(4):
    d1y.append(y[i+1] - y[i])
for i in range(len(d1y)-1):
    d2y.append(d1y[i+1] - d1y[i])
for i in range(len(d2y)-1):
    d3y.append(d2y[i+1] - d2y[i])
for i in range(len(d3y)-1):
    d4y.append(d3y[i+1] - d3y[i])

out10 = y[0] + p*d1y[0] + p*(p-1)*d2y[0]/2 + p*(p-1)*(p-2)*d3y[0]/6 + p*(p-1)*(p-2)*(p-3)*d4y[0]/24
print(d1y, d2y, d3y, d4y)
print(out10)
