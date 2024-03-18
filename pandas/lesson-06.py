import pandas as pd

reviews = pd.DataFrame(
    {
        "country": ["Italy", "Portugal"],
        "points": [87, 87],
    }
)
"""
`rename()` lets you change index names and/or column names
using index or column keyword parameter, respectively.
"""
reviews.rename(columns={"points": "score"})
reviews.rename(index={0: "firstEntry", 1: "secondEntry"})

"""
Both the row index and the column index can have their own name attribute.
The complimentary `rename_axis()` method may be used to change these names.
"""
reviews.rename_axis("wines", axis="rows").rename_axis("fields", axis="columns")

"""
There are 3 core methods for combining DataFrames and/or Series:
- concat()
- join()
- merge()
"""

# Use `concat` to combine DataFrame or Series objects with same columns.
canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

# Use `join` to combine DataFrame objects with same index.
left = canadian_youtube.set_index(["title", "trending_date"])
right = british_youtube.set_index(["title", "trending_date"])

left.join(right, lsuffix="_CAN", rsuffix="_UK")
