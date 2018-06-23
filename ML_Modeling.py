import Data_Reading as DR
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model


#making datasets of dependent and independent variable
X1 = DR.data.ix[:,:4]
#print(X1)

X2 = DR.data.ix[:,6:7]
#print(X2)

frame = [X1, X2]

X = pd.concat(frame,axis=1)
#print(X)

Y = DR.data.ix[:,9:10]
#print(Y)


#splitting data points into train and test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3,random_state=101)

reg = linear_model.LogisticRegression()

reg.fit(X_train,Y_train)

predicted_Y = reg.predict(X_test)