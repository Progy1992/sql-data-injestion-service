from schemas import User
from database import session_instance
import pandas as pd


# saving user data into the table
csv_data = pd.read_csv("./dataset/users.csv", skiprows=1)

user_data = []
for _, row in csv_data.iterrows():
    print(row)
    userObject = User(
        user_id=int(float(row[0])),
        username=row[1],
        password=row[2],
        firstname=row[3],
        lastname=row[4],
        age=row[5]
    )
    user_data.append(userObject)

session_instance.add_all(user_data)
session_instance.commit()
