import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

"""
1. Open this web site http://archive.ics.uci.edu/ml/datasets.html
2. Scroll down and open Breast Cancer Wisconsin (Original) Data Set
3. Open Download: Data Folder
4. Save breast-cancer-wisconsin.data file into the directory where you Get_Data.py
5. Open breast-cancer-wisconsin.names and scroll down to bottom
6. You will see # Attributed-NOTE these name are going to be added to the data file.
7. open the above data file in your IDE, and move data down to 2.
8. Now in 1 (header) write (do not include the '')'id,clump_thinkness,unif_cell_size,unif_cell_shape,marg_adhesion,single_epith_cell_size,bare_nuclei,bland_chrom,norm_nucleoli,mitosis,class'
9. Save this back to your directory, I've called mine Get Data.
10. run the code 
"""

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

print(y_test)

