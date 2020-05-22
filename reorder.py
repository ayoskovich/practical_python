"""
Quickly reordering the columns of a dataframe.
"""

import pandas as pd
import numpy as np


def reorder(df, *args, everything=True):
    """ Returns dataframe sorted using lists and functions.
    
    Params:
    df (pd.DataFrame): Input dataframe
    everything (bool): Whether or not to return all columns
    *args: Lists of columns or functions that return booleans
    """
    
    print(args)
    
    allCols = df.columns
    
    # For each arg:
    # If its a list, append
    colOrder = [x for x in args if isinstance(x, list)]

    if everything:
        return df[args[0]]
    else:
        print('Returning just a subset.') 


if __name__ == "__main__":
    
    np.random.seed(15)
    
    rand = lambda : np.random.randint(1, 4, 5)  
    cols = ['a', 'cost_two', 'b', 'test_price', 'test_thing', 'cost_one']

    df = pd.DataFrame({col : rand() for col in cols})
    reorder(df, ['a', 'b'], 'asdf', everything=True)

