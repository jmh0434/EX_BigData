# Pandas를 pd로 import
import pandas as pd

# DataFrame 데이터
data = {"fruits" : ["apple", "orange", "banana", "strawberry", "kiwifruits"],
        "year": [2001, 2002, 2001, 2008, 2006],
        "time": [1, 4, 5, 6, 3]}

df = pd.DataFrame(data)
print(df)

