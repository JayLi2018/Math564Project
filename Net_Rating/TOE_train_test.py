import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn import metrics
import numpy as np
# import data
df = pd.read_csv("/home/chenjie/Desktop/Math564Project/WinRatio_TOE/toe_results.csv")

df1 = df[['toe']] # old toe
df2 = df[['new_toe']]

X1 = df1['toe']   # setting variables
X2 = df2['new_toe']
y = df['win_ratio']

X1_train, X1_test, y_train, y_test = train_test_split(df1, y, test_size=0.2)
X2_train, X2_test, y_train, y_test = train_test_split(df2, y, test_size=0.2)

lm1 = linear_model.LinearRegression()
lm2 = linear_model.LinearRegression()

model1 = lm1.fit(X1_train, y_train)
predictions1 = lm1.predict(X1_test)
plt.scatter(y_test, predictions1)
plt.xlabel("True Win_Ratio")
plt.ylabel("Prediction of Win_Ratio using old toe")
print("Score: old toe is" + str(model1.score(X1_test, y_test)))
plt.show()

model2 = lm2.fit(X2_train, y_train)
predictions2 = lm2.predict(X2_test)
plt.scatter(y_test, predictions2)
plt.xlabel("True Win_Ratio")
plt.ylabel("Prediction of Win_Ratio using new toe")
print("Score: new toe is" + str(model2.score(X2_test, y_test)))
plt.show()


# cross validation k = 5
scores1= cross_val_score(model1,df1, y, cv=5)
print("Cross-validated scores for old toe:",scores1,"and the average score for 5 fold cv is ",scores1.mean,
	"Accuracy : %0.2f(+ - %0.2f)"%(scores1.mean(), scores1.std() * 2))


scores2 = cross_val_score(model2,df2, y, cv=5)
print("Cross-validated scores for new toe:",scores2,"and the average score for 5 fold cv is ",scores2.mean,
	"Accuracy : %0.2f(+ - %0.2f)"%(scores2.mean(), scores2.std() * 2))