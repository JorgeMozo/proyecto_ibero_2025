import numpy as np
import pandas as pd


def numpy_df():
    #create a dataframa with random
    df = pd.DataFrame(np.random.randn(5,3), columns =['A', 'B', 'C'])

    print("DataFrame: \n")
    print(df)

    arr = df.to_numpy()

    print("\nNumPy Array:")
    print(arr)

numpy_df()