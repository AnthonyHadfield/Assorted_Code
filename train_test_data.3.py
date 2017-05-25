"""
1. THE print(trd);print(trl);print(ted);print(tel)
2. CAN be removed, its just so you can see data individually
"""
import numpy as np
from sklearn import preprocessing, cross_validation
trd = []  # training_date
trl = []  # training_labels
ted = []  # test_data
tel = []  # test_labels
class data_set:
    def data(self, trd, trl):
        for i in range(0, 20):
            a = np.random.randint(0, 50)
            b = np.random.randint(0, 50)
            trd.append([a, b])
            trl.append(1)
        return trd, trl
    def split_data(self, trd, trl, ted, tel):
        data_set.data(self, trd, trl)
        trd, ted, trl, tel = cross_validation.train_test_split(trd, trl, test_size=0.2)
        tel = [2 if x == 1 else x for x in tel]
        print(trd);print(trl);print(ted);print(tel)
        return trd, trl, ted, tel
data = data_set()
print(data.split_data(trd, trl, ted, tel))
print('')
#ALTERNATIVELY YOU CAN JUST DO
import numpy as np
from sklearn import preprocessing, cross_validation
trd = []  # training_date
trl = []  # training_labels
ted = []  # test_data
tel = []  # test_labels
for i in range(0, 20):
    a = np.random.randint(0, 50)
    b = np.random.randint(0, 50)
    trd.append([a, b])
    trl.append(1)
trd, ted, trl, tel = cross_validation.train_test_split(trd, trl, test_size=0.2)
tel = [2 if x == 1 else x for x in tel]
print(trd);print(trl);print(ted);print(tel)
