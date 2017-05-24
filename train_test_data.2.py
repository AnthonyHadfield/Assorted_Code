import numpy as np
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
        trd = trd[:-5]; ted = trd[-5:]
        trl = trl[:-5]; tel = trl[-5:]
        tel = [2 if x == 1 else x for x in tel]
        print(trd);print(trl);print(ted);print(tel)
        return trd, trl, ted, tel
data = data_set()
print(data.split_data(trd, trl, ted, tel))