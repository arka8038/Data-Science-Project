# Data-Science-Project
Data science project on exploratory data analysis using Youtube trending video statistics 

Source of Dataset: Kaggle   
Size of Dataset: 40950 x 16   
Attributes:   
- Video_id ( String)

- Trending_date (String)

- Title (String)

- Channel_title (String)

- Category_id (ID)

- Publish_time (Date)

- Tags (String)

- Views (Integer)

- Likes (Integer)

- Dislikes (Integer)

- Comment_count (Integer)

- Thumbnail_link (URL)

- Comments_disabled (Boolean)

- Ratings_disabled (Boolean)

- Video_error_or_removed (Boolean)

- Description (String)

Description of files:

1. corr_linear.py:
This code performs correlation analysis for all numerical columns on the standardised dataset and Simple Linear Regression (SLR) for the dislikes and comment_count columns and plots the resulting least squares line.

2. corr_sample.py:
This code performs correlation analysis for all numerical columns on the cleaned dataset on a sample of 1000 rows, Simple Linear Regression (SLR) for likes vs comment_count and plots the resulting least squares line.

3. data_cleaning_interpolate.py:
Performs data cleaning for numerical columns (NaNs and missing values) by using the forward interpolation method. Categorical columns are replaced by the previous value in the column.

4. data_cleaning_mean.py:
Performs data cleaning for numerical columns (NaNs and missing values) by replacing all NaNs and missing values with the mean of the entire column. Categorical columns are replaced by the previous value in the column.

5. hyptest_correlation.py:
Performs hypothesis testing for the hypothesis that the mean of a random sample chosen is equal to the population mean. A random sample of 1000 rows is considered for the sample.

6. standardise.py:
Performs standardisation for the dataset so that the mean of the numerical columns is 0 and the standard deviation is 1. This centers the data around 0.
