import pandas as pd

df = pd.read_csv("animes.csv")  
cat_keywords = "cat|cats|kitten|kittens|neko"
has_cat = df["synopsis"].str.contains(cat_keywords, case=False, na=False)

df["has_cat"] = has_cat
cats_count = df["has_cat"].sum()
total_anime = len(df)

print(f"Total: {total_anime}")
print(f"With cats in synopsis: {cats_count}")