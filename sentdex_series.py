import math
import numpy as np
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

dire = '/home/kuba/Windows_Old_Staff/files'
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

import seaborn as sns
sns.lineplot(data = forecase_set_df, x = forecase_set_df.index, y = 'forecast')
sns.jointplot(data = [df, forecase_set_df], )

#saving classifier with pickle
import pickle
with open ('linearregression.pickle', 'wb') as f:
    pickle.dump(clf, f)
#reading classifier with pickle
clf = pickle.load(open('linearregression.pickle' ,'rb'))



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

m,b  = best_fit_slope(xs,ys)

regression_line = [(m*x)+b for x in xs]

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')



plt.scatter(xs,ys,color='#003F72')
plt.plot(xs, regression_line)
plt.show()
