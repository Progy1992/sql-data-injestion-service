from schemas import Book
from database import session_instance
import pandas as pd

csv_data = pd.read_csv("./dataset/books.csv", skiprows=1)
csv_data = csv_data.fillna(0)

book_data = []

for _, row in csv_data.iterrows():
    print(row)
    bookObject = Book(
        isbn=row[0],
        title=row[1],
        author=row[2],
        publicationYear=int(row[3]),
        publisher=row[4],
        image=row[5]
    )
    book_data.append(bookObject)

for data in book_data:
    try:
        session_instance.add(data)
        # session_instance.commit()
    except Exception as e:
        print(e)
# session_instance.add_all(book_data)
session_instance.commit()


session_instance.close()
