import math
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

dire = '/dire location'
os.chdir(dire)

%matplotlib inline

df = pd.read_csv('tsla.csv')


df = df[['Open',  'High',  'Low',  'Adj Close', 'Volume']]
df['HL_PCT'] = ((df['High'] - df['Low']) / df['Low']) * 100.0
df['PCT_change'] = ((df['Adj Close'] - df['Open']) / df['Open']) * 100.0
df = df[['Adj Close', 'HL_PCT', 'PCT_change', 'Volume']]
# print(df.head())

    #preprocessing, changing the missing values to -99999, so they 'll be treated as outliers
forecast_col = 'Adj Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-17:]
X = X[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs= -1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)

# =============================================================================
#                   Prediction / Saving LR Model
# =============================================================================
forecast_set = clf.predict(X_lately)
print(forecast_set, confidence, forecast_out)

    #saving classifier with pickle
    
# import pickle
# with open ('linearregression.pickle', 'wb') as f:
#     pickle.dump(clf, f)
 
# clf = pickle.load(open('linearregression.pickle' ,'rb'))

    #Building Linear Regression 
    
from statistics import mean
import numpy as np

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

    #Linear Regression
    
def best_fit_slope(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)**2) - mean(xs**2)))
    b = mean(ys) - m*mean(xs)
    return m, b

def squared_error(ys_orig,ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))

def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)



m,b  = best_fit_slope(xs,ys)
regression_line = [(m*x)+b for x in xs]

r_squared = coefficient_of_determination(ys,regression_line)
    print(r_squared)
    #ploting the line on scatter

# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use('ggplot')
# plt.scatter(xs,ys,color='#003F72')
# plt.plot(xs, regression_line)
# plt.show()

    #sklearn function for coeffictient_of_determination
from sklearn.metrics import r2_score
r2_score(ys, regression_line)

# =============================================================================
#                   dataset creator
# =============================================================================

import random

def create_dataset(hm, variance, step = 2, correlation = True):
    '''hm : how manny datapoints
       variance : the bigger variance the less-tight data will be
       setp : how far to step on average per point
       correlation : bool, no-corr, positive-corr, negative-corr'''
    val = 1
    ys = []
    for i in range(hm):
        v = val + random.randrange(-variance, variance, step = step)
        ys.append(y)

#SVM

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self, visualization=True):
        self.visualization = visualization
        self.colors = {1:'r',-1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
    # train
    def fit(self, data):
        

    def predict(self,features):
        # sign( x.w+b )
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)

        return classification
        
data_dict = {-1:np.array([[1,7],
                          [2,8],
                          [3,8],]),
             
             1:np.array([[5,1],
                         [6,-1],
                         [7,3],])}


### KMEANS CLUSTERING CLASSIFIER


import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale

dire = '/home/kuba/Downloads'
os.chdir(dire)

df = pd.read_excel('titanic.xls')
df.drop(['body','name'], axis = 1, inplace = True)
df.fillna(0, inplace = True)

def handle_non_int_data(df):
    columns = df.columns.values
    
    for column in columns:
        dicto = {}
        def assign_value_to_dict(val):
            return dicto[val]
        
        if df[column].dtype != np.int64 and np.float64:
            list_of_values = df[column].values.tolist()
            unique_values = set(list_of_values)
            x = 0
            for unique in unique_values:
                dicto[unique] = x
                x += 1
                
            df[column] = list(map(assign_value_to_dict, df[column]))
            
    return df

df2 = handle_non_int_data(df)

X = np.array(df2.drop('survived', axis = 1))
X = scale(X)
y = np.array(df2['survived'])

clf = KMeans(n_clusters = 2)
clf.fit(X)



correct = 0

for i in range(len(X)):
    prediction =  np.array(X[i].astype(float))
    prediction = prediction.reshape(-1,len(prediction))
    score = clf.predict(prediction)
    if score[0] == y[i]:
        correct += 1
        
print(correct/len(X))


# =============================================================================
#  37 episode
# =============================================================================

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

X = np.array([[1, 2],
              [1.5, 1.8],
              [5, 8 ],
              [8, 8],
              [1, 0.6],
              [9,11]])

plt.scatter(X[:,0], X[:,1], s=150)
plt.show()


centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.","r.","c.","y."]
class Kmeans:
    
    def __init__(self, k=2, tol = 0.001, max_iter = 300):
        
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        
    def fit(self, data):
        pass
    
        
    def predict(self, data):
        pass
    
#

import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use("ggplot")

centers = [[1,1,1],[5,5,5],[3,10,10]]

X, _ = make_blobs(n_samples = 100, centers = centers, cluster_std = 1.5)
make_blobs()

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters_)

colors = 10*['r','g','b','c','k','y','m']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], X[i][2], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:,0],cluster_centers[:,1],cluster_centers[:,2],
            marker="x",color='k', s=150, linewidths = 5, zorder=10)

plt.show()  
    
# =============================================================================
# 
# =============================================================================
import os
import cv2
import numpy as np
from tqdm import tqdm
class DogsVsCats:
    IMGSIZE = 50
    cat_count = 0
    dog_count = 0
    CATS = 'PetImages/Cat'
    DOGS = 'PetImages/Dog'
    training_dataset = []
    labels = {CATS : 0, DOGS : 1}
    exc = []
    
    def train_data(self):
        for label in self.label:
            for file in tqdm(os.listdir(label)):
                if 'jpg' in file:
                    try:
                        path = os.path.join(label, file)
                        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                        img = cv2.resize(img, (self.IMGSIZE * self.IMGSIZE))
                        self.training_dataset.append(np.array(img), np.eye(2)[self.labels][label])
                        if label == self.CATS:
                            self.cat_count += 1
                        elif label == self.DOGS:
                            self.dog_count += 1
                            
                    except Exception as e:
                        self.exc += 1
                        pass
    np.random.shuffle(self.training_dataset)
    np.save("training_dataset.npy", self.training_dataset)
    print('Cats', self.cat_count)
    print('Dogs', self.dog_count)
    
                        
if REBUILD_DATA:
    dogvcats = DogsVsCats()
    dogvcats.train_data()                   
                        




