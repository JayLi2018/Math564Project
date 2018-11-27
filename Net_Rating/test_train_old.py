import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics
import numpy as np
# import data
df = pd.read_csv("/home/chenjie/Desktop/Math564Project/Net_Rating/old_net_rating.csv")

df1 = df[['old_net_rating']]
print(df1.shape)

X = df1['old_net_rating']   # setting variables
y = df['win_ratio']

X_train, X_test, y_train, y_test = train_test_split(df1, y, test_size=0.2)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

lm = linear_model.LinearRegression()

model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel("True Win_Ratio")
plt.ylabel("Prediction of Win_Ratio")
print("Score:" + str(model.score(X_test, y_test)))
plt.show()

# cross validation k = 5
scores = cross_val_score(model,df1, y, cv=4)
print("Cross-validated scores for new toe:",scores,"and the average score for 5 fold cv is ",scores.mean,
	"Accuracy : %0.2f(+ - %0.2f)"%(scores.mean(), scores.std() * 2))

