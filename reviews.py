import pandas as pd

reviews_df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

summary = reviews_df.groupby('country').agg(count=('points', 'size'),points=('points', lambda x: round(x.mean(), 1))
).reset_index()

summary.to_csv('data/reviews-per-country.csv', index=False)

