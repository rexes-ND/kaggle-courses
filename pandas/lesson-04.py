import pandas as pd

reviews = pd.DataFrame(
    {
        "country": ["Italy", "Portugal"],
        "points": [87, 87],
    }
)

reviews.groupby("points").points.count()
reviews.points.value_counts()

reviews.groupby("points").price.min()

"""
You can think of each group we generate as being a slice of our DataFrame containing only data with values that match.
This DataFrame is accessible to us directly using the `apply` method.
"""

reviews.groupby("winery").apply(lambda df: df.title.iloc[0])

# Group by more than one column.
reviews.groupby(["country", "province"]).apply(lambda df: df.loc[df.points.idxmax()])

reviews.groupby(["country"]).price.agg([len, min, max])


countries_reviewed = reviews.groupby(["country", "province"]).description.agg([len])
mi = countries_reviewed.index
type(mi)  # pandas.core.indexes.multi.MultiIndex

"""
Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices.
They also require two levels of labels to retrieve a value.
However, in general the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method.
"""
countries_reviewed.reset_index()

countries_reviewed.sort_values(by="len")

"""
sort_values() defaults to an ascending sort, where the lowest values go first.
"""

countries_reviewed.sort_values(by="len", ascending=False)

# To sort by index,
countries_reviewed.sort_index()

# To sort by more than one column,
countries_reviewed.sort_values(by=["country", "len"])
