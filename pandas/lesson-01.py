import pandas as pd

"""
There are two core objects in pandas: the `DataFrame` and the `Series`

A DataFrame is a table. It contains an array of individual entries, each of which has a certain value.
Each entry corresponds to a row (or record) and a column.
"""

pd.DataFrame(
    {
        "Yes": [50, 21],  # The "0, Yes" entry has a value of 50.
        "No": [131, 2],  # The "0, No" entry has a value of 131.
    }
)

pd.DataFrame(
    {
        "Bob": ["I liked it.", "It was awful."],
        "Sue": ["Pretty good.", "Bland."],
    }
)

"""
The syntax for declaring a new DataFrame object is a dictionary
whose keys are the column names (Bob and Sue),
and whose values are list of entries.

The dictionary-list constructor assigns values to the column labels,
but just uses an ascending count from 0 for the row labels.

The list of row labels used in DataFrame is known as an `Index`.
"""

pd.DataFrame(
    {
        "Bob": ["I liked it.", "It was awful."],
        "Sue": ["Pretty good.", "Bland."],
    },
    index=["Product A", "Product B"],
)

"""
A Series, by contrast, is a sequence of data values.
If a DataFrame is a table, a Series is a list.
And in fact you can create one with nothing more than a list
"""

pd.Series([1, 2, 3, 4, 5])

"""
A Series is, in essence, a single column of a DataFrame.
So you can assign row labels to the Series the same way as before,
using an index parameter. However, a Series does not have a column name,
it only has one overall name.
"""

pd.Series(
    [30, 35, 40],
    index=["2015 Sales", "2016 Sales", "2017 Sales"],
    name="Product A",
)

# wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")
# wine_reviews.shape
# wine_reviews.head()

# wine_reviews.to_csv("wine_reviews.csv")
