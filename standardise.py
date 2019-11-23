import numpy as np
import matplotlib.pyplot as plt
import pandas


def standardize(data_frame, label):
    """
    standardizes a series with name label'' within the pd.DataFrame
    data_frame''.
    """
    data_frame = data_frame.copy(deep=True)
    series = data_frame.loc[:, label]
    avg = series.mean()
    stdv = series.std()
    series_standardized = (series - avg)/ stdv
    return series_standardized

data = pandas.read_csv("USvideos_clean.csv")
data_frame = data.copy(deep=True)
data['views'] = standardize(data, 'views')
data['likes'] = standardize(data, 'likes')
data['dislikes'] = standardize(data, 'dislikes')
data['comment_count'] = standardize(data, 'comment_count')

# Displaying the results
print("Initial mean before standardization:", data_frame['likes'].mean())
print("Final mean after standardization:", data['likes'].mean())
print("Initial SD before standardization:", data_frame['likes'].std())
print("Final SD after standardization:", data['likes'].std())
data.to_csv("USvideos_standard.csv")

# Plotting graphs for before and after standardization
# plot_disp = data.plot(x='likes', y='views', kind='box')
        
# data_frame.boxplot(column='comment_count',by='category_id')
data_frame.hist(column='likes')
data.hist(column='likes')
plt.show()