import pandas
import numpy as np


def clean_interpolate(data_frame):

    data_frame['views'] = pandas.to_numeric(data_frame['views'], errors='coerce')
    data_frame['likes'] = pandas.to_numeric(data_frame['likes'], errors='coerce')
    data_frame['comment_count'] = pandas.to_numeric(data_frame['comment_count'], errors='coerce')
    data_frame['dislikes'] = pandas.to_numeric(data_frame['dislikes'], errors='coerce')

    # Checking if NaNs are present in the data_frameset
    series = pandas.isnull(data_frame['likes'])
    print(data_frame[series][0:5])

    # Replacing all NaNs with the mean of the columns
    data_frame['likes'] = data_frame['likes'].interpolate(method='linear', limit_direction='forward')
    data_frame['comment_count'] = data_frame['comment_count'].interpolate(method='linear', limit_direction='forward')
    data_frame['dislikes'] = data_frame['dislikes'].interpolate(method='linear', limit_direction='forward')
    data_frame['views'] = data_frame['views'].interpolate(method='linear', limit_direction='forward')

    # Replacing missing values for categorical data with previous non null value
    data_frame['comments_disabled'] = data_frame['comments_disabled'].fillna(method='ffill')
    data_frame['ratings_disabled'] = data_frame['ratings_disabled'].fillna(method='ffill')
    data_frame['video_error_or_removed'] = data_frame['video_error_or_removed'].fillna(method='ffill')
    return data_frame


data = pandas.read_csv("USvideos_original.csv", dtype=str)
data = clean_interpolate(data)
data.to_csv("USvideos_clean_interpolate.csv")

# Checking if NaNs are present in the dataset
bool_series = pandas.isnull(data['likes'])
print(data[bool_series][0:5])
