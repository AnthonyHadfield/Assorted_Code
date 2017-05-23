import random
AA= 0; inumber =[]
pairs = ['22', '33', '44', '55', '66', '77', '88', '99', 'TT', 'JJ', 'QQ', 'KK', 'AA']
for i in range(0, 1001):
    a = random.randint(0, 12)
    if a == 12:
        inumber.append(i)
        AA += 1
print('')
print('AA occurs %s times, after %s pairs dealt' % (AA, i))
print('')
print('Pairs frequency check should be 13, and is %0.6s,' % (i/AA))
theAAlist = []
for x in range(0, AA-1):
    theAAlist.append(inumber[x+1]-inumber[x])
print('')
print('theAAlist IS # pairs dealt between each AA occurance:\n')
print(theAAlist)
theAAlist.sort()
print('')
print('The sorted AAList shows the outer variance range')
print('So the AA latency (max number of pairs to next AA) is %s,' % (theAAlist[-1]))
print('And the variance is %.3s %s after %s hands have been dealt,' % ((theAAlist[-1]/13)*100, '%' , i))
