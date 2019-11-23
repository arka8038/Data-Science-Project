# Performing linear regression for dislikes vs comment_count on standardised dataset

import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold, train_test_split
from sklearn.linear_model import LinearRegression

# Reading data and performing correlation analysis
data_frame = pandas.read_csv("USvideos_standard.csv")
corr_test = data_frame[['likes', 'comment_count', 'views', 'dislikes']]
print(corr_test.corr(method='pearson'))
print(corr_test.corr(method='kendall'))

# Extracting x and y values from dataframe
df = data_frame[['dislikes', 'comment_count']]
X = df.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
Y = df.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

# Splitting testing and training set and predicting outputs
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.9, random_state=0)
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X_train, y_train)  # perform linear regression
y_pred = linear_regressor.predict(X_test)  # make predictions

# Printing evaluation metrics and plotting data
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("Mean y:", data_frame['comment_count'].mean())
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.show()