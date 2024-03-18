import pandas as pd

reviews = pd.DataFrame(
    {
        "country": ["Italy", "Portugal"],
        "points": [87, 87],
    }
)

reviews.country

"""
These are the two ways of selecting a specific Series out of a DataFrame:

reviews.country or reviews["country"]
"""

reviews.country[0]  # Italy

"""
Pandas indexing works in one of two paradigms.

The first is index-based selection: selecting data based on its numerical position in the data.
reviews.iloc[0]  # row first, column second
reviews.iloc[:, 0]

The second is label-based selection.
reviews.loc[0, 'country']
reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

Label-based indexing derives its power from the labels in the index.
reviews.set_index('title')
"""

# IMPORTANT NOTE: iloc indexes exclusively and loc indexes inclusively

reviews.country == "Italy"  # returns Series of bool

reviews.loc[reviews.country == "Italy"]

reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)]  # AND
reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)]  # OR
reviews.loc[(reviews.country.isin(["Italy", "France"]))]
reviews.loc[reviews.country.notnull()]

reviews["critic"] = "everyone"
reviews["index_backward"] = range(len(reviews), 0, -1)
