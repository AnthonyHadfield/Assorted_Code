
#THIS code find the variance when being dealt a pair that it is AA 1:13 times
#THIS is NOT the variance of being dealt AA in any hand. 
import random; import matplotlib.pyplot as plt; from matplotlib import style
style.use('ggplot')
inumber =[]; theAAlist = []; frequency = []; variance = []; sum = 0; AA_Sum = []
# Let 13 represent being dealt AA. inumber variable is the number of hands dealt to get next AA
# AA_frequency is # of pairs dealt to give next AA # AA_variance is AA_frequency normalized 13 (one in every 13 pairs dealt).# add_data is the sum of the variances
class Pair_variance:
    def deal_AA(self, inumber): # AA is number hands dealt,
        for i in range(1,50001):
            a = random.randint(1, 13)
            if a == 13:
                inumber.append(i)
        return inumber
    def AA_frequency(self, frequency):
        frequency.append(inumber[0])
        for x in range(0, ((len(inumber)-1))):
            frequency.append(inumber[x + 1] - inumber[x])
        return frequency
    def AA_variance(self, variance):
        variance.append(round (((inumber[0]/13)-1), 3)) # adding the first index [0].You should lok up the round function to learn what it does
        for x in range(0, ((len(inumber)-1))):
            num =round((((inumber[x+1]-inumber[x])/13)-1),3)
            variance.append(num)
        return variance
    def add_data(self, AA_sum):
        var = self.AA_variance(variance)
        sum = 0
        AA_Sum = []
        for x in range(0, ((len(inumber)))):
            sum+=var[x]
            AA_Sum.append(sum)
            AA_Sum = [round(x,2) for x in AA_Sum]
        return AA_Sum
    def plot_graph(self):
        y = (Pair_variance.add_data(self, AA_Sum))
        X =(inumber)
        plt.scatter(X, y, s=25, c = "blue")
        plt.title('AA hand variance in Texas Holdem')
        plt.xlabel('# hands')
        plt.ylabel('Variance "pos" good  "neg "bad')
        plt.show()
hands = Pair_variance()
print(hands.deal_AA(inumber))
print(hands.plot_graph())