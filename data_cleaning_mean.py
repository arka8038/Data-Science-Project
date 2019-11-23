import pandas
import numpy as np
import cv2

data = pandas.read_csv("USvideos_original.csv", dtype=str)
data['views'] = pandas.to_numeric(data['views'], errors='coerce')
data['likes'] = pandas.to_numeric(data['likes'], errors='coerce')
data['comment_count'] = pandas.to_numeric(data['comment_count'], errors='coerce')
data['dislikes'] = pandas.to_numeric(data['dislikes'], errors='coerce')

# Checking if NaNs are present in the dataset
bool_series = pandas.isnull(data['likes'])
print(data[bool_series][0:5])

# Replacing all NaNs with the mean of the columns
data['likes'] = data['likes'].fillna(data['likes'].mean())
data['comment_count'] = data['comment_count'].fillna(data['comment_count'].mean())
data['dislikes'] = data['dislikes'].fillna(data['dislikes'].mean())
data['views'] = data['views'].fillna(data['views'].mean())

# Replacing missing values for categorical data with previous non null value
data['comments_disabled'] = data['comments_disabled'].fillna(method='ffill')
data['ratings_disabled'] = data['ratings_disabled'].fillna(method='ffill')
data['video_error_or_removed'] = data['video_error_or_removed'].fillna(method='ffill')
data.to_csv("USvideos_clean.csv")

# Checking if NaNs are present in the dataset
bool_series = pandas.isnull(data['likes'])
print(data[bool_series][0:5])
