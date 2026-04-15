from src.analysis import *

df = load_data("data/poll_data.csv")
df = clean_data(df)

print("\nVote %:\n", vote_percentage(df))
print("\nRegion Analysis:\n", region_analysis(df))
print("\nAge Analysis:\n", age_analysis(df))