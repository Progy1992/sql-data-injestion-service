from schemas import Rating
from database import session_instance
import pandas as pd

csv_data = pd.read_csv("./dataset/ratings.csv", skiprows=1)
csv_data = csv_data.fillna(0)

rating_data = []

for _, row in csv_data.iterrows():
    print(row)
    ratingObject = Rating(
        user_id=row[1],
        isbn=row[2],
        rating=float(row[3])
    )
    rating_data.append(ratingObject)

for data in rating_data:
    try:
        session_instance.add(data)
    except Exception as e:
        print(e)

session_instance.commit()
session_instance.close()
