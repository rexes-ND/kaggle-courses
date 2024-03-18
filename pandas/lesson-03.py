import pandas as pd

reviews = pd.DataFrame(
    {
        "country": ["Italy", "Portugal"],
        "points": [87, 87],
    }
)


reviews.points.describe()
"""
Generates a high-level summary of the attributes of the given column.
It is type-aware, meaning that its output changed based on the data type of the input.
"""

# Simple stat function in Pandas
reviews.points.mean()
reviews.country.unique()
reviews.country.value_counts()

"""
There are two mapping methods that you will use often.

First one is `map`:
reviews_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

`apply` is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
"""
