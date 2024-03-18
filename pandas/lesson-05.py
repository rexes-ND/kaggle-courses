import pandas as pd

"""
The data type for a column in a DataFrame or a Series is known as the `dtype`.
"""

reviews = pd.DataFrame(
    {
        "country": ["Italy", "Portugal"],
        "points": [87, 87],
    }
)

reviews.price.dtype  # dtype('float64')
reviews.dtype  # `dtype` of every column in the DataFrame

# NOTE: One peculiarity to keep in mind is that columns consisting entirely of strings do not get their own type

reviews.points.astype("float64")

# A DataFrame or Series index has its own `dtype`:
reviews.index.dtype

# Entries missing values are given the value `NaN`, short for "Not a Number". It is of the `float64` dtype.
reviews[pd.isnull(reviews.country)]

# `fillna()` can be used to replace missing values.
reviews.region_2.fillna("Unknown")

# `replace()` can be used to replace a non-null value.
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
