from fuzzywuzzy import fuzz
import pandas as pd

def full(original,copy):
    return fuzz.ratio(original,copy)

def partial(original,copy):
    return fuzz.partial_ratio(original,copy)

df = pd.read_csv("movies.csv")
df = df[["title"]]
print("Input movies you like when you are done write 'e'")
selected = set()

while True:
    movie = input()
    if movie == "e":
        break
    if movie not in selected:
        df_copy = df.copy()
        df_copy["full"] = df_copy["title"].apply(lambda title: full(movie,title)).astype(int)
        df_copy["partial"] = df_copy["title"].apply(lambda title: partial(movie,title)).astype(int)
        df_copy.sort_values(by=["full","partial"],ascending=False,inplace=True)
    else:
        print("Movie already selected. \n")
        continue
    top_candidate = df_copy.head(1)
    if (top_candidate[['full','partial']].sum(axis=1).iloc[0]) // 2 < 80:
        print("Movie not found. Try spelling it right or another movie.")
        continue
    selected.add(str(top_candidate["title"].iloc[0]))






