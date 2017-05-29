import random
import matplotlib.pyplot as plt
from matplotlib import  style
style.use('ggplot')
AA= 0; inumber =[]
pairs = ['22', '33', '44', '55', '66', '77', '88', '99', 'TT', 'JJ', 'QQ', 'KK', 'AA']
AA = 0
for i in range(0, 100001):
    a = random.randint(0, 12)
    if a == 12:
        inumber.append(i)
        AA += 1
theAAlist = []
theAAlist.append(inumber[0])
for x in range(0, AA-1):
    theAAlist.append(inumber[x+1]-inumber[x])
AA_frequency = []
AA_frequency.append((inumber[0]/13)-1)
AA_Sum = []
AA_Sum.append((inumber[0]/13)-1)
print(AA_Sum)
for x in range(0, AA-1):
    num =round((((inumber[x+1]-inumber[x])/13)-1),3)
    AA_frequency.append(num)
sum = AA_Sum[0]
for x in range(0, AA-1):
    num =round((((inumber[x+1]-inumber[x])/13)-1),3)
    sum+=(num)
    AA_Sum.append(sum)
AA_Sum = [round(x,2) for x in AA_Sum]
y = [AA_Sum]
X =[inumber]
plt.scatter(X, y, s=50, c = "blue")
plt.title('AA hand variance in Texas Holdem')
plt.xlabel('# hands')
plt.ylabel('Variance "pos" good  "neg "bad')
plt.show()
